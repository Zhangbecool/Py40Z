from django.urls import path, converters
from book.views import *



urlpatterns = [
    path('index/', index),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    # 转换器
    path('p/<int:tieba_id>', tieba),
]
