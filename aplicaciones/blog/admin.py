from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin



# Para agregar boton de importar y exportar debemos instalar los paquetes pip install import_export
#agregar las clases y agregar ImportExportModelAdmin en la clase admin

class CategoriaResource(resources.ModelResource):
	class Meta:
		model = Categoria 

class AutorResource(resources.ModelResource):
	class Meta:
		model = Autor 

# Por convencion creamos dos clases con el nombre del Modelo adjuntado al Admin. Para que podamos insertar un boton de busqueda
# search_fields mas los campos que quiero buscar
#Para mostar en lista debo agregar el campo list_display mas los campos que quiero mostrar 

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre', 'estado', 'fecha_creacion',)
	resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ['nombres', 'apellidos', 'correo',]
	list_display = ('nombres', 'apellidos', 'correo', 'estado', 'fecha_creacion',)
	resource_class = AutorResource

# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post)
