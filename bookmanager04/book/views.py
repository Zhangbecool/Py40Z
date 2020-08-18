from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')


def set_cookie(request):
    response = HttpResponse('set_cookie')
    response.set_cookie('name', 'tom', max_age=60)
    return response

