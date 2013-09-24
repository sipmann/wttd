# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:homepage'))

    def test_get(self):
        'Testa se o request retorna 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Index deve usar o template index.html'
        self.assertTemplateUsed(self.resp, 'core/index.html')
