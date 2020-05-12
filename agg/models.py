from django.db import models

# Create your models here.

class country(models.Model):
    name=models.CharField(max_length=100)
    cities=models.ManyToManyField('city')
    def __str__(self):
        return self.name

class city(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
