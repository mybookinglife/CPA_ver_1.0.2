from django.db import models
from mycompanies.models import Company
from myservices.models import Service

# Create your models here.
class Expert(models.Model):
    class Meta:
        db_table = 'experts'
        verbose_name = 'Expert'
        
    name = models.CharField(verbose_name= 'Full name', max_length=128, null=True, blank=False)        
    phone = models.CharField(verbose_name = 'Phone', max_length=13, blank=True)
    company = models.ForeignKey(Company, verbose_name = 'Company', null=False)
    short_description = models.CharField(verbose_name = 'Short description', max_length=255, blank=True)
    description = models.TextField(verbose_name ='Description', blank=True)
    is_active = models.BooleanField(verbose_name = 'Is active', default=True)
    
    def __str__(self):
        return self.name 
    
    
class Service_Experts(models.Model):
    class Meta:
        db_table = 'services_experts'
        verbose_name = 'Service experts'
        
    expert = models.ForeignKey(Expert, verbose_name = 'Expert', null=False)    
    service = models.ForeignKey(Service, verbose_name = 'Service', null=False)
    is_active = models.BooleanField(verbose_name = 'Is active', default=True)

    def __repr__(self):
        return models.Model.__repr__(self)
     
    def __str__(self):
        return self.service.name   
    
