import decimal

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Car(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Statuses(models.TextChoices):
    active = 'active'
    finished = 'finished'
    paused = 'paused'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.TextField(choices=Statuses.choices, default=Statuses.active, editable=False)
    start = models.DateTimeField(auto_now_add=True, editable=False)
    finish = models.DateTimeField(null=True, blank=True, editable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


    def calculate_order(self):
       return decimal.Decimal((self.finish-self.start) / 60 * self.car.price)


    def save(self, *args, **kwargs):
        if self.status == Statuses.finished and not self.finish:
            self.finish - datetime.now()
            self.user.balance.debit(self.calculate_order)
        return super(Order, self).save(*args, **kwargs)

