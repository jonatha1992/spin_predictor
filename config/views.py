# filepath: /d:/Repositorio/jonatha1992/spin_predictor/config/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')