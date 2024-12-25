from django.shortcuts import render
from .forms import PrediccionForm


def inicio(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'predict':
            form = PrediccionForm(request.POST)
            if form.is_valid():
                numero = form.cleaned_data['username']
                resultado = f"Procesando número: {numero}"
                return render(request, 'juego.html', {'form': form, 'resultado': resultado})
        else:
            form = PrediccionForm()
    else:
        form = PrediccionForm()
    
    return render(request, 'juego.html', {'form': form})