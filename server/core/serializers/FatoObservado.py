from rest_framework.serializers import ModelSerializer
from core.models import FatoObservado
from .Aplicador import AplicadorSerializer

class FatoObservadoSerializer(ModelSerializer):
    aplicador = AplicadorSerializer()
    class Meta:
        model = FatoObservado
        fields = "__all__"

class FOPostSerializer(ModelSerializer):
    class Meta:
        model = FatoObservado
        fields = "__all__"