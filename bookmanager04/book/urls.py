from django.urls import path
from book.views import *


urlpatterns = [
    path('index/', index),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
]
