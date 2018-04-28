# coding=utf-8
from django.db import models
# import pytz
from mycompanies.models import Company
from myclients.models import Client
from myservices.models import Service
from myexperts.models import Expert
from pytz import timezone
from channels.channel import Group


# from datetime import datetime

# Create your models here.
class Booking(models.Model):
    class Meta:
        db_table = 'bookings'
        verbose_name = 'Booking'
        ordering = ('-date_time',)
    
#     company_user = request.user.mycompanies
            
#     date_time = models.DateTimeField("Date", null=False, blank=False, default = datetime.now(tz=pytz.timezone('UTC')))
    date_time = models.DateTimeField("Date", null=False, blank=False)
    date = models.DateField("Date", null=False, blank=False)
    time = models.TimeField("Time", null=False, blank=False)
    company = models.ForeignKey(Company, verbose_name='Company', null = False)
    client = models.ForeignKey(Client, verbose_name='Client', null = False)
    service = models.ForeignKey(Service, verbose_name="Service", null = False)
    expert = models.ForeignKey(Expert, verbose_name='Expert', null = False)
    note = models.TextField('Note', blank=True)
    comment = models.TextField('Comment', blank=True)
    is_new = models.BooleanField("Is new", default=True)
    is_cansel = models.BooleanField("Is cancel", default=False, blank = True)
    is_finished = models.BooleanField('Is finished', default=False, blank = True)
    
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
        
    def __str__(self):
        return 'Booking №'+ str(self.id) +' on '+self.date_time.astimezone(timezone(self.company.timezone)).__str__()

    def save(self, *args, **kwargs):
        super(Booking, self).save(*args, **kwargs)
        Group('_mybookings_' + str(self.company_id)).send({'text': 'update'})

    def delete(self, *args, **kwargs):
        super(Booking, self).delete(*args, **kwargs)
        Group('_mybookings_' + str(self.company_id)).send({'text': 'update'})
