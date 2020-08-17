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
    print("cat_id:{}, good_id:{}".format(cat_id, good_id))

    return HttpResponse('ok')


def getlist(request):
    """
    get方式 ？后key：value 方式提交
    :param request:
    :return:
    """
    res = request.GET.get('a')
    res2 = request.GET.get('b')
    alist = request.GET.getlist('alist')
    print("a:{}, b:{}, alist:{}".format(res, res2, alist))

    return HttpResponse('getlist')




def postl(request):
    """
    form 表单形式提交
    :param request:
    :return:
    """
    a = request.POST.get('a')
    b = request.POST.get('b')
    l = request.POST.get('alist')
    print("a:{}, b:{}, alist:{}".format(a, b, l))

    return HttpResponse('postl')


import json

def post_json(request):
    """
    json 方式请求
    :param request:
    :return:
    """
    res = request.body
    # res = res.deconding()
    res = json.loads(res)
    print(res)
    return HttpResponse('post_josn')


def get_header(request):
    """
    获取请求头
    :param request:
    :return:
    """
    h = request.META['HTTP_AAA']
    print(h)
    return HttpResponse('header')


def respons_(request):
    """
    编辑相应体
    :param request:
    :return:
    """
    res = HttpResponse(content='response', content_type='text/html', status=200)
    return res

from django.http import JsonResponse

def jsonrespon(request):
    """
    Json子类
    :param request:
    :return:
    """
    cont = {
        "name": "张三",
        "age": 12
    }

    # cont = json.dumps(cont)
    return JsonResponse(cont, json_dumps_params={'ensure_ascii': False})    # 设置中文编码


from django.shortcuts import redirect
def redirect1(request):
    return redirect('http://www.baidu.com')



def index(request):
    return HttpResponse('ok')
