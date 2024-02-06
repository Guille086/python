from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.inicio),
    path('login/', views.login),
    path('autenticar/', views.autenticar),
    path('agregarcancion/', views.agregar_cancion),
]