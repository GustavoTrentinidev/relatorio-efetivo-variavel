from django.db import models
from django.contrib.auth.models import AbstractUser


class Aplicador(AbstractUser):
    nomeGuerra = models.CharField(max_length=60, blank=False, null=False, unique=True)
    numero = models.IntegerField(blank=True, null=True)
    om = models.CharField(max_length=50, blank=True)
    nomeCompleto = models.CharField(max_length=200, blank=False, null=False)
    grau_hieq = models.CharField(max_length=10, blank=False, null=False)
