from django.shortcuts import render
from .models import Platera


def index(request):
    Plat = Platera.objects.all()
    return render(request, 'index.html', {'Plat': Plat})