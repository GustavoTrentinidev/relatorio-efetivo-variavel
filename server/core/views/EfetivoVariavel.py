from rest_framework.viewsets import ModelViewSet

from core.models import EfetivoVariavel
from core.serializers import EfetivoVariavelSerializer


class EfetivoVariavelViewSet(ModelViewSet):
    queryset = EfetivoVariavel.objects.all()
    serializer_class = EfetivoVariavelSerializer