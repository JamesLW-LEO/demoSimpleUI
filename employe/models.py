from datetime import datetime

from django.db import models

# Create your models here.
GENDER_TYPE = (
    ('0', '男'),
    ('1', '女'),
)


class Employee(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    gender = models.CharField(choices=GENDER_TYPE, max_length=2, verbose_name='性别')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    birthday = models.DateTimeField(verbose_name='出生日期')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改日期')

    class Meta:
        db_table = 'employee'
        verbose_name = '雇员'
        verbose_name_plural = verbose_name
        permissions = (
            ('export', 'export models as file'),
        )
