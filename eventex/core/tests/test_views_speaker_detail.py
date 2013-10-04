# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(
                name = 'Mauricio Sipmann',
                slug = 'mauricio-sipmann',
                url = 'http://sipmann.com',
                description = 'Vai saber')
        url = r('core:speaker_detail', kwargs={'slug': 'mauricio-sipmann'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET deve retornar status 200'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        'Testa se o template utilizado é o core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'Testa se o HTML final possui alguns dados básicos'
        self.assertContains(self.resp, 'Mauricio Sipmann')
        self.assertContains(self.resp, 'Vai saber')
        self.assertContains(self.resp, 'http://sipmann.com')

    def test_context(self):
        'Speaker deve estar no contexto'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        'Valida o raise de uma pagina 404 caso não ache o speaker'
        url = r('core:speaker_detail', kwargs={'slug': 'charmander'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
