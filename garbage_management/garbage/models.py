from django.db import models

from user.models import BaseClass

# Create your models here. 


class WasteChoices(models.TextChoices):

    PLASTIC = 'Plastic','Plastic'

    ORGANIC ='Organic','Organic'

    EWASTE = 'E-Waste','E-Waste'

    OTHER = 'Other','Other'

class Status_Choices(models.TextChoices):
    PENDING = 'Pending','Pending'
    SCHEDULED ='Scheduled', 'Scheduled'
    COLLECTED = 'Collected', 'Collected'
    CANCELLED ='Cancelled', 'Cancelled'
    

class Garbage(BaseClass):

    user = models.ForeignKey('user.Users',null=True,on_delete=models.SET_NULL)

    garbage_type = models.CharField(max_length=50,choices=WasteChoices.choices)
    
    status = models.CharField(max_length=50,choices=Status_Choices.choices)

    quantity = models.DecimalField(max_digits=6,decimal_places=2)

    pick_up_date = models.DateField()

    address = models.CharField(max_length=50)


    def __str__(self):

        return f'{self.garbage_type}'
    

    class Meta:

        verbose_name = 'Garbage'

        verbose_name_plural = 'Garbages'

        ordering = ['-id']


