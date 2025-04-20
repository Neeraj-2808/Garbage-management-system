from django import forms 
from .models import GarbageTruck
from driver.models import Driver

class TruckRegisterForm(forms.ModelForm):
    class Meta:
        model = GarbageTruck
        exclude = ['uuid', 'profile']

        input_style = 'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-input'

        widgets = {
            'truck_number': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter the truck number',
                'required': 'required'
            }),

            'capacity': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter the maximum capcity',
                'required': 'required'

            }),
            'current_location': forms.TextInput(attrs={
                'class': input_style,
                'placeholder': 'Enter current location',
                'required': 'required'
            }),
            'active_status': forms.CheckboxInput(attrs={
    'class': 'h-5 w-5 text-green-600 accent-green-600 focus:ring-green-500 border-gray-300 rounded'

}),


        }

    driver = forms.ModelChoiceField(queryset=Driver.objects.all(),widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm text-gray-700 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-200 form-input'
}))
            
    


