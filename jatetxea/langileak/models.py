from email.policy import default
from django.db import models
from platerak.models import Platera

# Create your models here.
class Langilea(models.Model):
    izena = models.CharField(max_length=50)
    platera = models.ForeignKey(Platera, on_delete=models.CASCADE)