![image](https://github.com/user-attachments/assets/8e6cebf5-d756-4fd0-9463-ec72bff359c0)# Real_Time_Chat_Application

✅ 1. Project Objective
Build a Real-Time Chat Application using Django Channels where:

Users register/login.

Users add friends to chat with.

Users see friends' online/offline status.

Users chat in real-time (WebSocket) with unread message count.

✅ 2. Final Project Structure
![image](https://github.com/user-attachments/assets/6a8adb1f-ddd2-402b-a084-82b221430afd)
![image](https://github.com/user-attachments/assets/4c5743c7-c359-41ab-9c3e-a155941d6387)
✅ 3. Step-by-Step Execution
🔷 Step 1: Create Project & App
bash
Copy
Edit
django-admin startproject django_channels_chat
cd django_channels_chat
python manage.py startapp chat_app
🔷 Step 2: Install Requirements
In terminal:

bash
Copy
Edit
pip install django channels
🔷 Step 3: Update settings.py
Add to INSTALLED_APPS:

python
Copy
Edit
INSTALLED_APPS = [
    ...,
    'channels',
    'chat_app',
]
Add ASGI application:

python
Copy
Edit
ASGI_APPLICATION = 'django_channels_chat.asgi.application'
(Optional) For production:

python
Copy
Edit
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
🔷 Step 4: Setup Models in chat_app/models.py
Define models:

ChatSession: stores user pairs.

ChatMessage: stores each message with timestamp, read status.

Uses Django’s User model.

🔷 Step 5: Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
🔷 Step 6: Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
🔷 Step 7: Configure urls.py
In django_channels_chat/urls.py:
python
Copy
Edit
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat_app.urls')),
]
In chat_app/urls.py:
python
Copy
Edit
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_friend/', views.create_friend, name='create_friend'),
    path('friend_list/', views.friend_list, name='friend_list'),
    path('chat/<str:room_name>/', views.start_chat, name='start_chat'),
]
🔷 Step 8: Configure ASGI for Channels
In django_channels_chat/asgi.py:
python
Copy
Edit
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channels_chat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_app.routing.websocket_urlpatterns
        )
    ),
})
🔷 Step 9: Setup chat_app/routing.py
python
Copy
Edit
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
🔷 Step 10: Create consumers.py
Handles WebSocket connections, sends/receives real-time messages.

🔷 Step 11: Create Templates
In chat_app/templates/chat/:

base.html – common layout

home.html – app information, links to add friends & chat list

create_friend.html – displays all users to add as friends

friend_list.html – shows friends list with online status & unread count

start_chat.html – actual chat room page

🔷 Step 12: Static Files
Add any CSS/JS to chat_app/static/ and link in templates.

🔷 Step 13: Run Server
bash
Copy
Edit
python manage.py runserver
Open:

http://127.0.0.1:8000/

🔷 Step 14: Test Real-Time Chat
Login as User1 in Chrome.

Login as User2 in Firefox or Incognito.

Add each other as friends.

Start chat and test real-time message updates.


