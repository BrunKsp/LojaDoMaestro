from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    nome= models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='media')
    descricao= models.TextField()
    quantidade = models.IntegerField()
    preco = models.FloatField()
   


    def __str__(self):
        return self.nome

