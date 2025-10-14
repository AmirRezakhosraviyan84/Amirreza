from django.contrib.auth.forms import  UserCreationForm,UserChangeForm
from . models import CustomUser, Doctor_register
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

import re

User = get_user_model()

from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'full_name', 'is_doctor', 'is_patient')
    


       
class CustomUserChangeForm(UserChangeForm):       

    class Meta:
       model = CustomUser
       fields = ('phone_number', 'full_name', 'is_doctor', 'is_patient')




class DoctorForm(forms.ModelForm):
    class Meta:
        model =Doctor_register
        fields = '__all__'
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'specialties': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


User = get_user_model()
class RegisterForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number =PhoneNumberField()

    class Meta:

        model =User
        fields =['password','phone_number']





class PhoneForm(forms.Form):
      phone_number = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره موبایل'}),
        error_messages={'invalid': 'لطفا شماره موبایل معتبر وارد کنید.'}
    )

      def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        pattern = r'^(\+98|0)?9\d{9}$'  # الگوی شماره موبایل ایران
        if not re.match(pattern, phone):
            raise forms.ValidationError("شماره موبایل معتبر نیست.")
        return phone




class profile_form(forms.ModelForm):

    class Meta:
        model =CustomUser

        fields =['first_name', 'last_name', 'national_code', 
            'birth_year', 'is_foreign', 'gender', 'city', 'email']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'national_code': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class WalletTopUpForm(forms.Form):
    amount = forms.DecimalField(label="مقدار شارژ (تومان)", min_value=50000, decimal_places=2)        