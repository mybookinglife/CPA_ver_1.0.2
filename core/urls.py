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
from django.contrib import admin
from core import views

from core import views as core_views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

# from rest_framework import routers
# from mybookings import views as booking_views
# 
# router = routers.DefaultRouter()
# router.register(r'bookings', booking_views.BookingViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/password_reset/$', auth_views.password_reset, 
        {'post_reset_redirect' : '/user/password_reset_done/'},name="password_reset"),
    url(r'^user/password_reset_done/$', auth_views.password_reset_done),
    url(r'^user/password_reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        auth_views.password_reset_confirm, {'post_reset_redirect' : '/user/password_reset_done/'},name="password_reset_confirm"),
    url(r'^user/', include('myusers.urls')),
    url(r'^myservices/', include('myservices.urls')),
    url(r'^myexperts/', include('myexperts.urls')),
    url(r'^myclients/', include('myclients.urls')),
    url(r'^mycompany/', include('mycompanies.urls')),
    url(r'^mybookings/', include('mybookings.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/mycompanies/', include('mycompanies.api.urls', namespace='api-mycompanies')),
    url(r'^api/myclients/', include('myclients.api.urls', namespace='api-myclients')), 
    url(r'^api/mybookings/', include('mybookings.api.urls', namespace='api-mybooking')),
    url(r'^mycalendar/', include('mycalendar.urls')),
    url(r'^obtain-auth-token/$', obtain_auth_token),
#     url(r'^chained/', include('chained_selects.urls')),
    url(r'^chained/(?P<app_name>[\w\-]+)/(?P<model_name>[\w\-]+)/(?P<method_name>[\w\-]+)/(?P<pk>[\w\-]+)/$', views.filterchain_all, name='filter_all'),
    url(r'^', core_views.index, name='home'),
    ]
