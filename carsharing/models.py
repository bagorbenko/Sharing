from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Car(models.Model):
    pass


class Statuses(models.TextChoices):
    active = 'active'
    finished = 'finished'
    paused = 'paused'


class Order(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField(choices=Statuses.choices, default=Statuses.active)
    stat = models.DateTimeField(auto_now_add=True, editable=False)
    finish = models.DateTimeField()

