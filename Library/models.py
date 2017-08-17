# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.CharField('学号', primary_key=True, max_length=14)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass


class Excel(models.Model):
    excel_id = models.AutoField(primary_key=True)
    excel_name = models.CharField('表名', max_length=100)
    excel_tips = models.TextField('说明', blank=True)
    excel_headers = models.TextField('表头', blank=True)

    def __str__(self):
        return self.excel_name

    '''
    from django.db.backends import sqlite3
    from django.db import connection, transaction
    def fill_generator(self):
        fill_name = 'Library_Fill'+str(self.excel_id)

        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE db.sqlite3 %s (user_id CHAR(50) PRIMARY KEY  NOT NULL )" %fill_name)
            return fill_name
        except:
            return False'''


class InitialHeaders(models.Model):
    SELECT = 'select'
    CHARFIELD = 'CharField'
    DATE = 'DateField'
    FIELD_TYPES = (
        (SELECT, '选择框'),
        (CHARFIELD, '文本框'),
        (DATE, '日期'),
    )

    excel_name = models.ForeignKey(Excel, related_name='header_set')  # 这里应该是excel_id，但是现在数据库已经建好了，不好修改
    header_name = models.CharField('统计项名称', max_length=20)
    header_type = models.CharField('统计项类型', max_length=20, choices=FIELD_TYPES, default=CHARFIELD)

    def __str__(self):
        return str(self.excel_name)+'_'+self.header_name+'('+self.header_type+')'


class Fill(models.Model):
    user_id = models.ManyToManyField(User, related_name="excel_filled")
    excel_id = models.ManyToManyField(Excel, related_name="user_filled")
