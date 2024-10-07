# autenticad/urls.py

from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
