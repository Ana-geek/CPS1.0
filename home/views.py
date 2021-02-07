from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def index(request):  # Главная страница
    return render(request, 'home/index.html')


def blog(request):  # Блог
    return render(request, 'home/blog.html')


def qa(request):  # Вопросы и ответы
    return render(request, 'home/qa.html')


def cab(request):   # Личный кабинет
    return render(request, 'home/cab.html')


def cabinet(request):   # Вход в Личный кабинет
    return render(request, 'cabinet/cabinet.html')


def sign_in(request):  # Вход в свой кабинет
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/cabinet")
        return render(request, 'home/cab.html')
    elif request.method == "POST":
        data = {}

        _login = request.POST.get('login_field')
        _password = request.POST.get('password_field')

        user = authenticate(request, username=_login, password=_password)
        if user is None:
            data['report'] = 'User is not found or wrong password!'
            return render(request, 'home/cab.html', context=data)
        else:
            login(request, user)
            return redirect("/cabinet")


def logout_user(request):   # Выход из кабинета
    logout(request)
    return redirect("/")


def register(request):  # Регистрация
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, 'home/register.html', context={})
    elif request.method == "POST":
        login = request.POST.get('login_field')
        email = request.POST.get('email_field')
        pass1 = request.POST.get('password_field')
        pass2 = request.POST.get('password_confirm_field')

        data = dict()
        data['login'] = login
        data['email'] = email
        data['pass1'] = pass1
        data['pass2'] = pass2

        if pass1 != pass2:
            report = 'Passwords dont match'
        elif '' in data.values():
            report = 'All fields are obligated'
        elif len(pass1) < 8:
            report = 'Password too short'
        else:
            user = User.objects.create_user(login, email, pass1)
            user.save()
            if user:
                return redirect("/")
        report = 'ERROR'
        data['report'] = report
        return render(request, 'home/register.html', context=data)


def ops(request):  # Страница на все случаи жизни
    return render(request, 'cabinet/ops.html')


def presentation(request):
    return render(request, 'home/presentation.html')
