from django.contrib import admin
from django.urls import path
from .views import questions, topic, login_view, result, logout_view, signup

urlpatterns = [
    path('', topic, name='topic'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('test/<slug:slug>', questions, name = 'question'),
    path('results/', result, name='result')
]