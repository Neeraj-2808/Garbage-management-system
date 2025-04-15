from django.db import models

from user.models import BaseClass


# Create your models here.
class GarbageTruck(BaseClass):

    truck_number = models.CharField(unique=True,max_length=25)

    capacity = models.CharField(max_length=25)

    driver = models.ForeignKey('driver.Driver',null=True,on_delete=models.SET_NULL)

    current_location = models.CharField(max_length=255,blank=True,null=True)

    is_deleted = models.BooleanField(default=False)  # soft delete flag

    def delete(self):
    
        self.is_deleted = True
        
        self.save()




    def __str__(self):

        return f'{self.truck_number}'
    

    class Meta:

        verbose_name = 'Truck'

        verbose_name_plural = 'Trucks'

        ordering = ['-id']
