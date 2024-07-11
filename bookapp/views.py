from django.shortcuts import render
from django.db import models


# Create your views here.

class Book(models.Model):
    
    title = models.CharField(max=100)
    price = models.IntegerField()
    
    def __str__(self):
        return '{}'.format(self.title)
