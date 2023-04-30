from rest_framework.viewsets import ModelViewSet

from core.models import Aplicador
from core.serializers import AplicadorSerializer, AplicadorPostSerializer


class AplicadorViewSet(ModelViewSet):
    queryset = Aplicador.objects.all()
    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return AplicadorSerializer
        return AplicadorPostSerializer

class userDetail(ModelViewSet):
    serializer_class = AplicadorSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Aplicador.objects.filter(id=user.id)
        return queryset