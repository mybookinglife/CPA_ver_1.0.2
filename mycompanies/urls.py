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
from django.contrib.auth import views as auth_view
from mycompanies import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.CompanyViewSet)

urlpatterns = [
    url(r'^password_change/$', auth_view.password_change, name='password_change'),
    url(r'^password_change_done/$', auth_view.password_change_done, name='password_change_done'),
#     url(r'^login_change/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
#         views.login_change_confirm, {'post_reset_redirect' : '/login_change_done/'},name="login_change_confirm"),
#     url(r'^login_change/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
#         auth_views.password_reset_confirm, {'post_reset_redirect' : '/user/password_reset_done/'},name="password_reset_confirm"),
    url(r'^login_change/$', views.login_change, name='login_change'),
    url(r'^$', views.company_index, name='company_index'),
    url(r'^api/', include(router.urls)),
    ]