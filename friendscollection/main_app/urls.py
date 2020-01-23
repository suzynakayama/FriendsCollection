from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('friends/', views.index, name='index'),
    path('friends/<int:friend_id>/', views.details, name='details'),
    path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
    path('friends/<int:pk>/update/', views.FriendUpdate.as_view(), name='friends_update'),
    path('friends/<int:pk>/delete/', views.FriendDelete.as_view(), name='friends_delete'),
    path('friends/<int:friend_id>/give_booze/', views.give_booze, name='give_booze'),
    path('friends/<int:friend_id>/assoc_interest/<int:interest_id>/', views.assoc_interest, name='assoc_interest'),
    path('friends/<int:friend_id>/dissoc_interest/<int:interest_id>/', views.dissoc_interest, name='dissoc_interest'),
    path('friends/<int:friend_id>/add_photo/', views.add_photo, name='add_photo'),
    path('interests/', views.InterestList.as_view(), name='interests_index'),
    path('interests/<int:pk>/', views.InterestDetail.as_view(), name='interests_detail'),
    path('interests/create/', views.InterestCreate.as_view(), name='interests_create'),
    path('interests/<int:pk>/update/', views.InterestUpdate.as_view(), name='interests_update'),
    path('interests/<int:pk>/delete', views.InterestDelete.as_view(), name='interests_delete'),
]