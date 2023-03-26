from rest_framework.serializers import ModelSerializer
from core.models import FatoObservado


class FatoObservadoSerializer(ModelSerializer):
    class Meta:
        model = FatoObservado
        fields = "__all__"