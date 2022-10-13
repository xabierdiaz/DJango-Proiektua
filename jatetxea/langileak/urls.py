from django.urls import path

from . import views

urlpatterns = [
    path('', views.sukaldaria_index, name='sukaldaria_index'),   
    
    path('sukaldaria_add/', views.sukaldaria_add, name='sukaldaria_add'),
    path('sukaldaria_add/addrecord_sukaldaria/', views.addrecord_sukaldaria, name='addrecord_sukaldaria'),  #dirige el add.html a la funcion addrecord de views
    
    path('sukaldaria_update/<int:id>', views.sukaldaria_update, name='sukaldaria_update'),
    path('sukaldaria_update/sukaldaria_updaterecord/<int:id>', views.sukaldaria_updaterecord, name='sukaldaria_updaterecord'),
    
    path('sukaldaria_delete/<int:id>', views.sukaldaria_delete, name='sukaldaria_delete'),
]