# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os.path

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render

from annoying.decorators import render_to


from .forms import ContactForm
from .models import Page


def page(request, page=None):
    menu = Page.objects.all().values('title', 'page').order_by('id')

    if page:
        current = Page.objects.filter(page=page).first()
    else:
        current = Page.objects.all().first()

    context = {
        'page': page,
        'menu': menu,
        'current': current,
        'active': current.page,
    }
    return render(request, '{0}.html'.format(current.page), context)


def contact(request):
    if request.method == 'GET':
        form = ContactForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'result': 'ok'}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'result': 'error'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'result': 'error'}), content_type="application/json")

