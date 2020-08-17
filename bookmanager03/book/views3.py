# from django.shortcuts import render
from django.http import HttpResponse
# from book.models import BookInfo, PeopleInfo

# Create your views here.


def re(request, cat_id, good_id):
    """
    url形式提交
    :param request:
    :param cat_id:
    :param good_id:
    :return:
    """
    print('cat_id:{}, good_id{}'.format(cat_id, good_id))
    return HttpResponse('re')


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


    return HttpResponse('getlist')



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

    return HttpResponse('postl')



import json

def post_json(request):
    """
    json 方式请求
    :param request:
    :return:
    """
    rus = request.body
    rus = json.loads(rus)
    print(rus)

    return HttpResponse('post_json')


def get_header(request):
    """
    获取请求头
    :param request:
    :return:
    """
    header = request.META['HTTP_AAA']
    print(header)

    return HttpResponse('get_header')



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
        "name": "王五",
        "age": 22,
        "gender": "男"

    }

    return JsonResponse(cont)

from django.shortcuts import redirect
def redirect1(request):
    return redirect('http://www.baidu.com')



def index(request):
    return HttpResponse('ok')
