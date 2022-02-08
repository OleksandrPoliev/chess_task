from django.contrib import admin
from django.urls import path,include
from .views import index,start
urlpatterns = [
    path('',start),
    path('<str:figure>/<str:fild>', index)
]
