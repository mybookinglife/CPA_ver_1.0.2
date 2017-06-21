# coding=utf-8
from django.contrib import admin
from myexperts import models
# Register your models here.

admin.site.register(models.Expert)
admin.site.register(models.Service_Experts)