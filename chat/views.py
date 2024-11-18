from django.shortcuts import render
from django.views import generic
from .models import Chat, Friends_List
from django.contrib.auth.models import User

#this view should show part of a users firds list and their most recent chats
#it should also have ways to accseus the full firnds list and chats
class dashbaord(generic.TemplateView):
    pass

class add_friend(generic.UpdateView):
    pass

class send_message(generic.CreateView):
    pass
