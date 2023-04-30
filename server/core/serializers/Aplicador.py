from rest_framework.serializers import ModelSerializer
from core.models import Aplicador


class AplicadorSerializer(ModelSerializer):
    class Meta:
        model = Aplicador
        fields = (
                "id",
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

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance