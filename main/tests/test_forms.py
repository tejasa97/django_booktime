from django.test import TestCase
from django.core import mail
from main import forms

class TestForm(TestCase):

    def test_valid_contact_us_form_and_mail(self):

        form = forms.ContactForm({
            'name'   :'Ed Sheeran',
            'message':'Nothing'
        })
        self.assertTrue(form.is_valid())

        with self.assertLogs('main.forms', level="INFO") as cm:
            form.send_mail()

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Site message')

        self.assertGreaterEqual(len(cm.output), 1)

    def test_invalid_contact_us_form(self):

        form = forms.ContactForm({
            'name' : 'Taylor Swift'
        })

        self.assertFalse(form.is_valid())