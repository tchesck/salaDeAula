from django.db import models

# Create your models here.


class Professor(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
