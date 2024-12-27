from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('game/', views.game_view, name='game'),
    path('parameters/', views.parameters_view, name='parameters'),
]