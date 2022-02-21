from ast import Pass
from django.shortcuts import render, redirect
from .models import Topic, Answer, Questions, Result
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from random import  shuffle

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get()
            login(request, user)
            return redirect('blog_list')
    
    return render(request, 'login.html')

def topic(request):
    topic = Topic.objects.all()
    context = {
        'topic':topic
    }
    
    return render(request, 'home.html', context)


def questions(request, slug):
    topic = Topic.objects.get(slug = slug)
    question = Questions.objects.filter(topic = topic)
    ansver = list(Answer.objects.all())
     
    if request.method == 'POST':
        Result.objects.create(
            user = request.user
            
        )
         
    
    shuffle(ansver)
    context = {
        'question':question,
        'ansver':ansver,
    }
    
    return render(request, 'quiz.html', context)


