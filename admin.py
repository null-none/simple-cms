from __future__ import unicode_literals

from django.contrib import admin
from django import forms

from modeltranslation.admin import TranslationAdmin
from redactor.widgets import RedactorEditor

from .models import Contact, Page


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        widgets = {
           'short_text': RedactorEditor(),
        }

class PageAdmin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
            'js/redactor.js'
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        form = PageAdminForm

admin.site.register(Page, PageAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'message', 'created')
    search_fields = ['email', 'message']

admin.site.register(Contact, ContactAdmin)
