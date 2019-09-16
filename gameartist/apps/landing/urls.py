from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mensaje-enviado', views.mensaje_enviado, name='mensaje-enviado'),
    path('about', views.about, name='about'),
    path('categoria/<cat>', views.categoria, name='categoria')
]
