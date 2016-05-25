# encoding: utf-8

# encoding: utf-8

from .base import BaseNormalizer


class YandexNormalizer(BaseNormalizer):
    domains = ['yandex.ru',
               'ya.ru',
               'yandex.com',
               'yandex.by',
               'yandex.kz',
               'yandex.ua',
               'narod.ru']

    normalized_domain = 'yandex.ru'

    @classmethod
    def normalize(cls, local_part, domain):
        local_part = local_part.split('+')[0]

        """
        alise@yandex.ru == alise@ya.ru == alise@yandex.com ...
        """

        if domain != cls.normalized_domain and domain in cls.domains:
            domain = cls.normalized_domain

        return '{0}@{1}'.format(local_part, domain)
