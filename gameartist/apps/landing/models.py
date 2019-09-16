from django.db import models

TITLE_MAX_LENGTH = 200
EMAIL_MAX_LENGTH = 80
NOMBRE_MAX_LENGTH = 100


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return str(self.nombre)


class Imagen(models.Model):
    nombre = models.CharField(max_length=50)

    src = models.ImageField(upload_to='img/art/', default='', blank=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria',
        default="",
        null=True
    )

    def __str__(self):
        return str(self.nombre)
