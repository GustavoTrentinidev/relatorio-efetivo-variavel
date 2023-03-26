from rest_framework.serializers import ModelSerializer
from core.models import EfetivoVariavel


class EfetivoVariavelSerializer(ModelSerializer):
    class Meta:
        model = EfetivoVariavel
        fields = "__all__"