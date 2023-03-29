from django.db import models
from ckeditor.fields import RichTextField
# Creacion de los modelos Categoria y Autor

class Categoria(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField('Nombre de Categoria', max_length = 100, null = False, blank = False)
	estado = models.BooleanField('Categoria Activada/Categoria no Activada',default = True)
	fecha_creacion = models.DateTimeField('Fecha de Creacion',auto_now = False, auto_now_add = True)

	class Meta:
 	 verbose_name = 'Categoria'
 	 verbose_name_plural = 'Categorias'

	def __str__(self):
		return self.nombre

class Autor(models.Model):
	id = models.AutoField(primary_key = True)
	nombres = models.CharField('Nombres de Autor',max_length=255, null=False, blank=False)
	apellidos = models.CharField('Apellidos de Autor',max_length=100, null=False, blank=False)
	facebook = models.URLField('facebook',null= True, blank = True)
	twitter = models.URLField('twitter', null = True, blank = True)
	instagram = models.URLField('instagram', null = True, blank = True)
	web = models.URLField('web', null = True, blank = True)
	correo = models.EmailField('Correo Electronico',blank = False, null = False)
	estado = models.BooleanField('Autor Activada/Autor no Activada', default = True)
	fecha_creacion = models.DateTimeField('Fecha de Creacion', auto_now = False, auto_now_add = True)

	class Meta:
		verbose_name = 'Autor'
		verbose_name_plural = 'Autores'
		
	def __str__(self):
			return "{0},{1}".format(self.apellidos, self.nombres)

class Post(models.Model):
	id = models.AutoField(primary_key = True)
	titulo = models.CharField('Titulo', max_length=90, blank = False, null=False)
	slug = models.CharField('Slug', max_length=100, blank = False, null=False)
	descripción = models.CharField('Descripción', max_length=110, blank = False, null=False)
	contenido = RichTextField('Contenido')
	imagen = models.URLField(max_length= 255)
	autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
	categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
	estado = models.BooleanField('Publicado/No Publicado', default = True)
	fecha_creacion = models.DateTimeField('Fecha de Creacion', auto_now = False, auto_now_add = True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		
	def __str__(self):
		return  self.titulo
