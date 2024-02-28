from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context: dict = {
        'title': 'Home',
        'content': 'Главная страница сайта - Home'

    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
