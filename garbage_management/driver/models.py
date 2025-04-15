from django.db import models

from user.models import BaseClass

# Create your models here. 




class Driver(BaseClass):

    profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    name = models.CharField(max_length=25)

    license_number = models.CharField(max_length=25)

    email = models.EmailField(unique=True)

    contact = models.CharField(max_length=15)

    address = models.CharField(max_length=50)


    def __str__(self):

        return f'{self.name}'
    

    class Meta:

        verbose_name = 'Driver'

        verbose_name_plural = 'Drivers'

        ordering = ['-id']


