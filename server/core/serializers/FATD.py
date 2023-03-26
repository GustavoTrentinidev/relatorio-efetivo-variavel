from rest_framework.serializers import ModelSerializer
from core.models import FATD


class FATDSerializer(ModelSerializer):
    class Meta:
        model = FATD
        fields = "__all__"