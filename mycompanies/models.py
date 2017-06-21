from django.db import models
#from myusers.models import MyUser


class Activity(models.Model):
    class Meta:
        db_table = 'activities'
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'   
    
    name = models.CharField('Name', max_length=100, null=True, blank=False) 
    is_active = models.BooleanField('Is active', default=False)
    
    def __str__(self):
        return self.name
    

class Company(models.Model):
    class Meta:
        db_table = 'companies'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        
    is_active = models.BooleanField('Is active', default=False)
    name = models.CharField('Name', max_length=255, null=True, blank=False)
    legal_name = models.CharField('Legal name', max_length=255, null=True, blank=True)
    itn = models.CharField('ITN', max_length=12, blank=True) 
    phone = models.CharField('Phone', max_length=13, blank=True)
    legal_address = models.CharField('Legal address', max_length=255, null=True, blank=True)
    actual_address = models.CharField('Actual address', max_length=255, null=True, blank=True)
    activity = models.ForeignKey(Activity, null=False)
    description = models.CharField('Brief description', max_length=255, null=True, blank=True)
    full_description = models.TextField('HTML template', null=True, blank=True)
    schedule = models.BooleanField('Schedule for experts', default=False)
    language = models.CharField('Language', max_length=2, null=True, blank=True)
    timezone = models.CharField('Time zone', max_length=128, null=True, blank=False, default = 'UTC')

    def __str__(self):
        return self.name  
        
    def get_client_company(self):
        return self.client_set.all() 

    def get_service_company(self):
        return self.service_set.filter(is_active = True) 

