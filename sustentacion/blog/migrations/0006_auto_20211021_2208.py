# Generated by Django 3.0 on 2021-10-22 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_paquete_contenido'),
        ('blog', '0005_auto_20211021_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='paquete',
            field=models.ManyToManyField(to='package.categoriaPaquete'),
        ),
    ]
