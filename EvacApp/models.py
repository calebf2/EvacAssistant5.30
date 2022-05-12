from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    
class AddressProfile(models.Model):
    '''
    UserProfile model extends the built in Django User Model
    '''

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    town = models.CharField(verbose_name="City", max_length=100, null=True, blank=True)
    county = models.CharField(verbose_name="County", max_length=100, null=True, blank=True)
    zip_code = models.CharField(verbose_name="Zip Code", max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude", max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude", max_length=50, null=True, blank=True)