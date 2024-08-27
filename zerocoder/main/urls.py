from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('new_2', views.new_2),
    path('new3', views.new3),
]