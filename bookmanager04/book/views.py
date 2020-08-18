from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')


def tieba(request, tieba_id):
    return HttpResponse(tieba_id)


def num(requset, num):
    return HttpResponse(num)


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
    name = request.session['name'] = 'tom'
    age = request.session['age'] = 13
    # print(name)
    request.session.set_expiry(60 * 2)
    return HttpResponse('set_session')


def get_session(request):

    name = request.session.get('name', '没有数据')
    age = request.session.get('age', '没有数据')
    # print('name')
    # request.session.clear()   # 删除session的值
    # request.session.flush()     # 删除session的值和键
    # del request.session['name']



    return HttpResponse(age)
