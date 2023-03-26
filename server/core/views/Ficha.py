from rest_framework.viewsets import ModelViewSet

from core.models import Ficha
from core.serializers import FichaSerializer


class FichaViewSet(ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer