from rest_framework.serializers import ModelSerializer
from drf_extra_fields.fields import Base64ImageField
from core.models import EfetivoVariavel, Ficha


class EfetivoVariavelSerializer(ModelSerializer):
    foto = Base64ImageField()
    class Meta:
        model = EfetivoVariavel
        fields = (
            "nome_guerra",
            "numero",
            "cpf",
            "om",
            "nome_completo",
            "tipo_sanguineo",
            "grau_hieq",
            "nome_mae",
            "nome_pai",
            "local_nascimento",
            "data_nascimento",
            "foto",
            "ficha"
        )

    def create(self, validated_data):
        efetivoev = EfetivoVariavel.objects.create(**validated_data)
        Ficha.objects.create(ev=efetivoev)
        return efetivoev