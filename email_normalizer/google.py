# encoding: utf-8

from .base import BaseNormalizer


class GoogleNormalizer(BaseNormalizer):
    domains = ['google.com', 'googlemail.com', 'gmail.com']

    @classmethod
    def normalize(cls, local_part, domain):
        local_part = local_part.replace('.', '').split('+')[0]

        return '{0}@{1}'.format(local_part, domain)