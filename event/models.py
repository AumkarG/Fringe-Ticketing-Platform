from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    hoster = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

