from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('What knife do you want today?')


def new(request):
    return HttpResponse('New Products')

