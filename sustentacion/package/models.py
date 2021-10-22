from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here.

class categoriaPaquete(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'categoria'
        verbose_name_plural = 'categoria_P'
    def __str__(self):
        return self.nombre


class paquete(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    comentario = models.CharField(max_length=255)
    Contenido= RichTextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to='package')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(categoriaPaquete, related_name="get_paquetes")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'paquete'
        verbose_name = 'paquete'

    def __str__(self):
        return self.nombre



