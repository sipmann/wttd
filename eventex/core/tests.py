from django.test import TestCase, Client


class SimpleTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.resp = self.c.get('/')

    def test_basic_addition(self):
        """
        Testa se o request retorna 200
        """
        self.assertEqual(self.resp.status_code, 200)
