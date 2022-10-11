from django.db import models
from django.utils import timezone


class PriorityLevel(models.IntegerChoices):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5


class Task(models.Model):
    content = models.CharField(max_length=200)
    due_date = models.DateField()
    priority_level = models.IntegerField(choices=PriorityLevel.choices)
    finished = models.BooleanField()

