


from enum import unique
from unicodedata import name
from django import forms
from .models import registration
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

phoneValid = RegexValidator(regex=r'[6-9]{1}[0-9]{9}', message="Phone number must be 10 Digits")    
emailValid = RegexValidator(regex = r'^[0-9a-zA-Z]+[.+-_]{0,1}[A-Za-z0-9]+[@][a-zA-Z]+[.][a-zA-Z]{2,3}$',message="must contain @") 
passwordValid = RegexValidator(regex=r'[A-Z]{1}[.-/!@#$%^&*]{0,1}[0-9a-zA-Z]+',message="Must contain 1 upper case letter & 1 special character,Min 6 & max 15 characters")
usernameValid = RegexValidator(regex=r'[A-Za-z]',message="must contain alphabets only")


class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),required=True,validators=[usernameValid])
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone number must be 10 Digits'}),validators=[phoneValid],min_length=10)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Valid Email Address'}),validators=[emailValid])
    password = forms.CharField(validators=[passwordValid],label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),min_length=6,max_length=15,required=True)

    class Meta:
        model = registration
        fields = ['name','contact','email','password']
    

 


class LoginForm(forms.Form):
   username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),validators=[usernameValid])
   password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),validators=[passwordValid])
