from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('game/', views.game, name='game'),
    path('parameters/', views.parameters, name='parameters'),
]