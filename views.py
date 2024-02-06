from django.shortcuts import render
from django.http import HttpResponse
from .models import Cancion, Usuario, Genero

# Create your views here.
def inicio(request):
    lista_cancion = Cancion.objects.all()
    dicc = {"canciones":lista_cancion,"saludo":"Holaaaa"}
    return render(request,"index.html",dicc)

def login(request):
    return render(request,"login.html")

def autenticar(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']

        if usuario in Usuario.objects.values_list('nickname', flat=True) and password in Usuario.objects.values_list('password', flat=True):
            usuario_autenticado = Usuario.objects.values('nickname','nombre_apellido','email').distinct().filter(nickname = usuario)
            lista_cancion = Cancion.objects.filter(usuario_id = usuario)
            return render(request,"index.html",{'usuario':usuario_autenticado, 'canciones':lista_cancion})
        else:
            return render(request,"login.html")
        
def agregar_cancion(request):
    if request.method == 'POST':
        autor = request.POST['autor']
        titulo = request.POST['titulo']
        genero = request.POST['genero']
        usuario_nick = request.POST['user']

        #Crear un objeto del tipo usuario
        usu = Usuario.objects.get(nickname = usuario_nick)
        gen = Genero.objects.get(id = genero)

        #Crear un objeto del tipo cancion
        cancion = Cancion()
        cancion.autor = autor
        cancion.titulo = titulo
        cancion.genero = gen
        cancion.usuario = usu

        cancion.save()
        usuario_autenticado = Usuario.objects.values('nickname','nombre_apellido','email').distinct().filter(nickname = usuario_nick)
        lista_cancion = Cancion.objects.filter(usuario_id=usuario_nick)
        return render(request,"index.html",{'usuario':usuario_autenticado, 'canciones':lista_cancion})
