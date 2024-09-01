from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

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
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            errors = "Данные были заполнены некорректно"

    form = News_postForm()
    return render(request, 'main/add_new_post.html', {'form' : form, 'errors': error})
