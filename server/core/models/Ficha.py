from django.db import models
from core.models import EfetivoVariavel


class Ficha(models.Model):
    ev = models.OneToOneField(EfetivoVariavel, on_delete=models.CASCADE, related_name='ficha', blank=False)
    
    def __str__(self):
        return f'Ficha {self.ev.numero} {self.ev.nome_guerra}' 
