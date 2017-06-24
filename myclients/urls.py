# coding=utf-8
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
from django.conf.urls import url, include
from myclients import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.ClientViewSet)


urlpatterns = [
    url(r'^add/$', views.add_client, name='add_client'),
    url(r'^add_client/$', views.add_client, name='add_client'),
    url(r'^edit_client/(?P<client_id>\d+)/$', views.edit_client, name='edit_client'),
    url(r'^get_info_client/(?P<client_id>\d+)/$', views.get_info_client, name='get_info_client'),
    url(r'^delete_client/(?P<client_id>\d+)/$', views.delete_client, name='delete_client'),
    url(r'^filter/(?P<value_filter>\w+)/$', views.list_clients, name='filter_clients'),  
    # url(r'^$', views.list_clients, name='list_clients'),
     url(r'^api/', include(router.urls)),
    ]
