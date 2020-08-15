from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from book.models import Bookinfo


Bookinfo.objects.create()



def index(request):
    context = {
        'name': '爱丽丝'
    }
    return render(request, 'book/index.html', context)



