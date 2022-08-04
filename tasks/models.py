from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=80)
    date_add = models.DateTimeField()
    done = models.BooleanField(default=False)
    money = models.IntegerField()
    account_task_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task


class Market(models.Model):
    text = models.CharField(max_length=80)
    buy = models.BooleanField(default=False)
    price = models.IntegerField()
    account_market_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
