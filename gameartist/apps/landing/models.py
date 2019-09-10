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


class Target(models.Model):
    MUJER = 'MUJER'
    HOMBRE = 'HOMBRE'
    NIÑOS = 'NIÑOS'
    ADOL = 'ADOLESCENTES'
    ADUL = 'ADULTOS'

    TARGET = (
        (MUJER, 'Mujer'),
        (HOMBRE, 'Hombre'),
        (NIÑOS, 'Niños'),
        (ADOL, 'Adolescentes'),
        (ADUL, 'Adultos'),
    )

    target = models.CharField(
        max_length=15,
        choices=TARGET,
        default=MUJER,
    )

    class Meta:
        verbose_name_plural = 'Target'

    def __str__(self):
        return str(self.target)


class Mercado(models.Model):
    TEXTIL = 'TEXTIL'
    CAL = 'CALZADO'
    COMP = 'COMPLEMENTOS'
    MAQ = 'MAQUILLAJE'
    COSM = 'COSMETICA'
    PERF = 'PERFUMERIA'
    OTRO = 'OTRO'

    MERCADO = (
        (TEXTIL, 'Textil'),
        (CAL, 'Calzado'),
        (COMP, 'Complementos'),
        (MAQ, 'Maquillaje'),
        (COSM, 'Cosmética'),
        (PERF, 'Perfumería'),
        (OTRO, 'Otro'),
    )

    mercado = models.CharField(
        max_length=15,
        choices=MERCADO,
        default=TEXTIL,
    )

    class Meta:
        verbose_name_plural = 'Mercado'

    def __str__(self):
        return str(self.mercado)


class Servicios(models.Model):
    FAB = 'FABRICACION'
    OBRAS = 'OBRAS'
    SOFT = 'SOFTWARE'
    GEST = 'GESTORIAS'
    FINAN = 'FINANCIACION'
    MARK = 'MARKETING'
    INFLUEN = 'INFLUENCERS'
    CONSUL = 'CONSULTORIA'
    ASOC = 'ASOCIACIONES'
    INFO = 'INFORMACION'

    SERVICIOS = (
        (FAB, 'Fabricación, Confección, Packaging'),
        (OBRAS, 'Obras, Logística, Almacén'),
        (SOFT, 'Software, Hardware, Comunicaciones'),
        (GEST, 'Gestorías, Seguros, Abogados'),
        (FINAN, 'Financiación, Bancos'),
        (MARK, 'Marketing, Eventos'),
        (INFLUEN, 'Influencers, Ventas'),
        (CONSUL, 'Consultoría, Asesoramiento'),
        (ASOC, 'Asociaciones, Instituciones'),
        (INFO, 'Información, Noticias'),
    )

    servicios = models.CharField(
        max_length=50,
        choices=SERVICIOS,
        default=FAB,
    )

    class Meta:
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return str(self.servicios)


class Solicitud(models.Model):
    MARCA = 'MARCA'
    ESPACIO = 'ESPACIO'
    SERVICIO = 'SERVICIO'

    TYPE = (
        (MARCA, 'Marca'),
        (ESPACIO, 'Espacios (Offline/Online)'),
        (SERVICIO, 'Servicio'),
    )

    quien_eres = models.CharField(
        max_length=10,
        choices=TYPE,
        default=MARCA,
    )

    servicios = models.ManyToManyField(Servicios)

    mercado = models.ManyToManyField(Mercado)

    target = models.ManyToManyField(Target)

    que_buscas = models.CharField(
        max_length=10,
        choices=TYPE,
        default=ESPACIO,
    )

    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    nombre = models.CharField(max_length=NOMBRE_MAX_LENGTH)

    class Meta:
        verbose_name_plural = 'Solicitudes'

    def __str__(self):
        return str(self.nombre) + ' - ' + self.quien_eres + ' - ' + self.email

# class Pregunta(models.Model):
#     pregunta_text = models.CharField(max_length=TITLE_MAX_LENGTH)
#     pub_fecha = models.DateTimeField('fecha de publicación')
#
# class Respuesta(models.Model):
#     pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
#     respuesta_text = models.CharField(max_length=TITLE_MAX_LENGTH)
#     respuesta_icon = models.ImageField(upload_to='img/respuesta/')