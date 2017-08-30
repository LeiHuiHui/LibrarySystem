# -*- coding: utf-8 -*-
from django.contrib import admin
from Library.models import *
from django.db import models
from django.db import connection
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


class HeadersInline(admin.StackedInline):
    model = InitialHeaders
    extra = 3


class ExcelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('表格信息', {'fields': ['excel_name', 'excel_tips']})
    ]
    inlines = [HeadersInline]

    def save_model(self, request, obj, form, change):
        # 从内联表InitialHeaders中整合表头信息，以header_name,header_type,...的形式存储
        obj.save()
        header_set = obj.header_set.all()  # 反向关联
        headers = ""
        for h in header_set:
            headers += h.header_name+','+h.header_type+','
        obj.excel_headers = headers[:len(headers)-1]
        obj.save()
    '''def save_model(self, request, obj, form, change):
        obj.save()
        fill_name = obj.fill_generator()
        if fill_name:
            cursor = connection.cursor()
            cursor.execute("ALTER db.sqlite3_%s ADD COLUMN fill_date TEXT" %fill_name)'''


admin.site.register(User, UserAdmin)
admin.site.register(Excel, ExcelAdmin)
admin.site.register(InitialHeaders)
