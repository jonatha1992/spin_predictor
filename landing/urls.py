from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]