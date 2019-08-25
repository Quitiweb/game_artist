from django.contrib import admin

from .models import Solicitud, Target, Mercado, Servicios

admin.site.register(Solicitud)
admin.site.register(Target)
admin.site.register(Mercado)
admin.site.register(Servicios)