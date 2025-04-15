from django.urls import path

from . import views

urlpatterns = [

    path('user-payment-detials/',views.UserPaymentView.as_view(),name='payment-details'),
    path('razorpay/',views.RazorpayView.as_view(),name='razorpay'),
    path('payment-verify/',views.PaymentVerify.as_view(),name='payment-verify'),
    

]