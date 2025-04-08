from django.db import models
import datetime



class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.nombre


class historia(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
    nombre = models.CharField(max_length=100, unique=True)
    contenido = models.TextField(null=True, blank=True)
    fecha =  fecha = models.DateField(default=datetime.date.today) 
    autor=models.CharField(max_length=100, null=True, blank=True)


    def __str__(self) -> str:
        if self.categoria:
            return f"{self.categoria} - {self.nombre}"
        else:
            return self.nombre

    class Meta:
        unique_together = ("categoria", "nombre")
