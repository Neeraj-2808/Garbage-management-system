from django.urls import path

from . import views

urlpatterns = [
    path('trucks/',views.TruckView.as_view(),name = 'trucks'),
    path('truck-add/',views.TruckFormView.as_view(),name = 'truck-add'),
    path('truck-update/<str:uuid>/',views.TruckUpdateView.as_view(),name='truck-update'),
    path('truck-delete/<str:uuid>/',views.TruckDeleteView.as_view(),name='truck-delete'),
    
]
