from django.urls import path
from . import views

app_name='chat_app'

urlpatterns = [
    path('dashbord/', views.Dashbord.as_view(), name='dashbord' ),
    path('friends/<int:slug>/', views.Friend_Dashbord.as_view(), name='friends_dashbord'),
    path('friend_requests/<int:slug>/', views.Friend_Request.as_view(), name='friends_requsetes'),
    path('find_friends/', views.Find_Friends.as_view(), name='find_friends'),
    path('request_accepted/<int:slug>/', views.Accept_Friends, name='accepted'),
    path('request_rejected/<int:slug>/', views.Reject_Friends, name='rejected'),
    path('chat/<int:slug>/', views.Chat_List.as_view(), name='chat'),
    path('new_chat/<int:slug>/', views.Make_New_Chat.as_view(), name='new_chat'),
    path('friend_list/<int:slug>/', views.Friend_List.as_view(), name='friend_list'),
]
