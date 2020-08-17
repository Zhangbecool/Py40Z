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


def index(request):
    return HttpResponse('ok')
