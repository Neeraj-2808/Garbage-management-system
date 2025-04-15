from django.urls import path

from . import views

urlpatterns = [
    path('users/',views.UserView.as_view(),name = 'users'),
    path('user-form/',views.UserRegistration.as_view(),name = 'user-form'),

    
    
]
