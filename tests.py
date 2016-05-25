import unittest
import sys
import mock

from email_normalizer import normalize, _get_mx_servers, _load_domains


class NormalizerTest(unittest.TestCase):
    def test_to_lower(self):
        self.assertEqual(normalize('UPPERCASE@DOMAIN.COM'), 'uppercase@domain.com')

    def test_resolving(self):
        with mock.patch('email_normalizer._get_mx_servers') as patched_method, \
                mock.patch('email_normalizer.google.GoogleNormalizer.normalize') as google_normalize:

            patched_method.return_value = ['mx.google.com']
            normalize('test@under_google_mx.com')

            self.failUnless(patched_method.called)
            self.assertTrue(google_normalize.called)

    def test_wrong_domain(self):
        domain = 'not_existing.domain'
        self.assertEqual(_get_mx_servers(domain), [])

    def test_default(self):
        self.assertEqual(normalize('test@domain.com', resolve=False), 'test@domain.com')

    def test_duplicated_domains(self):
        with mock.patch('email_normalizer.google.GoogleNormalizer.domains', ['samedomain.com']), \
                mock.patch('email_normalizer.yandex.YandexNormalizer.domains', ['samedomain.com']):
            self.assertRaises(ValueError, _load_domains)


class YandexNormalizerTests(unittest.TestCase):
    def test_ya(self):
        self.assertEqual(normalize('test@ya.ru'), 'test@yandex.ru')

    def test_narod(self):
        self.assertEqual(normalize('test@narod.ru'), 'test@yandex.ru')

    def test_yandexcom(self):
        self.assertEqual(normalize('test@yandex.com'), 'test@yandex.ru')

    def test_yandexby(self):
        self.assertEqual(normalize('test@yandex.by'), 'test@yandex.ru')

    def test_yandexkz(self):
        self.assertEqual(normalize('test@yandex.kz'), 'test@yandex.ru')

    def test_yandexua(self):
        self.assertEqual(normalize('test@yandex.ua'), 'test@yandex.ru')

    def test_extra(self):
        self.assertEqual(normalize('test+extra_data@yandex.ru'), 'test@yandex.ru')


class FastMailNormalizerTests(unittest.TestCase):
    def test_extra(self):
        self.assertEqual(normalize('test+extra_data@fastmail.com'), 'test@fastmail.com')

    def test_domain_segments(self):
        self.assertEqual(normalize('extra+data@test.fastmail.com'), 'test@fastmail.com')


class GoogleNormalizerTests(unittest.TestCase):
    def test_dots_remove(self):
        self.assertEqual(normalize('test.email@gmail.com'), 'testemail@gmail.com')

    def test_extra(self):
        self.assertEqual(normalize('test+extra_data@gmail.com'), 'test@gmail.com')


class MicrosoftNormalizerTests(unittest.TestCase):
    def test_extra(self):
        self.assertEqual(normalize('test+extra_data@outlook.com'), 'test@outlook.com')


class YahooNormalizerTests(unittest.TestCase):
    def test_extra(self):
        self.assertEqual(normalize('test-extra_data@yahoo.com'), 'test@yahoo.com')


class RamblerNormalizerTests(unittest.TestCase):
    def test_extra(self):
        self.assertEqual(normalize('test+extra_data@rambler.ru'), 'test@rambler.ru')


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(YandexNormalizerTests),
        unittest.makeSuite(NormalizerTest),
        unittest.makeSuite(FastMailNormalizerTests),
        unittest.makeSuite(GoogleNormalizerTests),
        unittest.makeSuite(MicrosoftNormalizerTests),
        unittest.makeSuite(YahooNormalizerTests),
        unittest.makeSuite(RamblerNormalizerTests),
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

