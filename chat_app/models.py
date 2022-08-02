from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Chat(models.Model):
    messages = models.TextField(blank=True, max_length=2000, null=False),
    date = models.DateTimeField(blank=False, editable=False),
    slug = models.SlugField(allow_unicode=True, unique=True),
    friends = models.ManyToManyField(User, through='Friend'),

class Friend(models.Model):
    friend_name = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE),
    is_friend = models.BooleanField(default=False),


class FriendRequest(models.Model):
    name_of_sender = models.ManyToManyField(User, through='Friend'),
