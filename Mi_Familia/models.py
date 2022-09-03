from django.db import models

class Familia(models.Model):
    
    pdr_nombre = models.CharField(max_length=40)
    pdr_edad = models.FloatField()
    pdr_nacimiento = models.DateField()

    mdr_nombre = models.CharField(max_length=40)
    mdr_edad = models.FloatField()
    mdr_nacimiento = models.DateField()

    hjs_nombre = models.CharField(max_length=40)
    hjs_edad = models.FloatField()
    hjs_nacimiento = models.DateField()
