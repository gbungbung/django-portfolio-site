from django.urls import path
from portfolio import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.Home.as_view(), name= 'Home'),
    path('art/', views.Myart.as_view(), name= 'art'),
    path('art/<id>/', views.Myart.as_view(), name= 'art-details'),
    path('art/<id>/upload/', views.Myart.as_view(), name= 'upload-details'),
    path('contact/', views.Contact.as_view(), name= 'cantact'),
    path('contact/<id>/', views.Contact.as_view(), name= 'sent')
    ]
