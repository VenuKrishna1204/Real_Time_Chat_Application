****Real-Time Django Channels Chat Application****

This is a real-time chat application built with Django Channels, enabling users to:

	✅ Register and login.
	
	✅ Add friends to chat with.
	
	✅ See friends' online/offline status.
	
	✅ Chat in real-time (WebSocket) with unread message counts.


 **1. Project Objective**

**Build a Real-Time Chat Application using Django Channels where:**
    
    ✅Users register/login.
    
    ✅Users add friends to chat with.
    
    ✅Users see friends' online/offline status.
    
    ✅Users chat in real-time (WebSocket) with unread message count.

** 2. Final Project Structure**

![image](https://github.com/user-attachments/assets/6a8adb1f-ddd2-402b-a084-82b221430afd)


![image](https://github.com/user-attachments/assets/4c5743c7-c359-41ab-9c3e-a155941d6387)


**3. Step-by-Step Execution**

**🔷 Step 1: Navigations**

	✅PS D:\> cd .\DJANGO\
	
	✅PS D:\DJANGO> cd .\VENU\
	
	✅PS D:\DJANGO\VENU> cd .\Projects\
	
	✅PS D:\DJANGO\VENU\Projects> cd .\django_channels_chat\
	
	✅PS D:\DJANGO\VENU\Projects\django_channels_chat> ls
	
	
		Directory: D:\DJANGO\VENU\Projects\django_channels_chat
	
	
	Mode                 LastWriteTime         Length Name
	----                 -------------         ------ ----
	d-----        02-07-2025     15:50                chat_app
	d-----        02-07-2025     15:28                django_channels_chat
	-a----        02-07-2025     19:57         176128 db.sqlite3
	-a----        02-07-2025     15:27            698 manage.py
	

**🔷 Step 2: Create Project & App**

	django-admin startproject django_channels_chat
	cd django_channels_chat
	python manage.py startapp chat_app


**🔷 Step 3: Install Requirements**

	In terminal:
	pip install django channels  or pip install -r requirements.txt
 
**🔷 Step 4: Update settings.py**

		**Add to INSTALLED_APPS:**
		
		✅INSTALLED_APPS = [
		    ...,
		    'channels',
		    'chat_app',
		]
  
		**Add ASGI application:**
  
	✅ASGI_APPLICATION = 'django_channels_chat.asgi.application'
	(Optional) For production:

	CHANNEL_LAYERS = {
	    "default": {
	        "BACKEND": 
	        },
	    },
	}

 
**🔷 Step 5: Setup Models in chat_app/models.py**
	✅Define models:
	
	✅ChatSession: stores user pairs.
	
	✅ChatMessage: stores each message with timestamp, read status.
	
	✅Uses Django’s User model.

**🔷 Step 6: Migrations**

	✅python manage.py makemigrations
		No changes detected
 
	✅python manage.py migrate

	Operations to perform:
	  Apply all migrations: admin, auth, chat_app, contenttypes, sessions
	Running migrations:
	  No migrations to apply.

 **🔷 Step 7: Create Superuser**

	✅python manage.py createsuperuser
 
 	**output**
	Username (leave blank to use 'badbo'): venu
	Error: That username is already taken.
	Username (leave blank to use 'badbo'): aiml
	Email address: gaddamvenu12042004@gmail.com
	Password: 
	Password (again):
	This password is too short. It must contain at least 8 characters.
	This password is too common.
	Bypass password validation and create user anyway? [y/N]: y
	Superuser created successfully.


**🔷 Step 8: Configure urls.py**

**🔷 Step 9: Configure ASGI for Channels**

**🔷 Step 10: Setup chat_app/routing.py**

**🔷 Step 11: Create consumers.py**

	✅Handles WebSocket connections, sends/receives real-time messages.

**🔷 Step 12: Create Templates**

	✅In chat_app/templates/chat/:
	
	✅base.html – common layout
	
	✅home.html – app information, links to add friends & chat list
	
	✅create_friend.html – displays all users to add as friends
	
	✅friend_list.html – shows friends list with online status & unread count
	
	✅start_chat.html – actual chat room page

**🔷 Step 13: Static Files**

	✅Add any CSS/JS to chat_app/static/ and link in templates.

**🔷 Step 14: Run Server**

	✅python manage.py runserver
	Open:
 
	Watching for file changes with StatReloader
	Performing system checks...
	
	System check identified no issues (0 silenced).
	July 03, 2025 - 09:20:40
	Django version 5.1.6, using settings 'django_channels_chat.settings'
	Starting ASGI/Daphne version 4.2.0 development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.

**🔷 Step 15: Test Real-Time Chat**

	✅Login as User1 in Chrome.
	
	✅Login as User2 in Firefox or Incognito.
	
	✅Add each other as friends.
	
	✅Start chat and test real-time message updates.

**output:**

	user1:
 ![outpu1](https://github.com/user-attachments/assets/5a7ee8c5-5167-45bd-8e80-287e711ad662)

 login

 ![output2](https://github.com/user-attachments/assets/0274a4db-2c78-4aea-b140-70a1a3409e95)

 create friend list

 ![output5](https://github.com/user-attachments/assets/51d8166e-e246-4e04-a47f-495af8f00931)

added frined list

![6](https://github.com/user-attachments/assets/ee613dff-06be-48ab-a206-12aeb46932a0)

chat 

![9](https://github.com/user-attachments/assets/722c1fa0-211d-4ed6-ae43-db82bf087773)

![10](https://github.com/user-attachments/assets/f8790c93-d357-448d-a70f-16a6d704f0aa)

my chat list

![13](https://github.com/user-attachments/assets/2155c5e7-a474-44f1-ba23-e7848925ed63)


 user2

 ![output3](https://github.com/user-attachments/assets/183c91cc-80dd-48a3-9826-35cd2b5c2a7f)

 create friend list

 ![output4](https://github.com/user-attachments/assets/aed81e31-0271-4b6c-9bcd-52ec9a0e7cce)

 added friend list

 ![7](https://github.com/user-attachments/assets/0531dd09-667c-4765-96a5-6d18f2b74689)

 chat

 ![8](https://github.com/user-attachments/assets/164ebc3e-c693-4197-b311-f068cfcc3c01)

![11](https://github.com/user-attachments/assets/bbe96ab4-d0af-4c9e-8ab8-3827265b9aa2)

my chat list

![12](https://github.com/user-attachments/assets/df10d542-9f3c-4675-a13e-ff799e1ad19d)



**Administation:**


![14](https://github.com/user-attachments/assets/4716f215-3d44-4bbc-a165-3698a69d1a8f)


delete chat messgaes

![15](https://github.com/user-attachments/assets/9f934635-314f-4ffe-a26f-daebb6962989)

![16](https://github.com/user-attachments/assets/8e8b7942-732a-4661-a153-1e3df34f288d)



**Credits**

	Built by Your Name as a part of learning Django Channels and WebSocket-based applications.

**License**
   
	This project is licensed under the MIT License - see the LICENSE file for details.




