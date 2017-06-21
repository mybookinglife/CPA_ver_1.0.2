from django.conf.urls import url,include
from .views import (
    ClientListApiView,
    ClientDetailApiView,
    ClientUpdateApiView,
    ClientDeleteApiView,
    ClientCreateApiView
    )

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$', ClientDetailApiView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', ClientUpdateApiView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', ClientDeleteApiView.as_view(), name='delete'),
    url(r'^create/$', ClientCreateApiView.as_view(), name='create'),
    url(r'^', ClientListApiView.as_view(), name='list'),
#     url(r'^', include(router.urls)),   

    ]