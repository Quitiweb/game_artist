# Generated by Django 2.1.9 on 2019-09-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_auto_20190920_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='activo',
            field=models.BooleanField(blank=True, default=False, help_text='Ten activo solo uno'),
        ),
    ]
