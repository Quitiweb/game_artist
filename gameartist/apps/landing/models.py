from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import ugettext_lazy as _

TITLE_MAX_LENGTH = 200
EMAIL_MAX_LENGTH = 80
NOMBRE_MAX_LENGTH = 100
TEXT = 15000


class Categoria(models.Model):
    nombre = models.CharField(max_length=TITLE_MAX_LENGTH)

    def __str__(self):
        return str(self.nombre)


class Imagen(models.Model):
    nombre = models.CharField(max_length=TITLE_MAX_LENGTH)

    src = models.ImageField(upload_to='img/art/', default='', blank=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria',
        default="",
        null=True
    )

    class Meta:
        verbose_name_plural = "Imagenes"

    def __str__(self):
        return str(self.nombre)


class About(models.Model):
    titulo = models.CharField(max_length=TITLE_MAX_LENGTH)

    imagen_1 = models.ImageField(upload_to='img/about/')
    imagen_2 = models.ImageField(upload_to='img/about/', blank=True)
    imagen_3 = models.ImageField(upload_to='img/about/', blank=True)

    sobre_mi = HTMLField(
        max_length=TEXT,
        default='Me llamo Paloma Ribeiro...',
        help_text=_("Este es el texto que aparece en la seccion 'Sobre mi'")
    )

    activo = models.BooleanField(
        default=False, blank=True, help_text=_("Ten activo solo uno al mismo tiempo")
    )

    class Meta:
        verbose_name_plural = 'Sobre mi'

    def __str__(self):
        return str(self.titulo)


class Header(models.Model):
    titulo = models.CharField(max_length=TITLE_MAX_LENGTH)
    og_description = models.CharField(max_length=TITLE_MAX_LENGTH)

    class Meta:
        verbose_name_plural = 'Header'

    def __str__(self):
        return str(self.titulo)


class Empresa(models.Model):
    nombre = models.CharField(max_length=TITLE_MAX_LENGTH)
    imagen = models.ImageField(upload_to='img/empresa/', default='', blank=True)

    def __str__(self):
        return str(self.nombre)
