from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

# retorna um html
def index(request):
    return HttpResponse('<h1>Receitas</h1>')
