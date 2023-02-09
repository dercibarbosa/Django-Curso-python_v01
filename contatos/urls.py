from django.urls import path
from . import views

urlpatterns =[
    path ('', views.index , name='index'), #index pagina principal
   # path ('<int:contato_id>', views.ver_contato, name='ver_contato'), #O views ver contato tem que ser criadoz

    ]
