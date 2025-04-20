from django import forms 
from .models import Recipe

class RecipeRegisterForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['uuid', 'active_status']

        input_style = 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-input'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'tile',
                'required': 'required'
            }),
            
            'description': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'description',
                'required': 'required'
            }),
            'ingredients': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'full address',
                'required': 'required'
            }),
            'photo' :forms.FileInput(attrs={'class': input_style,
                                                        }),
          
        }

