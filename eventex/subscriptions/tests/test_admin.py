# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin
from mock import Mock

class MarkAsPaidTest(TestCase):
    def setUp(self):
        'Instancia o Model Admin'
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)

        Subscription.objects.create(name='Mauricio Sipmann',
                                    cpf='12345678901',
                                    email='email@email.com')

    def test_has_action(self):
        'Action esta instalada'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        'Marca todos como pago'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
