from django.urls import path,include
from django.contrib import admin
from home import views

urlpatterns = [
    path('', views.index),
    path('delete/<str:city>', views.delete),
]
