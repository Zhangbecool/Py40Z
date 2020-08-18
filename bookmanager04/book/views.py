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
    name = request.session['user'] = 'tom'
    age = request.session['age'] = 13
    # print(name)
    request.session.set_expiry(60 * 2)
    print(request.user)
    return HttpResponse('set_session')


def get_session(request):

    name = request.session.get('name', '没有数据')
    age = request.session.get('age', '没有数据')
    # print('name')
    # request.session.clear()   # 删除session的值
    # request.session.flush()     # 删除session的值和键
    # del request.session['name']

    return HttpResponse(age)

from django.views import View



class register(View):

    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')

from django.contrib.auth.mixins import LoginRequiredMixin

class mywork(LoginRequiredMixin,View):

    def get(self, request):
        return HttpResponse('个人中心 get')

    def post(self, request):
        return HttpResponse('个人中心 post')
