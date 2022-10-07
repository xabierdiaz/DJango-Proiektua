from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def langilea_index(request):
    return render(request, 'langilea_index.html')