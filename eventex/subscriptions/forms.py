# coding: utf-8
from django import forms
from eventex.subscriptions.models import Subscription
#from django.utils.translation import ugettext as _

class SubscriptionForm(forms.ModelForm):
    #name = forms.CharField(label=_('Nome'))
    #cpf = forms.CharField(label=_('CPF'), max_length=11)
    #email = forms.EmailField(label=_('Email'))
    #iphone = forms.CharField(label=_('Telefone'), max_length=20)
    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']
