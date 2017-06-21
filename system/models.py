from django.db import models
# from enum import unique


class Settings(models.Model):

    class Meta:
        db_table = 'settings'
        verbose_name = 'Settings'

    name = models.CharField('Name', max_length=128, blank=False)

    def __str__(self):
        return self.name
    
    
class Transactions(models.Model):

    class Meta:
        db_table = 'transactions'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    transaction_id = models.CharField('Transaction id', unique = True, db_index=True, max_length=128, blank=False)
    email = models.EmailField('E-mail', max_length=255, null=False, blank=False)
    lifetime = models.DateTimeField('Lifetime', null=False, blank=False)

    def __str__(self):
        return self.name