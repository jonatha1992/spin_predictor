from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.inicio, name='juego'),
]