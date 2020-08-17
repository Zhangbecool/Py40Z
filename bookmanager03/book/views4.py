from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo, PeopleInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def re(request, cat_id, good_id):
    """
    url形式提交
    :param request:
    :param cat_id:
    :param good_id:
    :return:
    """
    print('cat_id:{}, good_id:{}'.format(cat_id, good_id))
    return HttpResponse("re")


def getlist(request):
    """
    get方式 ？后key：value 方式提交
    :param request:
    :return:
    """
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.get('alist')
    print('a:{}, b:{}, alist:{}'.format(a, b, alist))
    return HttpResponse('getlsit')


def postl(request):
    """
    form 表单形式提交
    :param request:
    :return:
    """
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.get('alist')
    print('a:{}, b:{}, alist:{}'.format(a, b, alist))
    return HttpResponse('getlsit')


import json

def post_json(request):
    """
    json 方式请求
    :param request:
    :return:
    """
    res = request.body
    res = json.loads(res)
    print(res)
    return HttpResponse('post_json')


def get_header(request):
    """
    获取请求头
    :param request:
    :return:
    """
    h = request.META['HTTP_AAA']
    print(h)
    return HttpResponse('获取头')

def respons_(request):
    """
    编辑相应体
    :param request:
    :return:
    """
    return HttpResponse(content="标记响应体", content_type='text/html', status=200)

from django.http import JsonResponse

def jsonrespon(request):
    """
    Json子类
    :param request:
    :return:
    """
    cont = {
        "name": "比比东",
        "age": 22,
        "gender": "女"
    }

    return JsonResponse(cont, json_dumps_params={"ensure_ascii": False})


from django.shortcuts import redirect
def redirect1(request):
    return redirect('http://www.baidu.com')



def index(request):
    return HttpResponse('ok')
