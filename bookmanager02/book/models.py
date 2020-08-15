from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10)
    pub_date = models.DateField()
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = "bookinfo"
        verbose_name = "书籍信息"

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )

    name = models.CharField(max_length=10)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    description = models.CharField(max_length=200, verbose_name="人物描述")
    is_delete = models.BooleanField(default=0)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物列表'

    def __str__(self):
        return self.name
