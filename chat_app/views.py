from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Chat, Friend
# Create your views here.

###Genral###
class Dashbord(generic.TemplateView):
#This classs will have the list of all the users chats

###Friends###
class Friend_Dashbord(generic.ListView):
#This view will allow users to see thire friends and see thire friend requests and this will contain the button to add new friends

class Friend_Requests_R(generic.FormView):
#this will be the form to resive freind request R=resive

class Friend_Requests_S(generic.FormView):
#This is the form for sending requests S=sent

class Find_Friends(generic.FormView):
#this will be the page where you can serch for friends

###Chat###
#the chat portion of the app will be handeled in two parts one will the the form to send the chat and one will be the
#list of all the chats the form view will be inclued on the Chat_list template
class Chat_List(generic.ListView):
#This will be the list of all the chats sent and resived

class Chat_Form(generic.FormView):
