from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hot(request):
    return render(request, 'hot.html')

def settings(request):
    return render(request, 'settings.html')

def question(request):
    return render(request, 'question.html')

def login(request):
    return render(request, 'login.html')

def ask(request):
    return render(request, 'ask.html')