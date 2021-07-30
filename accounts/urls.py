
from django.urls import path

from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('resetpassword_validate/<uidb64>/<token>/',
         views.resetpassword_validate, name='resetpassword_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
 


]
