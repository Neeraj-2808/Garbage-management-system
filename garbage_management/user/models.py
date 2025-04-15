from django.db import models

import uuid

# Create your models here. 

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class DistrictChoices(models.TextChoices):

    THIRUVANANTHAPURAM = 'THIRUVANANTHAPURAM','THIRUVANANTHAPURAM'

    KOLLAM ='KOLLAM','KOLLAM'

    PATHANAMTHITTA = 'PATHANAMTHITTA','PATHANAMTHITTA'

    ALAPPUZHA = 'ALAPPUZHA','ALAPPUZHA'

    KOTTAYAM = 'KOTTAYAM','KOTTAYAM'

    IDUKKI = 'IDUKKI','IDUKKI'

    ERNAKULAM = 'ERNAKULAM','ERNAKULAM'

    THRISSUR = 'THRISSUR','THRISSUR'

    PALAKKAD = 'PALAKKAD','PALAKKADU'

    MALAPPUARM = 'MALPPURAM','MALAPPURAM'

    KOZHIKODE = 'KOZHIKODE','KOZHIKODE'

    WAYANAD = 'WAYANAD','WAYANADU'

    KANNUR = 'KANNUR','KANNUR'

    KASARGOD = 'KASARGOD','KASARGOD'



class Users(BaseClass):

    profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    email = models.EmailField(unique=True)

    contact = models.CharField(max_length=15)

    address = models.CharField(max_length=50)

    post_office = models.CharField(max_length=50)

    district = models.CharField(max_length=50,choices=DistrictChoices.choices)

    pin_code = models.CharField(max_length=6)

    



    def __str__(self):

        return f'{self.name}'
    

    class Meta:

        verbose_name = 'User'

        verbose_name_plural = 'Users'

        ordering = ['-id']



