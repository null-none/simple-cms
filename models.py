from __future__ import unicode_literals

from django.db import models

from redactor.fields import RedactorField


class Contact(models.Model):
    email = models.EmailField(max_length=255)
    message = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email


PAGES = (
    ('contact', "Contact"),
)


class Page(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.TextField(max_length=255)
    description = models.TextField(max_length=500)
    content = RedactorField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    page = models.CharField(choices=PAGES, max_length=255)

    def menu(self):
        return Page.objects.all().values('title', 'page')

    def __unicode__(self):
        return self.title
