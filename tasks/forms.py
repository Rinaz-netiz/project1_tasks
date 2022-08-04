from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'log-in-username'}))
    password = forms.CharField(max_length=80, widget=forms.PasswordInput(attrs={'autocomplete': 'off', 'class': 'log-in-password'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'username-input', 'autocomplete': 'off'}))
    password1 = forms.CharField(max_length=80, widget=forms.PasswordInput(attrs={'autocomplete': 'off', 'class': 'register-password1'}))
    password2 = forms.CharField(max_length=80, widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))


class TaskDid(forms.Form):
    class Meta:
        model = Task
        fields = ('done', )


class NewTask(forms.Form):
    task = forms.CharField(label='Task', widget=forms.TextInput(attrs={'class': 'text-input', 'autocomplete': 'off'}))
    date_add = forms.DateTimeField(label='Date', widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'date-class', 'autocomplete': 'off'}))
    money = forms.IntegerField(label='How much money', widget=forms.NumberInput(attrs={'class': 'money-class', 'autocomplete': 'off'}))


class BuyMarket(forms.Form):
    buy = forms.BooleanField()


class AddMarket(forms.Form):
    text = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'market-add-text-input', 'autocomplete': 'off'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'market-add-price-input', 'autocomplete': 'off'}))


#class MarketAddProduct(forms.Form):
    # text = forms.CharField(label='Text', widget=forms.TextInput())
    # price = forms.IntegerField(label='price', widget=forms.NumberInput())
