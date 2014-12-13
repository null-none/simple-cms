from __future__ import unicode_literals

from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
