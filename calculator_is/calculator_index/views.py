from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'calculator_index/index.html', { 'title' : 'Главная страница'})

def result(request):
    return render(request, 'calculator_index/calculator_index/result.html',{ 'title' : 'Результат работы'})


