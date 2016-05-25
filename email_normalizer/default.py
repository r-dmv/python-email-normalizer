# encoding: utf-8

from .base import BaseNormalizer


class DefaultNormalizer(BaseNormalizer):

    @classmethod
    def normalize(cls, local_part, domain):
        return '{0}@{1}'.format(local_part, domain)
