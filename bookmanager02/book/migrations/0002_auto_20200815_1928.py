# Generated by Django 2.2.5 on 2020-08-15 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '书籍信息'},
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='bookinfo',
        ),
    ]
