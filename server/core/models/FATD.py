from django.db import models
from datetime import datetime
from core.models import Ficha
from django.contrib.auth import get_user_model


date = str(datetime.now()).split(' ')[0]


class FATD(models.Model):
    aplicador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='fatds')
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

    def __str__(self):
        return self.punicao