from django import forms

class PrediccionForm(forms.Form):
    username = forms.IntegerField(
        label='Número',
        min_value=0,
        max_value=36,
        error_messages={
            'min_value': 'El número debe ser mayor o igual a 0',
            'max_value': 'El número debe ser menor o igual a 100',
            'required': 'Este campo es requerido',
            'invalid': 'Por favor ingrese un número válido'
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'required': True,
                'id': 'username',
                'min': '0',  # Agregar min para HTML5 validation
                'max': '36'  # Agregar max para HTML5 validation
            }
        )
    )


    
