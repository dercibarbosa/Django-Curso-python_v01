from django.contrib import admin
from . models import Categoria , Contato #importando os modulos criados

class ContatoAdmin(admin.ModelAdmin):

  list_display = ('id','nome','sobrenome','tefone','email','data_criacao','categoria')
  list_display_links = ('id','nome','sobrenome')
  list_filter = ('nome','sobrenome')
  list_per_page = 1
  search_field = ('nome','sobrenome','email')

admin.site.register(Categoria)#Modelo Categoria
admin.site.register(Contato)  #Modelo Contato

#admin.site.register(Contato, contatoAdmin)
