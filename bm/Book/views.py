from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = { 
            'name':'who would ever wanner be king'
            
            }

    return render(request, 'Book/index.html', context)


def login(request):
    return HttpResponse('登录')



