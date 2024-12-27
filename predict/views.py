from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ParametersForm, PrediccionForm

numeros_jugados = []  # Lista global para almacenar números
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
parametros = {
    'type_roulette': '',
    'limit_game': 0,
    'neighbors': 0,
    'probability': 0.0,
}

def realizar_prediccion(numero, parametros):
    # Simulación de la lógica de predicción
    if numero in black_numbers:
        return "black"
    elif numero in red_numbers:
        return "red"
    else:
        return "unknown"

def obtener_estadisticas_juego():
    # Simulación de la obtención de estadísticas del juego
    total_jugados = len(numeros_jugados)
    total_negros = sum(1 for n in numeros_jugados if n in black_numbers)
    total_rojos = sum(1 for n in numeros_jugados if n in red_numbers)
    return {
        'total_jugados': total_jugados,
        'total_negros': total_negros,
        'total_rojos': total_rojos,
    }

def game_view(request):
    # Obtener parámetros almacenados, por ejemplo desde la sesión
    parametros = request.session.get('parametros', None)
    
    if not parametros:
        return redirect('parameters')  # Redirigir si no hay parámetros configurados

    if request.method == 'POST':
        form = PrediccionForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data.get('action')
            numero = form.cleaned_data.get('username')
            if action == 'predict':
                # Procesar la predicción
                resultado = realizar_prediccion(numero, parametros)
                request.session['resultado'] = resultado
            elif action == 'delete':
                # Procesar la eliminación
                request.session.pop('numeros', None)
                request.session.pop('resultado', None)
            return redirect('predict:game')
    else:
        form = PrediccionForm()
    
    numeros = request.session.get('numeros', [])
    resultado = request.session.get('resultado', '')
    estadisticas = obtener_estadisticas_juego()

    context = {
        'form_prediccion': form,
        'numeros': numeros,
        'resultado': resultado,
        'estadisticas': estadisticas,
        'parametros': parametros,
        'black_numbers': black_numbers,  # Define esta función según tu lógica
    }
    return render(request, 'game.html', context)

def parameters_view(request):
    if request.method == 'POST':
        form = ParametersForm(request.POST)
        if form.is_valid():
            parametros = form.cleaned_data
            request.session['parametros'] = parametros
            messages.success(request, 'Parámetros guardados correctamente.')
            return redirect('predict:game')
        else:
            messages.error(request, 'Hubo un error al guardar los parámetros.')
    else:
        form = ParametersForm()
    
    context = {
        'form': form,
    }
    return render(request, 'parameters.html', context)

# def game(request):
#     form = PrediccionForm()
#     context = {
#         'numeros': numeros_jugados,
#         'resultado': '',
#         'form': form,
#         'black_numbers': black_numbers,
#         'red_numbers': red_numbers
#     }


#     if request.method == 'POST':
#         action = request.POST.get('action')
#         if action == 'predict':
#             form = PrediccionForm(request.POST)
#             if form.is_valid():
#                 numero = form.cleaned_data['username']
#                 numeros_jugados.append(numero)  # Agregar número
#                 # Actualizar contexto de forma individual
#                 context['resultado'] = f"Ultimo número: {numero}"
#                 context['numeros'] = numeros_jugados
#                 context['form'] = PrediccionForm()
                
#         elif action == 'delete':
#             if numeros_jugados:  # Si hay números
#                 ultimo_numero = numeros_jugados.pop()  # Eliminar último
#                 # Actualizar contexto de forma individual
#                 context['resultado'] = f"Número {ultimo_numero} borrado."
#                 context['numeros'] = numeros_jugados
    
#     # context['numeros'] = numeros_jugados  # Siempre incluir números en contexto
#     return render(request, 'game.html', context)


# def parameters(request):
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