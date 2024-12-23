from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


usertest = "admin"
passwordtest = "admin"  

def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if username == usertest and password == passwordtest:
            return redirect('landing:inicio')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')