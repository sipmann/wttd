# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Henrique Bastos',
                                        cpf='12345678901',
                                        email='email@email.com',
                                        phone='55-99999999')
        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))

    def test_get(self):
        'GET /inscricao/1/ deve retornar 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Deve usar um template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Contexto deve ser do tipo subscription'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Checa se realmente esta com os dados corretos'
        self.assertContains(self.resp, 'Henrique Bastos')

class DetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)
