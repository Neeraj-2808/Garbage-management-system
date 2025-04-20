from django import forms 
from .models import Complaint
from driver.models import Driver

class ComplaintRegisterForm(forms.ModelForm):
    class Meta:
        model = Complaint
        exclude = ['uuid', 'profile','customer']

        input_style = 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-input'

        widgets = {
            'title': forms.TextInput(attrs={ 
                'class': input_style,
                'placeholder': 'Enter the subject',
                'required': 'required'
            }),

            'description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 40,
                'class': input_style,
                'placeholder': 'Describe the issue in detail',
                'required': 'required'
            }),

            'suggestion': forms.Textarea(attrs={
                'rows': 3,
                'cols': 40,
                'class': input_style,
                'placeholder': 'Give your suggestion for improvement',
            }),
        }
