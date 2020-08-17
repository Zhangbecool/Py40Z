from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo, PeopleInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
"""
# ####### 级联查询 #########
# 查询书籍为1的所有人物信息
book = BookInfo.objects.get(id=1)  # 需要用get
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
people = PeopleInfo.objects.get(id=1)
people.book

# 查询图书，要求图书人物为"郭靖"
book = BookInfo.objects.filter(peopleinfo__name='郭靖')
book = BookInfo.objects.get(peopleinfo__name='郭靖')


# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains="八")
# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')
# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)

peo = PeopleInfo.objects.all()
peo[0:5:2]



p = Paginator(peo, 2)  # 数字代表一页的个数
p.count        # 查询总个数
p.num_pages    # 查询页数总数
p.page_range   # 查询页数范围
p.page(1)      # 查询第一页 返回第一页的结果集
p.page(1).object_list  # 显示第一页结果列表
p.page(1).has_next()   # 是否有下一页
p.page(1).has_previous()   # 是否有前一页
p.page(1).has_other_pages()  # 是否有其他页
p.page(1).next_page_number()  # 下一页的页数
p.page(1).previous_page_number()  # 上一页的页数
p.page(1).start_index()  # 本页第一个数据的索引
p.page(1).end_index()  # 本页最后一个数据的索引
"""

def listing(request):
    people_list = PeopleInfo.objects.all()
    paginator = Paginator(people_list, 5, orphans=3)  # orphans 参数设置最后一页的最少个数 如果少于则将数据放到前一页

    page = request.GET.get('page')
    print(page)

    try:
        pages = paginator.page(page).object_list
    except PageNotAnInteger:
        pages = paginator.page(1).object_list  # 如果输入的不是整数则返回第一页

    except EmptyPage:
        pages = paginator.page(paginator.num_pages).object_list  # 如果下标越界则返回最后一页

    return render(request, 'index.html', {'pages': pages})



def re(request, cat_id, good_id):
    """
    url形式提交
    :param request:
    :param cat_id:
    :param good_id:
    :return:
    """
    print('cat_id:{}, good_id:{}'.format(cat_id, good_id))

    return HttpResponse('内容')


def getlist(request):
    """
    get方式 ？后key：value 方式提交
    :param request:
    :return:
    """
    # res = request.GET.get('key')   # 只能接受一个值 多个取最后一个
    # print(res)
    res = request.GET.getlist('key')    # 接受的是一个列表
    print(res)

    return HttpResponse('内容')


def postl(request):
    """
    form 表单形式提交
    :param request:
    :return:
    """
    res = request.POST.get('a')
    res2 = request.POST.get('b')
    alist = request.POST.get('alist')
    print("a:{}  b:{}  alist:{}".format(res, res2, alist))

    return HttpResponse('内容')


import json

def post_json(request):
    """
    json 方式请求
    :param request:
    :return:
    """
    request_body = request.body
    request_str = request_body.decode()
    print(request_str)
    request_dict = json.loads(request_str)
    print(request_dict)
    print(request_dict['a'])
    return HttpResponse('内容')


def get_header(request):
    """
    获取请求头
    :param request:
    :return:
    """
    res = request.META['HTTP_AAA']
    print(res)
    print(request.method)       # 请求方法
    print(request.user)         # 请求的用户
    print(request.path)         # 请求的路径
    print(request.encoding)     # 请求的编码格式 none则使用浏览器默认
    return HttpResponse('内容')

def respons_(request):
    """
    编辑相应体
    :param request:
    :return:
    """
    # content 不能是对象
    # content 就是响应体的数据

    # content_type 响应数据的类型
    # MIME 类型
    # 语法格式: 大类/小类
    # text/html  application/json

    # status 响应状态码
    # 200 表示成功

    respons = HttpResponse(content="内容", content_type='text/html', status=200)
    return respons


from django.http import JsonResponse

def jsonrespon(request):
    """
    Json子类
    :param request:
    :return:
    """
    cont = {
        "a": "aaa",
        "b": "bbb"
    }
    # cont = json.dumps(cont)
    # return HttpResponse(content=cont)
    return JsonResponse(cont)   # 可以直接传递字典 内部进行了dumps方法

from django.shortcuts import redirect
def redirect1(request):
    return redirect('http://www.baidu.com')



def index(request):
    return HttpResponse('ok')
