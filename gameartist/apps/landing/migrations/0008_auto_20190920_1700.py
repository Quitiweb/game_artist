# Generated by Django 2.1.9 on 2019-09-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20190920_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='titulo',
            field=models.CharField(default='any', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
