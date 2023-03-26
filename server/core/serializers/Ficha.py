from rest_framework.serializers import ModelSerializer
from core.models import Ficha


class FichaSerializer(ModelSerializer):
    class Meta:
        model = Ficha
        fields = (
            "id", "ev", "fo", "fatd"
        )
        depth = 1
