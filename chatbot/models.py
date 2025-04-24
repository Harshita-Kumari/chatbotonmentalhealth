

# Create your models here.
from django.db import models

class Message(models.Model):
    USER = 'user'
    BOT = 'bot'
    SENDER_CHOICES = [
        (USER, 'User'),
        (BOT, 'Bot'),
    ]

    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.text[:50]}"
