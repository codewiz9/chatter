from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Chat(models.Model):
    messages = models.TextField(blank=True, max_length=2000, null=False),
    date = models.DateTimeField(blank=False, editable=False),
    slug = models.SlugField(allow_unicode=True, unique=True,),
    friends = models.ManyToManyField(User, through='Friend_List'),

class Friend_List(models.Model):
    friend_name = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE),
    is_friend = models.BooleanField(default=False),

    def __str__(self):
        return self.user.username


class Friend_Info(models.Model):
    friend_name = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE),
    slug = models.SlugField(allow_unicode=True, unique=True,),

class Friend_Request(models.Model):
    yes_or_no = models.BooleanField(default=False),
    friends = models.ManyToManyField(User, through='Friend_List'),
    slug = models.SlugField(allow_unicode=True, unique=True,),
