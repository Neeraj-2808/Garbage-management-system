from django.urls import path 

from .import views

from .views import update_garbage_status

urlpatterns=[
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),

    path('home/',views.HomeView.as_view(),name='home'),

    path('garbagesection/',views.GarbageSectionView.as_view(),name='garbagesection'),

    path('map/',views.MapView.as_view(),name='map'),

    path('status/',views.StatusUpdateView.as_view(),name='status'),

    path('settings/',views.SettingsView.as_view(),name='settings'),

    path('reports/',views.ReportsView.as_view(),name='reports'),

    path('gallery/',views.GalleryView.as_view(),name='gallery'),

    path('about/',views.AboutView.as_view(),name='about'),

    path('faq/',views.FaqView.as_view(),name='faq'),

    path('garbage-register/',views.GarbageRegisterView.as_view(),name='garbage-register'),

    path('garbage-list/',views.GarbageView.as_view(),name = 'garbage-list'),

    path('garbage/<str:uuid>/update-status/', update_garbage_status, name='update_status'),

    path('garbage-update/<str:uuid>/',views.GarbageUpdateView.as_view(),name='garbage-update'),

    path('garbage-delete/<str:uuid>/',views.GarbageDeleteView.as_view(),name='garbage-delete'),
    

]

