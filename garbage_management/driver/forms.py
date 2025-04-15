from django import forms 
from .models import Driver

class DriverRegisterForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['uuid', 'active_status', 'profile']

        input_style = 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-input'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter full name',
                'required': 'required'
            }),

            'license_number': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter the psot office',
                'required': 'required'

            }),

            'email': forms.EmailInput(attrs={
                'class': input_style,
                'placeholder': 'Enter mail'
            }),
            'contact': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter contact number',
                'required': 'required'
            }),
            'address': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'full address',
                'required': 'required'
            }),
            
        }


