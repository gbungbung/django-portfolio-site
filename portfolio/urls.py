from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from portfolio import views

app_name= 'portfolio'
urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('projects/', views.Arts.as_view(), name='projects'),
    path('upload/', views.AddArt.as_view(), name='upload'),
    path('artdetail/<int:pk>/', views.ArtDetail.as_view(), name='artdetail'),
    path('artdetail/<int:pk>/edit/', views.EditArt.as_view(), name='artedit'),
    path('artdetail/<int:pk>/delete/', views.ArtDelete.as_view(), name='artdelete'),
    path('hire/', views.Hire.as_view(), name='hire'),
    path('resume/', views.Resumee.as_view(), name='resume'),
    path('resumeadd/', views.Resumee_add.as_view(), name='resumeadd'),
    path('resumedetail/<int:pk>/', views.Resumee_detail.as_view(), name='resumedetail'),
    path('resumedetail/<int:pk>/edit/', views.Resumee_edit.as_view(), name='resumeedit'),
    path('resumedetail/<int:pk>/delete/', views.Resume_delete.as_view(), name='resumedelete'),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ]