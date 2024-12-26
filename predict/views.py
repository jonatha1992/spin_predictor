from django.shortcuts import redirect, render
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
    'neighbors': 0,
    'probability': 0.0,
}


def parameters(request):
    form = ParametersForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        action = request.POST.get('action')
        form = ParametersForm(request.POST)
        
        if action == 'init' and form.is_valid():
            # Actualizar parámetros globales
            parametros['type_roulette'] = form.cleaned_data['type_roulette']
            parametros['limit_game'] = form.cleaned_data['limite_games']
            parametros['neighbors'] = form.cleaned_data['neighbors']
            parametros['probability'] = form.cleaned_data['probability']
            return redirect('predict:game')
            
        elif action == 'delete':
            # Resetear parámetros
            parametros['type_roulette'] = ''
            parametros['limit_game'] = 1
            parametros['neighbors'] = 0
            parametros['probability'] = 0.0
            form = ParametersForm()  # Limpiar formulario
        
        context['form'] = form  

    return render(request, 'parameters.html', context)