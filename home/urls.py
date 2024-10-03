# home/urls.py
from django.urls import path
from .views import index  # Importa a função index

urlpatterns = [
    path('', index, name='home'),  # Define a URL para a página inicial
]
