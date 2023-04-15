from django.db import models

# Create your models here.

class Encuestado(models.Model):
    nombre=models.CharField(max_length=50)
    DNI=models.IntegerField()
    edad=models.IntegerField()
    sexo=models.CharField(max_length=50)
    localidad_de_nacimiento=models.CharField(max_length=50)
    localidad_de_residencia=models.CharField(max_length=50)
    nivel_educativo=models.CharField(max_length=50)
    profesion_u_oficio=models.CharField(max_length=50)

class Encuesta(models.Model): 
    pregunta=models.CharField(max_length=50)
    categoria_pregunta=models.CharField(max_length=50)

class Respuestas(models.Model):
    respuesta=models.CharField(max_length=50)



    



