from django.db import models
from django.contrib.auth.models import User

#the goal is to keep all the modles very basic and rely on views and the html
class Chat(models.Model):
    user = models.ManyToManyField(User, related_name='recpiants')
    message = models.TextField(max_length=500, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

#modle that contians friedns
class Friends_List(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')# makes sure that each user only has one firds list bc the one to one feild
    friends = models.ManyToManyField(User, related_name='friends_list')