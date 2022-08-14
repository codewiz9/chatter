from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Chat(models.Model):
    messages = models.TextField(blank=True, max_length=2000, null=False),
    date = models.DateTimeField(blank=False, editable=False, auto_now=True),
    slug = models.SlugField(allow_unicode=True, unique=True, editable=False),
    friends = models.ManyToManyField(User, through='Friend_Info'),
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE),

class Friend_List(models.Model):
    friends = models.ManyToManyField(User, through='Friend_Info'),


    def __str__(self):
        return self.user.username


class Friend_Info(models.Model):
    friend_name = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE),
    slug = models.SlugField(allow_unicode=True, unique=True,),

class Friend_Request(models.Model):
    slug = models.SlugField(allow_unicode=True, unique=True, editable=False),
    # create a tuple to manage different options for your request status
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Rejected'),
    )
    # store this as an integer, Django handles the verbose choice options
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    # store the user that has sent the request
    sent_from = models.ForeignKey(User, related_name="requests_sent", on_delete=models.CASCADE)
    # store the user that has received the request
    sent_to = models.ForeignKey(User, related_name="requests_received", on_delete=models.CASCADE)
    sent_on = models.DateTimeField(blank=False, editable=False, auto_now=True)
