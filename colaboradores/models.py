
from django.db import models

class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    funcao = models.CharField(max_length=50)

    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Ativo')

    # O views.py não usa, mas é bom ter
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo