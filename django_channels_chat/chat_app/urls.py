from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('home/', views.home, name='home_page'),  

    path('create_friend/', views.create_friend, name='create_friend'),
    path('friend_list/', views.friend_list, name='friend_list'),
    path('chat/<str:room_name>/', views.start_chat, name='start_chat'),
]
