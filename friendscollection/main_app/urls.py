from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('friends/', views.index, name='index'),
    path('friends/<int:friend_id>/', views.details, name='details'),
    path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
    path('friends/<int:pk>/update/', views.FriendUpdate.as_view(), name='friends_update'),
    path('friends/<int:pk>/delete/', views.FriendDelete.as_view(), name='friends_delete'),
    path('friends/<int:friend_id>/give_booze/', views.give_booze, name='give_booze')
]