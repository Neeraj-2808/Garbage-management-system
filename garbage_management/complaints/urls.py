from django.urls import path

from . import views

urlpatterns = [
    path('complaint/',views.ComplaintView.as_view(),name = 'complaint'),
    path('complaint-register/',views.ComplaintFormView.as_view(),name = 'complaint-register'),
    path('complaint-detail/<str:uuid>/',views.ComplaintDetailView.as_view(),name='complaint-detail'),
    path('complaint-delete/<str:uuid>/',views.ComplaintDeleteView.as_view(),name='complaint-delete'),
    path('complaintthanks/',views.ComplaintThankyouView.as_view(),name = 'complaintthanks'),

]