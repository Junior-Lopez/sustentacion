# Generated by Django 3.0 on 2021-10-11 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='contenido',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
