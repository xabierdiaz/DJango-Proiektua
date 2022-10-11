from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from langileak.models import Sukaldaria
from .models import Platera
from django.template import loader

# datuak ikusi
"""def index(request):
    Plat = Platera.objects.all()    #lo coge del models.py
    return render(request, 'index.html', {'Plat': Plat})"""


def index(request):
    # datuak ikusi eta plater guztien balioa gehiru.
    Plat = Platera.objects.all()  # lo coge del models.py
    p = 0
    for plt in Plat:
        p += plt.kopurua
    return render(request, 'index.html', {'Plat': Plat, 'p': p})

# datuak sartu


def add(request):
    Sukal = Sukaldaria.objects.all() # lo coge del models.py
    return render(request, 'add.html', {'Sukal': Sukal})

def addrecord(request):
    x = request.POST['platera']
    y = request.POST['kopurua']
    z = request.POST['sukaldaria']
    sukal_ob = Sukaldaria.objects.get(id=z)

    platerak_platera = Platera(platera=x, kopurua=y, sukaldaria=sukal_ob)  # coge el modelo de models.py con los valores (platera y kopurua) que nosotros hemos introducido por add.html
    platerak_platera.save()
    return HttpResponseRedirect(reverse('index'))

# datuak ezabatu

def delete(request, id):
    platerak_platera = Platera.objects.get(id=id)
    platerak_platera.delete()
    return HttpResponseRedirect(reverse('index'))

# datuak aldatu

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

# saskia

def saskia(request, id):
    pla = Platera.objects.get(id=id)
    p = 0
    p += pla.kopurua
    return render(request, 'saskia.html', {'p': p})
