from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('new_2', views.index),
    path('new3', views.index),
]