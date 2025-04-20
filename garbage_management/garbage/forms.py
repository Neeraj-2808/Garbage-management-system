from django import forms 
from .models import Garbage,WasteChoices,Status_Choices

class GarbageRegisterForm(forms.ModelForm):
    class Meta:
        model = Garbage
        exclude = ['uuid', 'active_status','customer','status']

        input_style = 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-input'

        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': input_style,
                'placeholder': 'Enter the quantity in kg',
                'required': 'required'
            }),
            'pick_up_date': forms.DateInput(attrs={
                'type':'date',
                'class': input_style,
                'required': 'required'
            }),
            'address': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter the address',
                'required': 'required'
            }),
        }

    garbage_type = forms.ChoiceField(
        choices=WasteChoices.choices,
        widget=forms.Select(attrs={
            'class': 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-select',
            'required': 'required'
        })
    )
    # status = forms.ChoiceField(
    #     choices=Status_Choices.choices,
    #     widget=forms.Select(attrs={
    #         'class': 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-select',
    #         'required': 'required'
    #     })
    # )
