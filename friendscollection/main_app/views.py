from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Friend, Interest, Photo
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.amazonaws.com/'
BUCKET = 'friendscollection'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    friends = Friend.objects.all()
    return render(request, 'friends/index.html', {'friends': friends})

def details(request, friend_id):
    friend = Friend.objects.get(id=friend_id)
    interests_friend_doesnt_have = Interest.objects.exclude(id__in = friend.interests.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'friends/details.html', {'friend': friend, 'feeding_form': feeding_form, 'interests': interests_friend_doesnt_have})

class FriendCreate(CreateView):
    model = Friend
    fields = ['name', 'background', 'likes', 'age']

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

class InterestList(ListView):
    model = Interest

class InterestDetail(DetailView):
    model = Interest

class InterestCreate(CreateView):
    model = Interest
    fields = '__all__'

class InterestUpdate(UpdateView):
    model = Interest
    fields = '__all__'

class InterestDelete(DeleteView):
    model = Interest
    success_url = '/interests/'

def assoc_interest(request, friend_id, interest_id):
    Friend.objects.get(id=friend_id).interests.add(interest_id)
    return redirect('details', friend_id=friend_id)

def dissoc_interest(request, friend_id, interest_id):
    Friend.objects.get(id=friend_id).interests.remove(interest_id)
    return redirect('details', friend_id=friend_id)

def add_photo(request, friend_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        session = boto3.Session(profile_name='friends')
        s3 = session.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.') :]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, friend_id=friend_id)
            photo.save()
        except:
            print('Oooops! Something went wrong.')
    return redirect('details', friend_id=friend_id)
