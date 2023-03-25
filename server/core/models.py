from django.db import models

# Create your models here.
class EfetivoVariavel(models.Model):
    nomeGuerra = models.CharField(max_length=60, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    nomeCompleto = models.CharField(max_length=200, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=True)
    tipoSanguineo = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.nomeGuerra

    class Meta:
        verbose_name_plural = 'efetivo variavel'

class Ficha(models.Model):
    def __str__(self):
        return self.ev.nomeGuerra

    ev = models.ForeignKey(EfetivoVariavel, on_delete=models.CASCADE, related_name='ficha')

from datetime import datetime
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
        return self.fator

class FATD(models.Model):
    punicoes_possiveis = [
        ('Advertência', 'Advertência'),
        ('Repreensão', 'Repreensão'),
        ('Detenção', 'Detenção'),
        ('Prisão', 'Prisão'),
        ('Exclusão a bem da disciplina', 'Exclusão a bem da disciplina'),
    ]
    punicao = models.CharField(max_length=50, choices=punicoes_possiveis, blank=False)
    descricao = models.CharField(max_length=200, blank=False)
    ficha = models.ManyToManyField(Ficha, related_name='fatd')
    data = models.DateField(default=date, blank=True, null=True)


