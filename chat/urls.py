from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('chats/', views.chat_list, name='chat_list'),
    path('chats/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('chats/<int:chat_id>/delete', views.delete_chat, name='delete_chat'),
    path('register/', views.signup, name='register'),
    path('start_chat/<int:user_id>/', views.start_chat, name='start_chat'),
    path('login/', auth_views.LoginView.as_view(next_page='home'), name='login'),
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('message/<int:message_id>/update/', views.update_message, name='update_message'),
]