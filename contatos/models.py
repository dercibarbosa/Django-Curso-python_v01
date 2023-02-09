from django.db import models #class models
from  django.utils import timezone


class Categoria(models.Model): #class categoria herda de model
    nome = models.CharField(max_length=255)

    def __str__(self): 
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255) #nome herda da class models
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now) #metodo nao executa
    descricao = models.TextField(blank=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.DO_NOTHING) #relacionamento de tabelas


    def __str__(self): 
        return self.nome
