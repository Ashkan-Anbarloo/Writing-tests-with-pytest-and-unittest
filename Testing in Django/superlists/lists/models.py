from django.db import models

# Create your models here.


class List(models.Model):
    pass
class Item(models.Model):
    list = models.ForeignKey(List , default=None , on_delete=models.CASCADE)
    text = models.TextField(default="")
    