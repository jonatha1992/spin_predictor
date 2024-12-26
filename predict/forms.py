from django import forms

class PrediccionForm(forms.Form):
    username = forms.IntegerField(
        label='Número',
        min_value=0,
        max_value=36,
        required=False,  # Permitir que sea opcional inicialmente
        error_messages={
            'min_value': 'El número debe ser mayor o igual a 0',
            'max_value': 'El número debe ser menor o igual a 36',
            'invalid': 'Por favor ingrese un número válido',
            'required': 'Este campo es requerido para predecir'
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'id': 'username',
                'min': '0',
                'max': '36',
                'placeholder': 'Ingrese un número entre 0 y 36',
                'autofocus': True  # Agregar autofocus
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        action = self.data.get('action')
        
        # Solo validar si es acción predecir
        if action == 'predict':
            numero = cleaned_data.get('username')
            if numero is None:
                raise forms.ValidationError('Debe ingresar un número para predecir')
        return cleaned_data




class ParametersForm(forms.Form):
    ROULETTE_CHOICES = [
        ('', 'Seleccione un tipo de ruleta'),  # Placeholder
        ('Crupier', 'Crupier'),
        ('Electromecanica', 'Electromecanica'),
        ('Electronica', 'Electronica'),
    ]

    type_roulette = forms.ChoiceField(
        label='Tipo de Ruleta',
        choices=ROULETTE_CHOICES,
        required=True,
        error_messages={
            'required': 'Debe seleccionar un tipo de ruleta',
            'invalid_choice': 'Seleccione una opción válida'
        },
        widget=forms.Select(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'id': 'type_roulette',
            }
        )
    )

    limite_games = forms.IntegerField(
        label='Límite de juegos',
        min_value=1,  # Consistente con el widget
        max_value=10,  # Consistente con el widget
        required=True,
        error_messages={
            'min_value': 'El número debe ser mayor o igual a 1',
            'max_value': 'El número debe ser menor o igual a 10',
            'invalid': 'Por favor ingrese un número válido',
            'required': 'Este campo es requerido para predecir'
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'id': 'limite_games',
                'min': '1',  # Ajustado al rango correcto
                'max': '10',  # Ajustado al rango correcto
                'placeholder': 'Ingrese un número entre 1 y 10',
            }
        ),
    )
    
    neighbors = forms.IntegerField(
        label='Cantidad de vecinos',
        min_value= 0,  # Consistente con el widget
        max_value= 3,  # Consistente con el widget
        required=True,
        error_messages={
            'min_value': 'El número debe ser mayor o igual a 0',
            'max_value': 'El número debe ser menor o igual a 3',
            'invalid': 'Por favor ingrese un número válido',
            'required': 'Este campo es requerido para predecir'
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'id': 'neighbors',
                'min': '0',  # Ajustado al rango correcto
                'max': '4',  # Ajustado al rango correcto
                'placeholder': 'Ingrese un número entre 0 y 3',
            }
        )
    )
    probability = forms.IntegerField(
        label='Umbral de probabilidad',
        min_value= 10,  # Consistente con el widget
        max_value= 100,  # Consistente con el widget
        required=True,
        initial=50,  # Valor por defecto
        error_messages={
            'min_value': 'El número debe ser mayor o igual a 10',
            'max_value': 'El número debe ser menor o igual a 100',
            'invalid': 'Por favor ingrese un número válido',
            'required': 'Este campo es requerido para predecir',
            
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'id': 'probability',
                'min': '1',  # Ajustado al rango correcto
                'max': '100',  # Ajustado al rango correcto
                'placeholder': 'Ingrese un número entre 10 y 100',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        type_roulette = cleaned_data.get('type_roulette')
        limite_games = cleaned_data.get('limite_games')
        probability = cleaned_data.get('probability')
        neighbors = cleaned_data.get('neighbors')

        # Validar que no se seleccione el placeholder
        if type_roulette == '':
            raise forms.ValidationError({'type_roulette': 'Debe seleccionar un tipo de ruleta válido.'})
        if limite_games == '':
            raise forms.ValidationError({'limite_games': 'Debe colocar el límite de juegos.'})
        if probability == '':
            raise forms.ValidationError({'probability': 'Debe colocar el umbral de probabilidad.'})
        if neighbors == '':
            raise forms.ValidationError({'neighbors': 'Debe colocar la cantidad de vecinos.'})

        # Validaciones adicionales para otras acciones
        action = self.data.get('action')
        if action == 'iniciar' and not type_roulette:
            raise forms.ValidationError('Debe seleccionar un tipo de ruleta.')

        return cleaned_data
