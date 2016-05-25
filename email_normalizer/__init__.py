# encoding: utf-8
import logging
from dns import resolver
from dns.exception import DNSException

from .base import BaseNormalizer
from .default import DefaultNormalizer

from .google import GoogleNormalizer
from .fastmail import FastMailNormalizer
from .microsoft import MicrosoftNormalizer
from .yahoo import YahooNormalizer
from .yandex import YandexNormalizer
from .rambler import RamblerNormalizer

logger = logging.getLogger(__name__)

__all__ = [
    'normalize',
]


NORMALIZERS = (
    GoogleNormalizer,
    FastMailNormalizer,
    MicrosoftNormalizer,
    YahooNormalizer,
    YandexNormalizer,
    RamblerNormalizer
)


_domain_normalizers = {}


def _load_domains():
    for cls in NORMALIZERS:
        assert issubclass(cls, BaseNormalizer)
        for domain in cls.domains:
            if domain in _domain_normalizers:
                raise ValueError('Duplicated domain value %s for normalizer %s', domain, cls)

            _domain_normalizers[domain] = cls


def _get_mx_servers(domain):
    try:
        answer = resolver.query(domain, 'MX')
        return [str(record.exchange).lower()[:-1] for record in answer]
    except DNSException as error:
        logger.error('DNS error for %s: %r', domain, error)
        return []


def _get_normalizer(domain, resolve):
    if domain in _domain_normalizers:
        return _domain_normalizers[domain]

    if resolve:
        for mx in _get_mx_servers(domain):
            for service_domain, normalizer in _domain_normalizers.iteritems():
                if mx.endswith(service_domain):
                    return normalizer

    return DefaultNormalizer


def normalize(email, resolve=True):
    local_part, domain = email.lower().split('@')

    return _get_normalizer(domain, resolve).normalize(local_part, domain)


_load_domains()
