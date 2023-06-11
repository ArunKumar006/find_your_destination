from django.db import models

# Create your models here.

class States(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class Destinations(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    state = models.ForeignKey(States,on_delete=models.CASCADE)
    