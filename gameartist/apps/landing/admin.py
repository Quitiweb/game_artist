from django.contrib import admin

from .models import Solicitud, Target, Mercado, Servicios, Categoria, Imagen

admin.site.register(Solicitud)
admin.site.register(Target)
admin.site.register(Mercado)
admin.site.register(Servicios)
admin.site.register(Categoria)
admin.site.register(Imagen)
