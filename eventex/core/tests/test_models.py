# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact

class SpeakerModel(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Mauricio Sipmann',
                                slug='mauricio-sipmann',
                                url='http://sipmann.com',
                                description='Vai saber')
        self.speaker.save()

    def test_create(self):
        'Speaker deve impactar no banco'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker deve ter uma funcao unicode'
        self.assertEqual(u'Mauricio Sipmann', unicode(self.speaker))

class ContactModel(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Mauricio Sipmann',
                                                slug='mauricio-sipmann',
                                                url='http://sipmann.com',
                                                description='Vai saber')
    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                        kind='E',
                                        value='mauricio@sipmann.com')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                        kind='P',
                                        value='55-91919191')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                        kind='F',
                                        value='55-91919191')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Tipo contato deve estar limitado a E, P ou F'
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)
