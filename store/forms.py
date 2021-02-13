from django import forms
from .models.customer import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Asma'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Begum'}),
            'phone_no' : forms.TextInput(attrs={'class':'form-control', 'placeholder': '017234*****'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'example@gmail.com'}),
            'password' : forms.TextInput(attrs={'class':'form-control', 'placeholder': '*******'}),
        }