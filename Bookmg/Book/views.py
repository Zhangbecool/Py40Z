from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'name':'who am i'
    }
    return render(request, 'Book/index.html', context)