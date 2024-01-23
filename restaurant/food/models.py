from django.db import models

# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=100)
    primeryMaterial = models.CharField(max_length= 100)
    drink = models.BooleanField(default=False)
    drinkType = models.CharField(max_length=50)
    torshi = models.BooleanField(default=False)
