# coding=utf-8
from django.contrib import admin
from myservices.models import Service
from myservices.models import TypeService
# Register your models here.

admin.site.register(Service)
admin.site.register(TypeService)