from django.db import models
from django.db.models.base import Model

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return self.name