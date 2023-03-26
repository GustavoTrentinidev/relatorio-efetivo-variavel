from rest_framework.serializers import ModelSerializer
from core.models import Aplicador


class AplicadorSerializer(ModelSerializer):
    class Meta:
        model = Aplicador
        fields = (
                "username",
                "password",
                "nomeGuerra",
                "numero",
                "om",
                "nomeCompleto",
                "grau_hieq"
            )
