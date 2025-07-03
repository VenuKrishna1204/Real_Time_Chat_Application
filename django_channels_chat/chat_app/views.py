from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

from .models import ChatMessage, ChatSession, User

def home(request):
    """
    Home page showing overall unread messages count.
    """
    unread_msg = ChatMessage.count_overall_unread_msg(request.user.id) if request.user.is_authenticated else 0
    return render(request, 'chat/home.html', {"unread_msg": unread_msg})

@login_required
def create_friend(request):
    user_1 = request.user
    if request.GET.get('id'):
        user2_id = request.GET.get('id')
        user_2 = get_object_or_404(User, id=user2_id)
        get_create = ChatSession.create_if_not_exists(user_1, user_2)
        if get_create:
            messages.success(request, f'{user_2.username} successfully added to your chat list!')
        else:
            messages.info(request, f'{user_2.username} is already in your chat list!')
        return HttpResponseRedirect('/create_friend')
    else:
        user_all_friends = ChatSession.objects.filter(Q(user1=user_1) | Q(user2=user_1))
        user_list = []
        for ch_session in user_all_friends:
            user_list.extend([ch_session.user1.id, ch_session.user2.id])
        
        # suggested friends excluding existing friends + self
        suggested_users = User.objects.exclude(Q(id__in=set(user_list)) | Q(id=user_1.id))
        
        # get existing friends for display
        friends_data = []
        for ch_session in user_all_friends:
            friend = ch_session.user2 if ch_session.user1 == user_1 else ch_session.user1
            friends_data.append({
                "username": friend.username,
                "room_name": ch_session.room_group_name,
            })
        
        context = {
            'all_user': suggested_users,
            'friends_data': friends_data,
        }
        return render(request, 'chat/create_friend.html', context)
@login_required
def friend_list(request):
    """
    Displays list of friends with unread messages count and online status.
    """
    current_user = request.user
    chat_sessions = ChatSession.objects.filter(Q(user1=current_user) | Q(user2=current_user)).select_related('user1', 'user2').order_by('-updated_on')

    all_friends = []
    for session in chat_sessions:
        friend = session.user2 if session.user1 == current_user else session.user1

        unread_count = ChatMessage.objects.filter(
            chat_session=session.id,
            message_detail__read=False
        ).exclude(user=current_user).count()

        data = {
            "user_name": friend.username,
            "room_name": session.room_group_name,
            "un_read_msg_count": unread_count,
            "status": getattr(friend.profile_detail, 'is_online', False),  # Adjust if is_online exists
            "user_id": friend.id
        }
        all_friends.append(data)

    return render(request, 'chat/friend_list.html', {'user_list': all_friends})

@login_required
def start_chat(request, room_name):
    """
    Starts chat room between two users if session exists.
    """
    current_user = request.user
    try:
        session_id = room_name[5:]
        chat_session = ChatSession.objects.filter(Q(id=session_id) & (Q(user1=current_user) | Q(user2=current_user)))
    except Exception as e:
        return HttpResponse("Something went wrong!")

    if chat_session.exists():
        chat_session = chat_session.first()
        opposite_user = chat_session.user2 if chat_session.user1 == current_user else chat_session.user1
        fetch_all_message = ChatMessage.objects.filter(chat_session=chat_session).order_by('message_detail__timestamp')

        return render(request, 'chat/start_chat.html', {
            'room_name': room_name,
            'opposite_user': opposite_user,
            'fetch_all_message': fetch_all_message
        })
    else:
        return HttpResponse("You don't have permission to chat with this user!")

@login_required
def get_last_message(request):
    """
    Fetch last message of a chat session.
    """
    session_id = request.GET.get('room_id')
    qs = ChatMessage.objects.filter(chat_session__id=session_id).last()
    if qs:
        return JsonResponse({
            'user': qs.user.username,
            'message': qs.message_detail.msg,
            'timestamp': str(qs.message_detail.timestamp)
        })
    return JsonResponse({'message': 'No messages found.'})
