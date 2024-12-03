from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    user_balance = forms.CharField(max_length=10, label='Введите баланс')
    age = forms.CharField(max_length=3, label='Введите свой возраст')


