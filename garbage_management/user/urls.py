from django.urls import path

from . import views

urlpatterns = [
    path('users/',views.UserView.as_view(),name = 'users'),
    path('user-form/',views.UserRegistration.as_view(),name = 'user-form'),
    path('user-update/<str:uuid>/',views.UserUpdateView.as_view(),name='user-update'),
    path('user-delete/<str:uuid>/',views.UserDeleteView.as_view(),name='user-delete'),

    
    
]
