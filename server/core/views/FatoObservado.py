from rest_framework.viewsets import ModelViewSet

from core.models import FatoObservado
from core.serializers import FatoObservadoSerializer, FOPostSerializer


class FatoObservadoViewSet(ModelViewSet):
    queryset = FatoObservado.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return FatoObservadoSerializer
        return FOPostSerializer