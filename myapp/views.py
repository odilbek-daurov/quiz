
from django.shortcuts import render, redirect
from .models import Topic, Answer, Questions, Result
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from random import shuffle
from .forms import RegisterForm


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('topic')
    form = RegisterForm()

    return render(request, 'login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('topic')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def topic(request):
    topics = Topic.objects.all()
    context = {
        'topics': topics,
    }

    return render(request, 'home.html', context)


def questions(request, slug):
    topic = Topic.objects.get(slug=slug)
    question = Questions.objects.filter(topic=topic)
    ansver = list(Answer.objects.all())
    shuffle(ansver)
    if request.method == 'POST':
        correct = 0
        wrong = 0
        for q in question:
            if request.POST.get(q.name) == 'True':
                correct += 1
            else:
                wrong += 1

        Result.objects.create(
            user=request.user,
            correct=correct,
            topic=topic,
            total_question=len(question),

        )

        context = {
            'user': request.user.username,
            'correct': correct,

        }
        return render(request, 'result_list.html', context)

    context = {
        'question': question,
        'ansver': ansver,
    }

    return render(request, 'quiz.html', context)


def result(request):
    results = Result.objects.all()
    return render(request, 'result.html', {'result': results})
