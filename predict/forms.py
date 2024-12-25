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
            ('europea', 'Ruleta Europea'),
            ('americana', 'Ruleta Americana'),
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
            label='Limite de juegos',
            min_value=0,
            max_value=20,
            required=True,
            error_messages={
                'min_value': 'El número debe ser mayor o igual a 0',
                'max_value': 'El número debe ser menor o igual a 20',
                'invalid': 'Por favor ingrese un número válido',
                'required': 'Este campo es requerido para predecir'
            },
            widget=forms.NumberInput(
                attrs={
                    'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                    'id': 'limite_games',
                    'min': '0',
                    'max': '20',
                    'placeholder': 'Ingrese un número entre 0 y 20',
                }
            )
        )

        def clean(self):
            cleaned_data = super().clean()
            action = self.data.get('action')
            
            if action == 'iniciar' and not cleaned_data.get('type_roulette'):
                raise forms.ValidationError('Debe seleccionar un tipo de ruleta')
            
            return cleaned_data
