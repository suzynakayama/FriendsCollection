from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to the Friends Collection page!</h1>')

def about(request):
    return render(request, 'about.html')

def index(request):
    friends = Friend.objects.all()
    return render(request, 'friends/index.html', {'friends': friends})

def details(request, friend_id):
    friend = Friend.objects.get(id=friend_id)
    return render(request, 'friends/details.html', {'friend': friend})