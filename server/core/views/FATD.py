from rest_framework.viewsets import ModelViewSet

from core.models import FATD
from core.serializers import FATDViewSerializer, FATDPostSerializer


class FATDViewSet(ModelViewSet):
    queryset = FATD.objects.all()
    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return FATDViewSerializer
        return FATDPostSerializer