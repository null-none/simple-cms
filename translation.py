from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions

from .models import Page

class PagesTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'content')

translator.register(Page, PagesTranslationOptions)