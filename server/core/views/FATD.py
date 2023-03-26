from rest_framework.viewsets import ModelViewSet

from core.models import FATD
from core.serializers import FATDSerializer


class FATDViewSet(ModelViewSet):
    queryset = FATD.objects.all()
    serializer_class = FATDSerializer