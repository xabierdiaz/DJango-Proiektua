from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Sukaldaria
from django.template import loader

# Create your views here.

def sukaldaria_index(request):
    Suka = Sukaldaria.objects.all()  # lo coge del models.py
    return render(request, 'sukaldaria_index.html', {'Suka':Suka})

#sukaldaria add
def sukaldaria_add(request):
  template = loader.get_template('sukaldaria_add.html')
  return HttpResponse(template.render({}, request))

def addrecord_sukaldaria(request):
  x = request.POST['sukaldari_izena']
  y = request.POST['sukaldari_abizena']
  langileak_sukaldaria = Sukaldaria(izena=x, abizena=y) 
  langileak_sukaldaria.save()
  return HttpResponseRedirect(reverse('sukaldaria_index'))

#sukaldarua update
def sukaldaria_update(request, id):
    sukal = Sukaldaria.objects.get(id=id)
    template = loader.get_template('sukaldaria_update.html')
    context = {
        'sukal': sukal,
    }
    return HttpResponse(template.render(context, request))
  
def sukaldaria_updaterecord(request, id):
    izen = request.POST['izena']
    abizen = request.POST['abizena']
    sukalda = Sukaldaria.objects.get(id=id)
    sukalda.izena = izen
    sukalda.abizena = abizen
    sukalda.save()
    return HttpResponseRedirect(reverse('sukaldaria_index'))
  
#datuak ezabatu
def sukaldaria_delete(request, id):
  sukal = Sukaldaria.objects.get(id=id)
  sukal.delete()
  return HttpResponseRedirect(reverse('sukaldaria_index'))