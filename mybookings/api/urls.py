from django.conf.urls import url,include
from .views import (
    BookingListApiView,
    BookingDetailApiView,
    BookingUpdateApiView,
    BookingDeleteApiView,
    BookingCreateApiView
    )

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'list', BookingApiListView.as_view())
# router.register(r'events', views.booking_get_evets)

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$', BookingDetailApiView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', BookingUpdateApiView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', BookingDeleteApiView.as_view(), name='delete'),
    url(r'^create/$', BookingCreateApiView.as_view(), name='create'),
    url(r'^', BookingListApiView.as_view(), name='list'),
#     url(r'^', include(router.urls)),   

    ]