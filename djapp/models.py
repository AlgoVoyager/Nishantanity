from django.db import models
from django.db.models.base import Model

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    date =  models.DateTimeField()

    def __str__(self):
        return self.name
    
class raw_text(models.Model):
    RawText = models.TextField(max_length=1000)
    rdate = models.DateTimeField()
    
    def __str__(self):
        temp = str(self.rdate)
        temp1= str(self.RawText)
        temp2= temp + " | " + temp1
        return temp2

