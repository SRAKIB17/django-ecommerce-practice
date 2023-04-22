from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import path, reverse, resolve


def index(request):
    context = {
        'mycar': {
            'brand': 'Ford',
            'model': 'Mustang',
            'year': '1964',
        },
    }
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render(context, request))
    # return HttpResponse(reverse('home'))
