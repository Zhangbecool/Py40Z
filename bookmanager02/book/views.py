from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo, PeopleInfo

# Create your views here.
# ##############增加#################
book = BookInfo(
    name="python入门",
    pub_date='2010-01-01'
)
book.save()

book = BookInfo.objects.create(
    name='HTML入门',
    pub_date='2011-2-3'
)

# ###########修改##############

book = BookInfo.objects.get(id=6)
book.name = 'CSS入门'

book = BookInfo.objects.filter(id=6).update(name='大威天龙')

# #############删除##############

book = BookInfo.objects.get(id=6)
book.delete()

BookInfo.objects.filter(id=5).delete()


# ################查询##############
book = BookInfo.objects.get(id=1)

book = BookInfo.objects.filter(id__gt=1)

# 查询编号为1的图书
book = BookInfo.objects.get(id=1)
# 查询书名包含'湖'的图书
book = BookInfo.objects.filter(name__contains="湖")
# 查询书名以'部'结尾的图书
book = BookInfo.objects.filter(name__endswith="部")
# 查询书名为空的图书
book = BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
book = BookInfo.objects.filter(id__in=[1, 3, 5])
# 查询编号大于3的图书
book = BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
book = BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
book = BookInfo.objects.filter(pub_date__gt='1990-1-1')
from django.db.models import F
# 查询阅读量大于等于评论量的图书。
book = BookInfo.objects.filter(readcount__gt=F('commentcount'))
# 查询阅读量大于2倍评论量的图书。
book = BookInfo.objects.filter(readcount__gt=2*F('commentcount'))
book = BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
book = BookInfo.objects.filter(readcount__lt=2*F('commentcount'))
book = BookInfo.objects.filter(readcount__lt=F('commentcount')/2)
# 查询阅读量大于20，并且编号小于3的图书
from django.db.models import Q
book = BookInfo.objects.filter(readcount__gt=20, id__lt=3)
book = BookInfo.objects.filter(Q(readcount__gt=20) & Q(id__lt=3))
# 查询阅读量大于20，或编号小于3的图书
book = BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))
# 查询编号不等于3的图书。
book = BookInfo.objects.filter(~Q(id=3))
book = BookInfo.objects.exclude(id=3)



def index(request):
    return HttpResponse('ok')
