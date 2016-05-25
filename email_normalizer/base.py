# encoding: utf-8


class BaseNormalizer(object):
    domains = []

    @classmethod
    def normalize(cls, local_part, domain):
        raise NotImplementedError
