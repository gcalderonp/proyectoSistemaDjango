from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class libro(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='libros/', null=True)
    descripcion = models.CharField(max_length=250 , null=True)

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'

    def __str__(self):
        return '{}'.format(self.titulo)