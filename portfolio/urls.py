from django.urls import path
from portfolio import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.Home.as_view(), name= 'Home'),
    path('art/', views.Myart.as_view(), name= 'art'),
    path('art/<id>/', views.Myart.as_view(), name= 'art-details'),#Will be used for specific art
    path('art/<id>/upload/', views.Myart.as_view(), name= 'upload-details'),
    path('hire/', views.Hire.as_view(), name= 'hire'),
    path('hire/<id>/', views.Hire.as_view(), name= 'hired')#will be used for specific hire
    ]
