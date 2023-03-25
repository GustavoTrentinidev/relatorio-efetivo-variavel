from django.db import models


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