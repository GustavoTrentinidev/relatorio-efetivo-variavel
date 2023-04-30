from rest_framework.viewsets import ModelViewSet

from core.models import Aplicador
from core.serializers import AplicadorSerializer, AplicadorPostSerializer


class AplicadorViewSet(ModelViewSet):
    queryset = Aplicador.objects.all()
    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return AplicadorSerializer
        return AplicadorPostSerializer