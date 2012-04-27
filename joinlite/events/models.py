from django.db import models

# Create your models here.

class Event(models.Model):
  organizer_email = models.CharField(max_length=256)
  name = models.CharField(max_length=128)
  code = models.CharField(max_length=64)
  date = models.DateTimeField()
  location = models.CharField(max_length=128)
  url = models.CharField(max_length=256)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)



