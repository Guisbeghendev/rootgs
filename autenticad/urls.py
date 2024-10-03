from django.urls import path
from . import views

urlpatterns = [
    path('area-restrita/', views.area_restrita, name='area_restrita'),
]
