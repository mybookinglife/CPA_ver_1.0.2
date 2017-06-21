# coding=utf-8

from django.conf.urls import url, include
from mycalendar import views
from mybookings import views as viewsB
from mybookings.api.views import BookingListApiView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'get_events', BookingApiListView.as_view())

urlpatterns = [
#     url(r'get_events$', viewsB.BookingApiListView, name='get_events'),
#     url(r'get_events/$', views.get_events, name='get_events'),
    url(r'^$', views.show_calendar, name='show_calendar'), 
    url(r'^events/$', viewsB.booking_get_evets),
    url(r'^events/(?P<pk>[0-9]+)/$', viewsB.booking_detail),
#     url(r'^api/', include(router.urls)), 
    
    ]
