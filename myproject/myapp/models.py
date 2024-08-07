from django.db import models

# Create your models here.
class Tour(models.Model):

    oregin_country = models.CharField(max_length=64)
    destiny_country = models.CharField(max_length=64)
    nights = models.IntegerField()
    price = models.IntegerField()
    
    #str
    def __str__(self):
        return (f'Id:{self.id} From {self.oregin_country} To {self.destiny_country} {self.nights} nights costs {self.price}$')

