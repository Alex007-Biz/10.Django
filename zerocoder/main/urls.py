from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new,  name='page2'),
    path('new2', views.new2, name='page3')
]