from django.shortcuts import render
from django.views import generic
from .models import Chat, Friends_List
from django.contrib.auth.models import User
from django.db.models import Max, F

#this view should show part of a users firds list and their most recent chats
#it should also have ways to accseus the full firnds list and chats
class DashboardView(generic.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'latest_chats'  # More descriptive name for the varribal

    def get_queryset(self):
       
        latest_chat_ids = Chat.objects.filter(users=self.request.user).values('users').annotate(latest_chat=Max('id')).values_list('latest_chat', flat=True)
        latest_chats = Chat.objects.filter(id__in=latest_chat_ids).order_by('-timestamp')

        return latest_chats




class add_friend(generic.UpdateView):
    pass

class send_message(generic.CreateView):
    pass
