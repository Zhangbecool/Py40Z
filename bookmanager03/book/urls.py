from django.urls import path

from book.views import index, re, getlist, postl, post_json, get_header, respons_, jsonrespon, redirect1
# from book.views import listing

urlpatterns = [
    path('index/', index),
    # path('listing/', listing),
    path('<cat_id>/<good_id>', re),
    path('getlist/', getlist),
    path('postl/', postl),
    path('post_json/', post_json),
    path('get/', get_header),
    path('respon/', respons_),
    path('jsonrespon/', jsonrespon),
    path('redirect/', redirect1),

]
