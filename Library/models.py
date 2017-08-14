# coding: utf-8
from django.db import models


class User(models.Model):
    user_id = models.CharField('学号', primary_key=True, max_length=14)
    user_name = models.CharField('姓名', max_length=20)

    def __str__(self):
        return self.user_name


class Excel(models.Model):
    excel_id = models.AutoField(primary_key=True)
    excel_name = models.CharField('表名', max_length=100)
    excel_tips = models.TextField('说明', blank=True)

    def __str__(self):
        return self.excel_name


class InitialHeaders(models.Model):
    SELECT = 'select'
    CHARFIELD = 'CharField'
    DATE = 'DateField'
    FIELD_TYPES = (
        (SELECT, '选择框'),
        (CHARFIELD, '文本框'),
        (DATE, '日期'),
    )

    excel_name = models.ForeignKey(Excel)
    header_name = models.CharField('统计项名称', max_length=20)
    header_type = models.CharField('统计项类型', max_length=20, choices=FIELD_TYPES, default=CHARFIELD)
