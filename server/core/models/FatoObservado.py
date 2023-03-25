from django.db import models
from datetime import datetime
from core.models import Ficha


date = str(datetime.now()).split(' ')[0]


class FatoObservado(models.Model):
    fatores_possiveis = [
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo')
    ]
    fator = models.CharField(choices=fatores_possiveis, blank=False, max_length=8)
    motivo = models.CharField(max_length=40, null=False)
    descricao = models.CharField(max_length=200, null=False)
    ficha = models.ManyToManyField(Ficha, related_name='fo')
    data = models.DateField(default=date, blank=True, null=True)

    def __str__(self):
        return f'{self.fator}: {self.motivo}'