from django.conf.urls import include, url
from django.contrib import admin
from . import views


admin.autodiscover()

urlpatterns = [
    url(r'^$', views.HomePage, name='HomePage'),
    url(r'^submit/$', views.Submit, name='Submit'),
    url(r'^showlist/$', views.ShowList, name='ShowList'),
]
