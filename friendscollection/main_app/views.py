from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Friend
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'friends/details.html', {'friend': friend, 'feeding_form': feeding_form})

class FriendCreate(CreateView):
    model = Friend
    fields = '__all__'

class FriendUpdate(UpdateView):
    model = Friend
    fields = ['background', 'likes', 'age']

class FriendDelete(DeleteView):
    model = Friend
    success_url = '/friends/'

def give_booze(request, friend_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.friend_id = friend_id
        new_feeding.save()
    return redirect('details', friend_id=friend_id)