from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length = 40)
    price = models.FloatField()
    detail = models.TextField(blank=True)
    state = models.BooleanField(default=False)
    quantity = models.IntegerField()
