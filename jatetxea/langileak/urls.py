from django.urls import path

from . import views

urlpatterns = [
    path('', views.langilea_index, name='langilea_index'),   
]