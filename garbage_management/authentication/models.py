from django.db import models

from django.contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):

    ADMIN = 'Admin','Admin'

    USER = 'User','User'
    
    DRIVER = 'Driver','Driver'

    COLLECTOR = 'Garbage Collector','Garbage Collector'

class Profile(AbstractUser):

    role = models.CharField(max_length=30,choices=RoleChoices.choices)

    def __str__(self):
        return f'{self.username}-{self.role}'
    
    class Meta:

        verbose_name = 'Profile'

        verbose_name_plural = 'Profile'
