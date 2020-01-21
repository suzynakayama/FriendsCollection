from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('friends/', views.index, name='index'),
    path('friends/<int:friend_id>/', views.details, name='details'),
]