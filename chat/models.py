from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Friends_list(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    friends = models.ManyToManyField(User, related_name='friends_list')