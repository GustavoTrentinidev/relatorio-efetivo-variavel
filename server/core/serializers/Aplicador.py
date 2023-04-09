from rest_framework.serializers import ModelSerializer
from core.models import Aplicador


class AplicadorSerializer(ModelSerializer):
    class Meta:
        model = Aplicador
        fields = (
                "nome_guerra",
                "numero",
                "om",
                "nome_completo",
                "grau_hieq"
            )

class AplicadorPostSerializer(ModelSerializer):
    class Meta:
        model = Aplicador
        fields = (
                "username",
                "password",
                "nome_guerra",
                "numero",
                "om",
                "nome_completo",
                "grau_hieq"
            )