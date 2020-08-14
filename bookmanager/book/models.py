from django.db import models

# Create your models here.
class Bookinfo(models.Model):
    name = models.CharField(max_length=10)



class Peopleinfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField(default=False)
    # 添加外键
    book = models.ForeignKey(Bookinfo, on_delete=models.CASCADE)