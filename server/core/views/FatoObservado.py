from rest_framework.viewsets import ModelViewSet

from core.models import FatoObservado
from core.serializers import FatoObservadoSerializer


class FatoObservadoViewSet(ModelViewSet):
    queryset = FatoObservado.objects.all()
    serializer_class = FatoObservadoSerializer