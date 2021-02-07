from django.shortcuts import render


def cabinet(request):   # Личный кабинет
    return render(request, 'cabinet/cabinet.html')


def homework(request):
    return render(request, 'cabinet/homework.html')


def my_account(request):
    pass
