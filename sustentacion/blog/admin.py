from django.contrib import admin
from blog.models import *
# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

class PublicacionesAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

admin.site.register(categorias, CategoriasAdmin)
admin.site.register(publicaciones, PublicacionesAdmin)