from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('header.html')
    return HttpResponse(template.render())

# def index(request):
#     return HttpResponse("Hello world!")
