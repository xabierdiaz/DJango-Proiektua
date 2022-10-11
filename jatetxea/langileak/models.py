from email.policy import default
from django.db import models

# Create your models here.
class Sukaldaria(models.Model):
    izena = models.CharField(max_length=50)
    abizena = models.CharField(max_length=50)
    def __str__(self): # objetuari deitzerakoan self.*** jartzen dugunari deitzen diogu
        return u'%s'%self.izena