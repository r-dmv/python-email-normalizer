# encoding: utf-8

# encoding: utf-8

from .base import BaseNormalizer


class RamblerNormalizer(BaseNormalizer):
    domains = ['rambler.ru', 'lenta.ru', 'autorambler.ru', 'myrambler.ru', 'ro.ru']

    @classmethod
    def normalize(cls, local_part, domain):
        local_part = local_part.split('+')[0]

        return '{0}@{1}'.format(local_part, domain)
