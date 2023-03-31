from django.db import models


class EfetivoVariavel(models.Model):
    nome_guerra = models.CharField(max_length=60, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False)
    om = models.CharField(max_length=50, blank=False)
    nome_completo = models.CharField(max_length=200, blank=False, null=False)
    tipo_sanguineo = models.CharField(max_length=3, blank=False)
    grau_hieq = models.CharField(max_length=3, default="SD", blank=True)
    nome_mae = models.CharField(max_length=200, blank=False) 
    nome_pai = models.CharField(max_length=200, blank=False) 
    local_nascimento = models.CharField(max_length=100, blank=False)
    foto = models.FileField(upload_to='efetivovariavel', blank=True)

    def __str__(self):
        return self.nome_guerra

    class Meta:
        verbose_name_plural = 'efetivo variavel'