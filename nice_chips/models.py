# imports
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone


# class-model for my draft
class Draft(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    drafts = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# class-model form my reminder
class Reminder(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_is_up = models.DateTimeField(auto_now_add=False)
    reminders = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.text