from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=50)
    quantitiy = models.IntegerField()
