from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')


def tieba(request, tieba_id):
    return HttpResponse(tieba_id)


def set_cookie(request):
    response = HttpResponse('set_cookie')
    response.set_cookie('name', 'tom', max_age=60*2)
    return response


def get_cookie(request):

    # cookie = request.COOKIES['name']
    # 没有cookie不会报错
    cookie = request.COOKIES.get('name')
    response = HttpResponse(cookie)
    # 删除cookie
    response.delete_cookie('name')

    return response


def set_session(request):
    request.session('name', 'tom')
