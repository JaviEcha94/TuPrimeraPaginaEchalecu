from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_personas, name='listado'),
    path('agregar/', views.agregar_persona, name='agregar'),
]
