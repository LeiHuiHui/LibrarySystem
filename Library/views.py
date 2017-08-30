# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from Library.models import *
from .forms import RegisterForm

app_name = 'Library'


def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    #  只有当请求为POST时，才表示用户提交了注册信息
    if request.method == 'POST':
        #  request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        #  这里提交的就是用户名(username)，学号(user_id)和邮箱(email)
        form = RegisterForm(request.POST)

        #  验证数据的合法性
        if form.is_valid():
            #  如果提交数据合法， 则调用表单的save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        #  请求不是 POST ，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()
        #  渲染模板
        #  如果用户正在访问注册页面，则渲染一个空的注册表单
        #  如果用户通过表单提交注册信息， 但是数据验证不合法， 则渲染的是一个带有错误信息的表单
    return render(request, 'Library/register.html', context={'form': form})


def index(request):
    excel_list = Excel.objects.all()
    return render(request, 'Library/index.html', context={'excel_list': excel_list})


def fill(request, excel_id):
    #  要从InitialHeaders表中，查找当前Excel对象的表头。事实上这一步已经在admin.py中ExcelAdmin重写的save_model()中做好了
    #  表头及其格式以header_name,header_type,...的字符串形式存储在Excel.excel_headers中，方便存储在数据库中
    #  现需要将headers转换成字典{'header_name':'header_type',...}，方便程序取用
    obj = Excel.objects.get(id=excel_id)
    header_list = obj.excel_headers.split(',')
    header_name = header_list[0::2]
    header_type = header_list[1::2]
    headers = {}
    for h in header_name:
        headers[h] = header_type[header_name.index(h)]
    if request.method == 'POST':
        request_data = ""
        for h in header_name:
            data = request.POST.get(h)
            request_data += h+','+str(data) + ','
        request_data = request_data[:len(request_data)-1]
        try:
            Fill.objects.create(user=request.user, excel=obj, fill_data=request_data)
            return HttpResponseRedirect(reverse('Library:submit'))
        except:
            raise Fill.DoesNotExist
        '''fill_obj = Fill.objects.create(user=request.user, excel=obj, fill_data=request_data)
        return redirect(reverse('Library:submit'))'''
    else:
        fill_obj = Fill.objects.get(user=request.user, excel=obj)
        if fill_obj:
            fill_data = fill_obj.fill_data.split(',')
            value_set = {}
            for i in range(len(fill_data)-1):
                if i % 2 == 0:
                    value_set[fill_data[i]] = fill_data[i+1]
            return render(request, 'Library/fill.html',
                          context={'obj': obj, 'headers': headers, 'value_set': value_set})
        else:
            return render(request, 'Library/fill.html',
                          context={'obj': obj, 'headers': headers, 'value_set': 0})


def submit(request):
    return HttpResponse("提交成功！")
