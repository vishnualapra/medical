"""tailoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from  django.contrib.auth.views import logout,login,password_reset,password_reset_confirm,password_reset_done,password_reset_complete
from django.views.generic.base import TemplateView

from . import views
app_name = 'web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    url(r'^web/',include('web.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'web/pages/samplepage/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'web/pages/samplepage/logout.html'}, name='logout'),
    url(r'^reset-password/$',password_reset, {'template_name': 'web/pages/samplepage/user-pass.html'}, name="reset_password"),
url(r'^reset-password/done/$',password_reset_done,{'template_name': 'web/pages/samplepage/reset_sent.html'}, name="password_reset_done"),
url(r'^reset-password/confirm/(?P<uidb64>[0=9A-Za-z]+)=(?P<token>.+)/$',password_reset_confirm,{'template_name': 'web/pages/samplepage/confirm.html'}, name="password_reset_confirm"),
url(r'^reset-password/complete/$',password_reset_complete,{'template_name': 'web/pages/samplepage/changed.html'}, name="password_reset_complete")

]
