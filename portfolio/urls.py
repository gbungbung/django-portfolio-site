from django.urls import path
from django.contrib.auth.views import LogoutView

from portfolio import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.Home.as_view(), name= 'Home'),
    path('art/', views.Myart.as_view(), name= 'art'),
    path('art/<id>/', views.ArtDetail.as_view(), name= 'artdetail'),                             #Will be used for specific art
    path('upload/', views.Upload.as_view(), name= 'upload'),
    path('hire/', views.Hire.as_view(), name= 'hire'),
    path('hire/<id>/', views.Hire.as_view(), name= 'hired'),                                     #will be used for specific hire
    path('resume/', views.Resume.as_view(), name= 'resume'),
    path('resumeadd/', views.Resume_add.as_view(), name= 'resumeadd'),
    path('resume/<id>/edit', views.Resume_edit.as_view(), name= 'resumeedit'),
    path('resume/<id>/delete', views.Resume.as_view(), name= 'resumedelete'),
    path('register/', views.Register.as_view(), name= 'register'),
    path('signin/', views.Login.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    ]
