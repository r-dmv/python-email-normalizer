# encoding: utf-8

from .base import BaseNormalizer


class FastMailNormalizer(BaseNormalizer):
    domains = ['fastmail.com', 'messagingengine.com', 'fastmail.fm']

    @classmethod
    def normalize(cls, local_part, domain):
        domain_segments = domain.split('.')

        if len(domain_segments) > 2:
            local_part = domain_segments[0]
            domain = '.'.join(domain_segments[1:])
        else:
            local_part = local_part.split('+')[0]

        return '{0}@{1}'.format(local_part, domain)
