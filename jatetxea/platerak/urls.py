from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),  #dirige el add.html a la funcion addrecord de views
    
    path('delete/<int:id>', views.delete, name='delete'),
    
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),    
    
    path('saskia/<int:id>', views.saskia, name='saskia'),
    
    path('langileak/', include('langileak.urls')), #'' me envia al langileak url
]