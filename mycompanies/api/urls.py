from django.conf.urls import url,include
from .views import (
    CompanyListApiView,
    ActivityListApiView,
    CompanyDetailApiView,
    CompanyUpdateApiView,
    CompanyDeleteApiView,
    CompanyCreateApiView
    )

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$', CompanyDetailApiView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', CompanyUpdateApiView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', CompanyDeleteApiView.as_view(), name='delete'),
    url(r'^create/$', CompanyCreateApiView.as_view(), name='create'),
    url(r'^activity/$', ActivityListApiView.as_view(), name='activity'),
    url(r'^', CompanyListApiView.as_view(), name='list'),
#     url(r'^', include(router.urls)),   

    ]