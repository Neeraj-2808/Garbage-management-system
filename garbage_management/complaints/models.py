from django.db import models

from user.models import BaseClass

# Create your models here. 




class Complaint(BaseClass):

    customer = models.ForeignKey('user.Users',null=True,on_delete=models.SET_NULL)

    title = models.CharField(max_length=25)

    description = models.CharField(max_length=200)

    suggestion = models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):

        return f'{self.title}'
    

    class Meta:

        verbose_name = 'Complaint'

        verbose_name_plural = 'Complaints'

        ordering = ['-id']





