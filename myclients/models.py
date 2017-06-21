# coding=utf-8
from django.db import models

from mycompanies.models import Company
from myusers.models import MyUser

# Create your models here.
class Client(models.Model):
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        
 
    name = models.CharField('Name', max_length=128, blank=False)
    phone = models.CharField('Phone', max_length=13, blank=True)
    firstname = models.CharField(
        'First name',
        max_length=40,
        null=True,
        blank=True)
    lastname = models.CharField(
        'Last name',
        max_length=40,
        null=True,
        blank=True)
    middlename = models.CharField(
        'Middle name',
        max_length=40,
        null=True,
        blank=True)
    email = models.EmailField(
        'E-mail',
        max_length= 255,
        db_index=True,
        null=True,
        blank=True
    )
    
    is_vip = models.BooleanField('VIP', default=False, blank=True)
    note = models.TextField(verbose_name ='Note', blank=True)
    company = models.ForeignKey(Company, verbose_name = 'Company', null=False)
    user = models.ForeignKey(MyUser, verbose_name = 'User', null=True, blank=True)
 
    def __str__(self):
        return self.name