from django.shortcuts import render
from .models import Contato     #importando a class do models.py Contatos 

def index(request):
    contatos = Contato.objects.all()    #colocando os objetos do contato em uma variavel
    return render(request , 'contatos/index.html',{  #Usou a variavel dentro render dentro do dicionario
        'contatos': contatos #chave contatos e valor que vai conter todos os valores da base de dados
        })

    def ver_contato(request , contato_id):
        contato = Contato.objects.get(id=contato_id)
        return render (request , 'contatos/ver_contato.html',{
            'contato':contato
            })

