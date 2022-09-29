from django.db import models

# Create your models here.
class Platera(models.Model):
    platera = models.CharField(max_length=50)
    kopurua = models.IntegerField()
