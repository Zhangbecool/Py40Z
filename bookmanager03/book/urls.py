from django.urls import path

from book.views import index, listing

urlpatterns = [
    path('index/', index),
    path('listing/', listing)
]
