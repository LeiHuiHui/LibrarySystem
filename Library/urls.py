from django.conf.urls import include, url
from django.contrib import admin
from . import views


admin.autodiscover()
app_name = 'Library'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<excel_id>[0-9]+)/fill/', views.fill, name='fill'),
    url(r'^submit/', views.submit, name='submit'),
    #  url(r'^showlist/$', views.showList, name='ShowList'),
]
