from django.contrib import admin
from package.models import *

# Register your models here.
class PaqueteAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

admin.site.register(paquete, PaqueteAdmin)
admin.site.register(categoriaPaquete, categoriaAdmin)