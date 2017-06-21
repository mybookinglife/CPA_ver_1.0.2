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
from myservices import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.ServiceViewSet)


urlpatterns = [
    url(r'^add/$', views.add_service, name='add_service'),
    url(r'^add_service/$', views.add_service, name='add_service'),
    url(r'^edit_service/(?P<service_id>\d+)/$', views.edit_service, name='edit_service'),
    url(r'^get_info_service/(?P<service_id>\d+)/$', views.get_info_service, name='get_info_service'),
    url(r'^delete_service/(?P<service_id>\d+)/$', views.delete_service, name='delete_service'),
#     url(r'^(?P<service_id>\d+)/$', views.detail, name='detail_service'),
    
        
#     url(r'^filter/(?P<value_filter>\w+)/add_service/$', views.add_service),  
#     url(r'^filter/(?P<value_filter>\w+)/edit_service/$', views.edit_service),   
#     url(r'^filter/(?P<value_filter>\w+)/get_info_service/$', views.get_info_service),
#     url(r'^filter/(?P<value_filter>\w+)/delete_service/$', views.delete_service),   

    url(r'^filter/(?P<value_filter>\w+)/$', views.list_services, name='filter_service'),  
    url(r'^$', views.list_services, name='list_services'),
    url(r'^api/', include(router.urls)),
    ]
