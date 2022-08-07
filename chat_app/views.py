from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Chat, Friend_List, Friend_Info, Friend_Request
# Create your views here.

###Genral###
class Dashbord(generic.TemplateView):
    #This classs will have the list of all the users chats
    models = Chat, Friend_List
    template_name = 'chat_app/dashbord.html'


###Friends###
class Friend_Dashbord(generic.ListView):
    #This view will allow users to see thire friends and see thire friend requests and this will contain the button to add new friends
    models = Friend_Info, Friend_List
    template_name = 'chat_app/friend_dashbord.html'

class Friend_Request(generic.RedirectView):
    #This is the form for sending requests S=sent
    models = Friend_Request, Friend_list, Friend_Info
    def get(self, request, *args, **kwargs):
        friend = get_object_or_404(Friend_Info, slug=self.kwargs.get("slug"))

        try:
            Friend_Request.objects.create(friends=)

class Find_Friends(generic.FormView):
    #this will be the page where you can serch for friends
    models = Friend
    template_name = 'chat_app/dashbord.html'

###Chat###
#the chat portion of the app will be handeled in two parts one will the the form to send the chat and one will be the
#list of all the chats the form view will be inclued on the Chat_list template
class Chat_List(generic.ListView):
    #This will be the list of all the chats sent and resived
    models = Chat
    template_name = 'chat_app/dashbord.html'

class Chat_Form(generic.FormView):
    models = Chat
    template_name = 'chat_app/dashbord.html'
