"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url 
from django.contrib.auth import views as auth_views

from core import views as core_views
from myusers import views as myuser_views

urlpatterns = [
    #url(r'^login/', auth_views.login, name='login'),
    url(r'^login/', myuser_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^add_user/$', myuser_views.add_user, name='add_user'),
    url(r'^add_company/$', myuser_views.add_company, name='add_company'),
    url(r'^', core_views.index),
    ]
