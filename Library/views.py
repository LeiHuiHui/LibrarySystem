# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
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
    return render(request, 'Library/index.html')


def submit(request):
    pass
