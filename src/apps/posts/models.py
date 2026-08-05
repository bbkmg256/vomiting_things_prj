from django.db import models
from django.utils import timezone

from apps.tablon.models import Tablon


# Clase para los posteos
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=60, null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateField(default=timezone.localdate)
    hora_publicacion = models.TimeField(default=timezone.localtime)
    # Tablon/topico al que pertenece
    tablon = models.ForeignKey(Tablon, on_delete=models.CASCADE)


# Crear clase para los comentarios
# ...
