from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from core.models import EfetivoVariavel
from core.serializers import EfetivoVariavelSerializer, EfetivoVariavelGetSerializer


class EfetivoVariavelViewSet(ModelViewSet):
    queryset = EfetivoVariavel.objects.all()
    filter_backends = [filters.SearchFilter]
    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return EfetivoVariavelGetSerializer
        return EfetivoVariavelSerializer
    serializer_class = EfetivoVariavelSerializer
    search_fields = ['nome_guerra', 'numero', 'om']