from django.db import models

# Create your models here.
class Colaborador(models.Model):
    rutColaborador = models.CharField(primary_key=True, max_length=12 ,verbose_name='Rut de Colaborador')
    imagen = models.ImageField(upload_to='img', verbose_name='Foto de identificacion')
    nombreCompleto = models.CharField(max_length=70, verbose_name='Nombre Completo')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=70, verbose_name='Direccion')
    email = models.EmailField(max_length=70, verbose_name='Email')
    pais = models.CharField(max_length=20, verbose_name='Pais')  
    contraseña = models.CharField(max_length=15, verbose_name='Contrasena') 
           
    def __str__(self):
        return self.rutColaborador