from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")

class List(models.Model):
    title = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="lists")
    position = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["position"]
    


class Card(models.Model):
    title = models.CharField(max_length=200)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="cards")
    position = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["position"]