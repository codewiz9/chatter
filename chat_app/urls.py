from django.urls import path
from . import views

app_name='chat_app'

urlpatterns = [
    path('dashbord/', views.Dashbord.as_view(), name='dashbord' ),
    path('friends/<int:pk>/', views.Friend_Dashbord.as_view(), name='friends_dashbord'),
    path('friend_requests/<int:pk>/', views.Friend_Request.as_view(), name='friends_requsetes'),
    path('find_friends/', views.Find_Friends.as_view(), name='find_friends'),
    path('chat/<int:pk>/', views.Chat_List.as_view(), name='chat'),
]
