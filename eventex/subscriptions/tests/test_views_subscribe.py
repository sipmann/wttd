# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get(self):
        'GET /inscricao/ deve retornar o status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Subscribe deve usar o template subscription_form.html'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        'HTML deve conter os seguintes inputs'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, 'type="submit"')
    
    def test_csrf(self):
        'HTML deve ter o token csrf'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'O context deve ter uma variavel do tipo form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
     
    def test_form_has_fields(self):
        'Form deve ter 4 campos'
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Mauricio Sipmann',
                    cpf='12345678901',
                    email='email@email.com',
                    phone='55-99999999')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Valida se o resultado do post foi um redirect'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Valida se o POST realmente salvou um registro'
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Mauricio Sipmann',
                    cpf='12345678901212',
                    email='email@email.com',
                    phone='55-9999999999999999999999999')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Dados inválidos não devem redirecionar'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Form deve ter erros'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Não deve salvar os dados'
        self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        'Checa se non_field_errors esta visivel no template'
        invalid_data = dict(name='Mauricio Sipmann', cpf='12345678901')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)

        self.assertContains(response, '<ul class="errorlist">')
