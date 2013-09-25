# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        'Form deve ter 4 campos'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'CPF deve aceitar só numeros'
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF deve ter 11 digitos'
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_option(self):
        'Email é opcional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_name_must_be_capitalized(self):
        'Nome deve ser capitalizado'
        form = self.make_validated_form(name='MAURICIO sipmann')
        self.assertEqual('Mauricio Sipmann', form.cleaned_data['name'])

    def test_must_inform_email_or_phone(self):
        'Email ou Fone deve ser informado'
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Maurcio Sipmann', email='email@email.com',
                    cpf='12345678901', phone_0='21', phone_1='12345678')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
