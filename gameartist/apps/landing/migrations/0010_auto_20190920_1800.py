# Generated by Django 2.1.9 on 2019-09-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_about_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('og_description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Header',
            },
        ),
        migrations.AlterField(
            model_name='about',
            name='activo',
            field=models.BooleanField(blank=True, default=False, help_text='Ten activo solo uno al mismo tiempo'),
        ),
    ]
