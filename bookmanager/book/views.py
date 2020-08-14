from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {
        'name':'爱丽丝'
    }
    return render(request, 'book/index.html', context)