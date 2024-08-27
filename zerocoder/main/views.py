from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def new2(request):
    return HttpResponse("<h1>Это 2-я страница проекта на Django</h1>")

def new3(request):
    return HttpResponse("<h1>Это третья страница проекта на Django</h1>")