# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Mauricio Sipmann',
            cpf='12',
            email='email@email.com',
            phone='55-99999999'
        )

    def test_create(self):
        'Subscription deve salvar'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription deve ter o campo created_at automaticamente'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Mauricio Sipmann', unicode(self.obj))

    def test_paid_default_value_is_False(self):
        'Por default pago deve ser false'
        self.assertEqual(False, self.obj.paid)

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Mauricio Sipmann', cpf='12345678901',
                                    email='email@email.com', phone='55-99999999')
            
    def test_cpf_unique(self):
        'CPF deve ser unico'
        s = Subscription(name='Mauricio Sipmann',
            cpf='12345678901',
            email='contato@email.com',
            phone='55-99999999')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email deve ser unico'
        s = Subscription(name='Mauricio Sipmann',
            cpf='23456789012',
            email='email@email.com',
            phone='55-99999999')
        self.assertRaises(IntegrityError, s.save)

