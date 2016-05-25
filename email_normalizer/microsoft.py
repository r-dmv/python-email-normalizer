# encoding: utf-8

from .base import BaseNormalizer


class MicrosoftNormalizer(BaseNormalizer):
    domains = ['hotmail.com', 'outlook.com', 'live.com']

    @classmethod
    def normalize(cls, local_part, domain):
        local_part = local_part.split('+')[0]

        return '{0}@{1}'.format(local_part, domain)
