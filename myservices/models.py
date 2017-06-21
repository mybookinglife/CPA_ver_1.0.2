from django.db import models

from mycompanies.models import Activity
from mycompanies.models import Company


# Create your models here.
class TypeService(models.Model):
    class Meta:
        db_table = 'types_service'
        verbose_name = 'Type myservices'
        verbose_name_plural = 'Types myservices'
    
    name = models.CharField('Name', max_length=128, blank=False)
    is_active = models.BooleanField('Is active', default=True)
    activity = models.ForeignKey(Activity, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Service(models.Model):
    class Meta:
        db_table = 'services'
        verbose_name = 'Service'
    
    name = models.CharField('Name', max_length=128, blank=False)
    is_active = models.BooleanField('Is active', default=True)
    type_service = models.ForeignKey(TypeService, null=False, blank=False)
    company = models.ForeignKey(Company, null=False)
    number_of_experts = models.IntegerField('Number of Experts', default=0)
    price = models.FloatField('Price', default=0)
    duration = models.IntegerField('Duration', default=0)
    
    def __str__(self):
        return self.name
    
    def get_expert_services(self):
        
        qs = self.service_experts_set.filter(is_active = True)
        results = list(qs)
        final = []
        for item in results:
            final.append(item.expert)
        
        return final  
