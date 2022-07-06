from django.contrib import admin
from django.urls import path , include 

from .views import inicioApp , Familia

urlpatterns = [
       path('',inicioApp),
       path('Familia/',Familia),
]