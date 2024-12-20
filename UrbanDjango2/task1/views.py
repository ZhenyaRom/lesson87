from django.shortcuts import render
from .forms import UserRegister
from .models import *


def store_func(request):
    title = 'Товары'
    name = 'Магазин'
    plays = Game.objects.all()
    context = {
        'title': title,
        'name': name,
        'plays': plays
    }
    return render(request, 'store_page.html', context)


def basket_func(request):
    title = 'Корзина'
    name = 'Корзина'
    products = []
    context = {
        'title': title,
        'name': name,
        'products': products
    }
    return render(request, 'basket_page.html', context)


def main_func(request):
    title = 'Игровая платформа'
    name = 'Главная'
    context = {
        'title': title,
        'name': name,
    }
    return render(request, 'main_page.html', context)


def sign_up_by_django(request):
    info = {'error': ''}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            age = form.cleaned_data['age']
            if password != password_again:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)
            try:
                if int(age) < 1:
                    info['error'] = 'Возраст введен некорректно'
                    return render(request, 'registration_page.html', info)
                else:
                    users = Buyer.objects.all()
                    for user in users:
                        if user.name == username:
                            info['error'] = 'Пользователь уже существует'
                            return render(request, 'registration_page.html', info)
                Buyer.objects.create(name=username, password=password, age=age)
                info['hi'] = f'Приветствуем, {username}!'
            except ValueError:
                info['error'] = 'Возраст введите арабскими цифрами'
                return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
        info['form'] = form
    return render(request, 'registration_page.html', info)


# python manage.py runserver
