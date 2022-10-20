from django.db import models

from django.contrib.auth.models import User

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    bank_acc = models.IntegerField()
    coins = models.DecimalField(max_digits=10, decimal_places=2)
