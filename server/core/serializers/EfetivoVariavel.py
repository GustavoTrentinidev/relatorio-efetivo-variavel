from rest_framework.serializers import ModelSerializer
from core.models import EfetivoVariavel, Ficha


class EfetivoVariavelSerializer(ModelSerializer):
    class Meta:
        model = EfetivoVariavel
        fields = "__all__"

    def create(self, validated_data):
        efetivoev = EfetivoVariavel.objects.create(**validated_data)
        Ficha.objects.create(ev=efetivoev)
        return efetivoev