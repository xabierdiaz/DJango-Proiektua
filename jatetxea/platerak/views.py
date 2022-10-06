from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Platera
from django.template import loader

#datuak ikusi
"""def index(request):
    Plat = Platera.objects.all()    #lo coge del models.py
    return render(request, 'index.html', {'Plat': Plat})"""


def index(request):
    #datuak ikusi eta plater guztien balioa gehiru.
    Plat = Platera.objects.all()    #lo coge del models.py
    p=0
    for plt in Plat:
      p += plt.kopurua
    return render(request, 'index.html', {'Plat': Plat, 'p':p})

#datuak sartu
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['platera']
  y = request.POST['kopurua']
  platerak_platera = Platera(platera=x, kopurua=y) #coge el modelo de models.py con los valores (platera y kopurua) que nosotros hemos introducido por add.html
  platerak_platera.save()
  return HttpResponseRedirect(reverse('index'))

#datuak ezabatu
def delete(request, id):
  platerak_platera = Platera.objects.get(id=id)
  platerak_platera.delete()
  return HttpResponseRedirect(reverse('index'))

#datuak aldatu
def update(request, id):
  platerak_platera = Platera.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'platerak_platera': platerak_platera,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  plat = request.POST['platera']
  kop = request.POST['kopurua']
  platob = Platera.objects.get(id=id)
  platob.platera = plat
  platob.kopurua = kop
  platob.save()
  return HttpResponseRedirect(reverse('index'))

#saskia
def saskia(request, id):
    Plat = Platera.objects.all()    #lo coge del models.py
    pla = Platera.objects.get(id=id)
    p = 0
    p += pla.kopurua
    return render(request, 'saskia.html', {'Plat': Plat, 'p':p})
  
