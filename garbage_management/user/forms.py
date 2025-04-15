from django import forms 
from .models import Users, DistrictChoices

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['uuid', 'active_status', 'profile']

        input_style = 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-input'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter full name',
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
            'post_office': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter the psot office',
                'required': 'required'
            }),
            'pin_code': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter pincode',
                'required': 'required'
            }),
        }

    district = forms.ChoiceField(
        choices=DistrictChoices.choices,
        widget=forms.Select(attrs={
            'class': 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-select',
            'required': 'required'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        pin_code = cleaned_data.get('pin_code')

        if pin_code and len(pin_code) < 6:
            self.add_error('pin_code', 'Pincode must be six digits')

        return cleaned_data
