from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.views import AplicadorViewSet, EfetivoVariavelViewSet, FichaViewSet, FATDViewSet, FatoObservadoViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r"aplicador", AplicadorViewSet)
router.register(r"efetivovariavel", EfetivoVariavelViewSet)
router.register(r"ficha", FichaViewSet)
router.register(r"fatd", FATDViewSet)
router.register(r"fo", FatoObservadoViewSet)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
