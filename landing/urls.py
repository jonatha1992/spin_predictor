from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
]