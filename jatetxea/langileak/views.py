from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Sukaldaria
from django.template import loader

# Create your views here.

def sukaldaria_index(request):
  return render(request, 'sukaldaria_index.html')

def sukaldaria_add(request):
  template = loader.get_template('sukaldaria_add.html')
  return HttpResponse(template.render({}, request))

def addrecord_sukaldaria(request):
  x = request.POST['sukaldari_izena']
  y = request.POST['sukaldari_abizena']
  langileak_sukaldaria = Sukaldaria(izena=x, abizena=y) 
  langileak_sukaldaria.save()
  return HttpResponseRedirect(reverse('sukaldaria_index'))