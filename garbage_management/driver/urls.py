from django.urls import path

from . import views

urlpatterns = [
    path('drivers/',views.DriverView.as_view(),name = 'drivers'),
    path('driver-add/',views.DriverFormView.as_view(),name = 'driver-add'),
    path('driver-update/<str:uuid>/',views.DriverUpdateView.as_view(),name='driver-update'),
    path('driver-delete/<str:uuid>/',views.DriverDeleteView.as_view(),name='driver-delete'),
    
    
]
