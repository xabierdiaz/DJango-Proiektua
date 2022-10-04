from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),  #dirige el add.html a la funcion addrecord de views
    path('delete/<int:id>', views.delete, name='delete'),
]