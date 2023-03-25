from django.db import models
from core.models import EfetivoVariavel


class Ficha(models.Model):
    ev = models.ForeignKey(EfetivoVariavel, on_delete=models.CASCADE, related_name='ficha')
    
    def __str__(self):
        return f'Ficha {self.ev.numero} {self.ev.nomeGuerra}' 
