from django.contrib import admin
from .models import Profile, ChatSession, ChatMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "is_online"]

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ["id", "user1", "user2", "updated_on"]

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "chat_session", "user", "message_detail"]

