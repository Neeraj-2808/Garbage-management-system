from django.urls import path 
from .import views

urlpatterns=[
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),

    path('map/',views.MapView.as_view(),name='map'),

    path('status/',views.StatusUpdateView.as_view(),name='status'),

    path('settings/',views.SettingsView.as_view(),name='settings'),

    path('reports/',views.ReportsView.as_view(),name='reports'),

    path('gallery/',views.GalleryView.as_view(),name='gallery'),

    path('about/',views.AboutView.as_view(),name='about'),

    path('faq/',views.FaqView.as_view(),name='faq'),
    

]

