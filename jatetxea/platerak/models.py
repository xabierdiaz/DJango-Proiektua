from django.db import models

from django.db import models
from langileak.models import Sukaldaria

# Create your models here.
class Platera(models.Model):
    platera = models.CharField(max_length=50)
    kopurua = models.IntegerField()
    sukaldaria = models.ForeignKey(Sukaldaria, on_delete=models.CASCADE, null=True)
    def __str__(self): # objetuari deitzerakoan self.*** jartzen dugunari deitzen diogu
        return u'%s'%self.platera
