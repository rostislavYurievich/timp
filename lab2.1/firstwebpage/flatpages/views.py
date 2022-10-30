from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(u'Привет, Мир!') #,content_type="text/plain; charset=utf-8")


# Create your views here.
