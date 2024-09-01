from django.shortcuts import render
from .models import News_post

# Create your views here.
from django.http import HttpResponse

def index(request):
    # data = {
    #     'caption':"CatDjango"
    # }
    news = News_post.objects.all()
    return render(request, 'main/index.html',{'news': news})

def new(request):
    return render(request, 'main/new.html')

def new2(request):
    return HttpResponse("<h1>Это 22-я страница проекта на Django</h1>")

def new3(request):
    return HttpResponse("<h1>Это третья страница проекта на Django</h1>")

def create_news(request):
    return render(request, 'main/add_new_post.html')