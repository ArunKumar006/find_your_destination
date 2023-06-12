from django.db import models

# Create your models here.

class States(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

class District(models.Model):
    state = models.ForeignKey(States,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Destinations(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    state = models.ForeignKey(States,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    near_railway_station=models.CharField(max_length=100,null=True,blank=True)
    main_railwy_station = models.CharField(max_length=100,null=True,blank=True)
    near_aiport = models.CharField(max_length=100,null=True,blank=True)
    rating = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    

class Places(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destinations,on_delete=models.CASCADE)
    rating = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name
    
