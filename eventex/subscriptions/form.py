from django import forms

class SubscriptionForm(forms.Form):
    Nome = forms.CharField()
    
    Email = form.EmailField()
    Fone = forms.CharField()
