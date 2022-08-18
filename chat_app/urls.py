from django.urls import path
from . import views

app_name='chat_app'

urlpatterns = [
    path('dashbord/', views.Dashbord.as_view(), name='dashbord' ),
    path('friends/<int:pk>/', views.Friend_Dashbord.as_view(), name='friends_dashbord'),
    path('friend_requests/<int:pk>/', views.Friend_Req.as_view(), name='friends_requsetes'),
    path('find_friends/', views.Find_Friends.as_view(), name='find_friends'),
    path('request_accepted/<int:pk>/', views.Accept_Friends, name='accepted'),
    path('request_rejected/<int:pk>/', views.Reject_Friends, name='rejected')
    path('chat/<int:pk>/', views.Chat_List.as_view(), name='chat'),
    path('new_chat/<int:pk>/', views.Make_New_Chat)
]
