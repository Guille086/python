from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime

lista = [12, 45, 78]
def consultar(request,num):
    if num in lista:
        mensaje = "Existe en la lista"
    else:
        mensaje = "No existe en la lista"

    return HttpResponse(mensaje)

def fecha_hora(request):
    now = datetime.datetime.now()
    html = "<h1>Hoy es %s.</h1>" % now
    return HttpResponse(html)

def plantilla_index(request):
    #cargador de plantilla> loader
    plantilla = loader.get_template('index.html')
    pr = plantilla.render()
    return HttpResponse(pr)

def plantilla_login(request):
    return render(request,'login.html')