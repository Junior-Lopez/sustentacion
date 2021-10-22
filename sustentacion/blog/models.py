from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from package.models import categoriaPaquete

# Create your models here.
class categorias(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'categorias'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.nombre

class publicaciones(models.Model):
    titulo = models.CharField(max_length=100)
    Contenido= RichTextField(verbose_name="Contenido")
    fecha_publicidad = models.DateTimeField(default=now)
    imagen = models.ImageField(upload_to='blog')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(categorias)
    paquete = models.ManyToManyField(categoriaPaquete)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'publicaciones'
        verbose_name_plural = 'publicaciones'
    def __str__(self):
        return self.titulo

