from rest_framework.viewsets import ModelViewSet

from core.models import Aplicador
from core.serializers import AplicadorSerializer


class AplicadorViewSet(ModelViewSet):
    queryset = Aplicador.objects.all()
    serializer_class = AplicadorSerializer