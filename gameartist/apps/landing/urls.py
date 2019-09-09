from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('mensaje-enviado', views.mensaje_enviado, name='mensaje-enviado'),
    path('solicitud-recibida', views.solicitud_recibida, name='solicitud-recibida'),
    path('categoria/<cat>', views.categoria, name='categoria')
]