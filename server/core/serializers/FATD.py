from rest_framework.serializers import ModelSerializer
from core.models import FATD
from .Aplicador import AplicadorSerializer

class FATDViewSerializer(ModelSerializer):
    aplicador = AplicadorSerializer()
    class Meta:
        model = FATD
        fields = "__all__"

class FATDPostSerializer(ModelSerializer):
    class Meta:
        model = FATD
        fields = "__all__"