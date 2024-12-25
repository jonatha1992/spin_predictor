from django.shortcuts import render
from .forms import ParametersForm, PrediccionForm

numeros_jugados = []  # Lista global para almacenar números
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]




def game(request):
    form = PrediccionForm()
    context = {
        'numeros': numeros_jugados,
        'resultado': '',
        'form': form,
        'black_numbers': black_numbers,
        'red_numbers': red_numbers
    }


    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'predict':
            form = PrediccionForm(request.POST)
            if form.is_valid():
                numero = form.cleaned_data['username']
                numeros_jugados.append(numero)  # Agregar número
                # Actualizar contexto de forma individual
                context['resultado'] = f"Ultimo número: {numero}"
                context['numeros'] = numeros_jugados
                context['form'] = PrediccionForm()
                
        elif action == 'delete':
            if numeros_jugados:  # Si hay números
                ultimo_numero = numeros_jugados.pop()  # Eliminar último
                # Actualizar contexto de forma individual
                context['resultado'] = f"Número {ultimo_numero} borrado."
                context['numeros'] = numeros_jugados
    
    # context['numeros'] = numeros_jugados  # Siempre incluir números en contexto
    return render(request, 'game.html', context)



parametros = {
    'type_roulette': '',
    'limit_game': 0,
}


def parameters(request):
    form = ParametersForm()
    if request.method == 'POST':
        action = request.POST.get('action')

    # context['numeros'] = numeros_jugados  # Siempre incluir números en contexto
    return render(request, 'parameters.html', parametros)