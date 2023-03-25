from django.contrib import admin

from core.models import EfetivoVariavel, Ficha, FatoObservado, FATD

# Register your models here.

admin.site.register(EfetivoVariavel)
admin.site.register(Ficha)
admin.site.register(FatoObservado)
admin.site.register(FATD)