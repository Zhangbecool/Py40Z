from django.urls import path, converters
from book.views import *

"""
自定义转换器 
1. 定义转换器类(需求)
2. 要添加到系统的 转换器列表中
3. 使用
"""
class PhoneConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

converters.register_converter(PhoneConverter, 'Phone')


urlpatterns = [
    path('index/', index),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    # 转换器
    path('p/<int:tieba_id>', tieba),
    path('register_/<Phone:num>/', num),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('register/', register.as_view()),
]
