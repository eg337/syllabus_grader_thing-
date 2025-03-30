from django.contrib import admin
from django.urls import path
from .views import index
from .views import Create_Grade_Calc_View



urlpatterns = [
    path('', index),
    path('create-grade-calc/', Create_Grade_Calc_View.as_view()),
]