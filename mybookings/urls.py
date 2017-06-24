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
from mybookings import views
from rest_framework import routers
from mybookings.views import BookingCreate
from django.views import generic

router = routers.DefaultRouter()
router.register(r'list', views.BookingViewSet)
# router.register(r'events', views.booking_get_evets)

urlpatterns = [

    url(r'^chat/$', views.home),
    url(r'^add/$', views.add_booking, name='add_booking'),
    url(r'^add_booking/$', views.add_booking, name='add_booking'),
#     url(r'^add_booking2/$', BookingCreate.as_view(), name='add_booking2'),
    url(r'^edit_booking/(?P<booking_id>\d+)/$', views.edit_booking, name='edit_booking'),
    url(r'^get_info_booking/(?P<booking_id>\d+)/$', views.get_info_booking, name='get_info_booking'),
#     url(r'^cansel_booking/(?P<booking_id>\d+)/$', views.cansel_booking, name='cansel_client'),
    url(r'^delete_booking/(?P<booking_id>\d+)/$', views.delete_booking, name='delete_client'),
    url(r'^filter/(?P<value_filter>\w+)/$', views.list_bookings, name='filter_bookings'),
#     url(r'^list/$', BookingList.as_view()),
    url(r'^work/$', views.list_bookings, name='list_of_working_bookings'),
    url(r'^completed/$', views.list_bookings, name='list_of_completed_bookings'),
    # url(r'^list/$', views.list_bookings, name='list_bookings'),
    # url(r'^', generic.TemplateView.as_view(template_name='bookings_root.html'), name='list_bookings'),


#     url(r'^api/', include(router.urls)),
    ]
