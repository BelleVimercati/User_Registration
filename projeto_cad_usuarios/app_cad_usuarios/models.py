from django.db import models

class Usuario(models.Model):
    #campos da tabela de usuarios
    id_usuario = models.AutoField(primary_key=True) #Chave primaria
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
