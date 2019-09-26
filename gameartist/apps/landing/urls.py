from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('mensaje-enviado', views.mensaje_enviado, name='mensaje-enviado'),
    path('about', views.about, name='about'),
    path('categoria/<int:cat>', views.categoria, name='categoria')
]
