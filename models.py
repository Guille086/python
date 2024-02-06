from django.db import models

class Usuario(models.Model):
    nickname = models.CharField(primary_key=True,max_length=20)
    nombre_apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Genero(models.Model):
        id = models.AutoField(primary_key=True)
        descripcion = models.CharField(max_length=100)

class Cancion(models.Model):
       id = models.AutoField(primary_key=True)
       nombre = models.CharField(max_length=100)
       autor = models.CharField(max_length=100)
       genero = models.ForeignKey(Genero, on_delete= models.CASCADE)
       usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)


class ListaReproduccion(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)


class ListaCancion(models.Model):
    id = models.AutoField(primary_key=True)
    lista_reproduccion = models.ForeignKey(ListaReproduccion, on_delete= models.CASCADE)