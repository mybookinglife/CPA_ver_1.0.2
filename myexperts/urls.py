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
from myexperts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.ExpertViewSet)


urlpatterns = [
    url(r'^add/$', views.add_expert, name='add_expert'),
    url(r'^sendmail/$', views.sendmail, name='sendmail'),
    url(r'^add_expert/$', views.add_expert, name='add_expert'),
    url(r'^add_service_experts/(?P<expert_id>\d+)/(?P<service_id>\d+)/$', views.add_service_experts, name='add_service_experts'),
    url(r'^edit_expert/(?P<expert_id>\d+)/$', views.edit_expert, name='edit_expert'),
    url(r'^get_info_expert/(?P<expert_id>\d+)/$', views.get_info_expert, name='get_info_expert'),
    url(r'^get_service_experts/(?P<expert_id>\d+)/$', views.get_service_experts, name='get_service_experts'),
    url(r'^delete_expert/(?P<expert_id>\d+)/$', views.delete_expert, name='delete_expert'),
    url(r'^delete_service_experts/(?P<expert_id>\d+)/(?P<service_id>\d+)/$', views.delete_service_experts, name='delete_service_experts'),
    url(r'^filter/(?P<value_filter>\w+)/$', views.list_expert, name='filter_expert'),  
    url(r'^$', views.list_expert, name='list_experts'),
    url(r'^api/', include(router.urls)),
    ]