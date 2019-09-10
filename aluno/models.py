from django.db import models


# Create your models here.
from professor.models import Professor


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    prof_favorito = models.ForeignKey(
        Professor,
        on_delete = models.CASCADE,
        related_name = 'alunos'


    def __str__(self):
        return self.nome
