from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as authview

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
url(r'^reg/$', views.reg, name='reg'),
url(r'^reguser/$', views.reguser, name='reguser'),
url(r'^success/$', views.success, name='success'),

]