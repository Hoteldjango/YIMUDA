from django.db import models
from django.utils import timezone

#hay que hacer que importe los usuarios de django
class Usuario(models.Model):
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	dni = models.IntegerField()
	direccion = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	telefono = models.IntegerField()
	def __str__(self):
		return self.apellido

class Habitacion(models.Model):
	numero_habitacion =  models.IntegerField(default=0)
	imagen = models.ImageField(upload_to="foto", null=True, blank=True )
	precio = models.IntegerField(default=0)
	capacidad = models.IntegerField(default=0)
	clase = models.ForeignKey('Clases', on_delete=models.CASCADE)
	estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
	informacion = models.TextField(max_length=200)
	def __str__(self):
		return str(self.numero_habitacion)

class Reserva(models.Model):
	#usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	clase = models.ForeignKey('Clases', on_delete=models.CASCADE)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	consulta = models.TextField(max_length=1000)

	def __str__(self):
		return self.clase

class Estado(models.Model):
	disponibilidad = models.CharField(max_length=200)
	def __str__(self):
		return self.disponibilidad

class Clases(models.Model):
	tipos = models.TextField(max_length=28)
	precios = models.FloatField()

	def __str__(self):
		return self.tipos

class Opinion(models.Model):
	descripcion = models.TextField(max_length=1000)
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.descripcion


class Contacto(models.Model):
	descripcion = models.TextField(max_length=1000)
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.descripcion

class Promocion(models.Model):
	datos = models.TextField(max_length=200)
	id_habitacion = models.ForeignKey('Habitacion', on_delete=models.CASCADE)
	vigencia = models.TextField()

	def __str__(self):
		return self.datos