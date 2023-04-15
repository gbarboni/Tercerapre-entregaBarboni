from django.contrib import admin
from .models import Encuestado,Encuesta,Respuestas

# Register your models here.
admin.site.register(Encuestado)
admin.site.register(Encuesta)
admin.site.register(Respuestas)