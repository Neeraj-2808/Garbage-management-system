from django.db import models

from user.models import BaseClass

class PaymenyStatusChoices(models.TextChoices):

    PENDING = 'Pending','Pending'

    SUCCESS = 'Success','Success'

    FAILED = 'Failed','Failed'

class Payment(BaseClass):

    customer = models.ForeignKey('user.Users',on_delete=models.CASCADE)

    garbage = models.ForeignKey('garbage.Garbage', on_delete=models.CASCADE)

    amount = models.FloatField()

    status = models.CharField(max_length=20,choices=PaymenyStatusChoices.choices,default=PaymenyStatusChoices.PENDING)

    paid_at = models.DateTimeField(null=True,blank=True)


    def __str__(self):

        return f'{self.customer.name}'
    

    class Meta:

        verbose_name = 'Payment'

        verbose_name_plural = 'Payments'

        ordering = ['-id']

class Transactions(BaseClass):

    payment = models.ForeignKey('Payment',on_delete=models.CASCADE)

    rzp_order_id = models.SlugField()

    amount = models.FloatField()

    status = models.CharField(max_length=20,choices=PaymenyStatusChoices.choices,default=PaymenyStatusChoices.PENDING)

    transaction_at = models.DateTimeField(null=True,blank=True)

    rzp_payment_id = models.SlugField(null=True,blank=True)

    rzp_signature = models.TextField()





    def __str__(self):

        return f'{self.payment.customer.name} {self.status}'
    

    class Meta:

        verbose_name = 'Transaction'

        verbose_name_plural = 'Transactions'

        ordering = ['-id']












































# from students.models import BaseClass

# # Create your models here.

# class PaymentSettleChoices(models.TextChoices):

#     ONE_TIME = 'One Time','One Time'

#     INSTALLMENTS = 'Installments','Installments'

# class InstallmentChoices(models.IntegerChoices):

#     TWO = 2,'2'

#     THIRD = 3,'3'

#     FOUR = 4,'4'

#     FIVE = 5,'5'

#     SIX = 6,'6'

# class PaymentStructure(BaseClass):

#     student = models.OneToOneField('students.Students',on_delete=models.CASCADE)

#     one_time_or_installment = models.CharField(max_length=20,choices=PaymentSettleChoices.choices)

#     no_of_installments = models.IntegerField(choices=InstallmentChoices,null=True,blank=True)

#     fee_to_be_paid = models.FloatField()




    
#     def __str__(self):

#         return f'{self.student.first_name} {self.student.batch.name} Payment Structure'
    

#     class Meta:

#         verbose_name = 'Payment Structure'

#         verbose_name_plural = 'Payment Structure'

#         ordering = ['-id']

