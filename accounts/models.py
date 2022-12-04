from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nome_completo = models.CharField(max_length=100 ,null= True)
    cpf = models.CharField(max_length=14 , null= True)
    cep = models.CharField(max_length=10 , null= True)
    telefone= models.CharField(max_length=16, null= True)
    email = models.EmailField(max_length=100 , null= True)
    estado = models.CharField(max_length= 50 , null= True)
    cidade = models.CharField(max_length=100 , null= True)
    usuario =models.OneToOneField(User,on_delete=models.CASCADE)
