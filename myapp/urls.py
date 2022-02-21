from django.contrib import admin
from django.urls import path
from .views import questions, topic, login

urlpatterns = [
    path('', topic, name = 'topic' ),
    path('', login, name = 'login' ),
    path('test/<slug:slug>', questions, name = 'question' ),
]