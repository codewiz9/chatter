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
    #This is the form for sending requests
    models = Friend_Request, Friend_List, Friend_Info

    def get_redirect_url(self, *args, **kwargs):
        return reverse("chat_app:friends_dashbord", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        friend = get_object_or_404(Friend_Info, slug=self.kwargs.get("slug"))
        user = get_user_model()

        try:
            Friend_Request.objects.create(sent_to=friend, sent_from=self.user)

        except User>DoesNotExist:
            message.warning(self.request, ("something went wrong pleas relod the page"))

        else:
            message.success(self.request, "Your fried request was successfully sent to {}".format(Friend_Request.sent_to))


def Accept_Friends(request, self, *args, **kwargs):
    f_request = modles.Friend_Request.objects.filter(user=self.request.user, friendrequest__slug=self.kwargs.get("slug")).get()
    f_request += 1
    f_request.save()
    return reverse("chat_app:friends_dashbord", pk=kwargs["pk"])


def Reject_Friends(request, *args):
    f_request = modles.Friend_Request.objects.filter(user=self.request.user, friendrequest__slug=self.kwargs.get("slug")).get()
    f_request += 2
    f_request.save()
    return reverse("chat_app:friends_dashbord", pk=kwargs["pk"])


class Find_Friends(generic.FormView):
    #this will be the page where you can serch for friends
    models = Friend_Info, Friend_List
    template_name = 'chat_app/find_friend.html'

    def sech_bar(request):
        if request.method == 'GET':
            serch = request.GET.get('serch')
            users = Friend_List.objects.all().filter(friends=serch)
            return render(request, 'find_friend.html', {"users":users})


###Chat###
#the chat portion of the app will be handeled in two parts one will the the form to send the chat and one will be the
#list of all the chats the form view will be inclued on the Chat_list template
class Chat_List(generic.ListView):
    #This will be the list of all the chats sent and resived
    models = Chat
    template_name = 'chat_app/chat.html'

class Chat_Form(generic.FormView):
    models = Chat
    template_name = 'chat_app/dashbord.html'
