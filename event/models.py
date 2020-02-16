from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

COLOR_CHOICES = (
    ('South Bombay','South Bombay'),
    ('Western Suburbs','Western Suburbs'),
    ('Eastern Suburbs','Eastern Suburbs'),
    ('North Mumbai','North Mumbai'),
)
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location=models.TextField(max_length=50, choices=COLOR_CHOICES,default="South Bombay")
    date_created = models.DateTimeField(default=timezone.now)
    hoster = models.ForeignKey(User, on_delete=models.CASCADE)
    model_pic = models.ImageField(upload_to = 'images/')
    verify = models.FileField(upload_to = 'proof/', default="proof/trek.png")    
    verified=models.BooleanField(default=False) 
    latitude=models.DecimalField(max_digits=15,decimal_places=10)
    longitude=models.DecimalField(max_digits=15,decimal_places=10)

    def __str__(self):
        return self.name

