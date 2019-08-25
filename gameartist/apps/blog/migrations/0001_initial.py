# Generated by Django 2.2.4 on 2019-08-25 11:41

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='titulo-del-post', help_text='Se auto-rellena al escribir el Título', max_length=255, unique_for_date='fecha_de_publicacion', verbose_name='slug')),
                ('titulo', models.CharField(default='Titulo del Post', max_length=100)),
                ('subtitulo', models.CharField(default='Subtitulo del Post', max_length=100)),
                ('imagen_principal', models.ImageField(upload_to='img/post/')),
                ('introduccion', tinymce.models.HTMLField(default='Escribe aquí el texto de la introducción...', help_text='La intro se muestra en la página principal del Blog', max_length=15000)),
                ('texto_1', tinymce.models.HTMLField(default='Escribe aquí la primera parte del post...', max_length=15000)),
                ('imagen_1', models.ImageField(blank=True, default='', upload_to='img/post/')),
                ('texto_2', tinymce.models.HTMLField(blank=True, default='', max_length=15000)),
                ('imagen_2', models.ImageField(blank=True, default='', upload_to='img/post/')),
                ('texto_3', tinymce.models.HTMLField(blank=True, default='', max_length=15000)),
                ('url_video_final', models.CharField(blank=True, default='', max_length=1000)),
                ('fecha_de_publicacion', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Fecha de publicacion')),
            ],
        ),
    ]
