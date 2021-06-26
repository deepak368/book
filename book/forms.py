from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import addbookmodel,order_model


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    class Meta:
        model=User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'username': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.TextInput(attrs={'class': 'input'}),

        }
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'input'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'input'}))


class AddbookForm(ModelForm):
    class Meta:
        model=addbookmodel
        fields = "__all__"
        widgets = {
            'Book_name': forms.TextInput(attrs={'class': 'input'}),
            'Author': forms.TextInput(attrs={'class': 'input'}),
            'Price': forms.TextInput(attrs={'class': 'input'}),

        }
class OrderForm(ModelForm):
    class Meta:
        model=order_model
        fields="__all__"
