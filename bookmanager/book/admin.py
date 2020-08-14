from django.contrib import admin

# Register your models here.
from django.contrib import admin
from book.models import Bookinfo, Peopleinfo

admin.site.register(Bookinfo)
admin.site.register(Peopleinfo)