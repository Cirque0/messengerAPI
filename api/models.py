from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=32, blank=True)

class Conversation(models.Model):
    name = models.CharField(max_length=64, blank=True)
    members = models.ManyToManyField(User, blank=False, related_name="conversations")

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="outbox")
    receiver = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)