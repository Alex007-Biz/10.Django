from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница проекта на Django</h1>")

def new_2(request):
    return HttpResponse("<h1>Это 3 страница проекта на Django</h1>")

def new3(request):
    return HttpResponse("<h1>Это ретья страница проекта на Django</h1>")