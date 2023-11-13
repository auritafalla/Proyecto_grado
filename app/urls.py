from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('arte_cultura/', views.arte_cultura, name='arte_cultura'),
    path('deportes/', views.deportes, name='deportes'),
    path('apoyos/', views.apoyos, name='apoyos'),
    path('enfermeria/', views.enfermeria, name='enfermeria'),
    path('psicosocial/', views.psicosocial, name='psicosocial'),
    path('liderazgo/', views.liderazgo, name='liderazgo'),
    path('formulario/', views.formulario, name='formulario'),
    path('login/', views.login, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('registrar_bienestar/', views.registrar_bienestar, name='registrar_bienestar'),
    path('super_administrador/', views.super_administrador, name='super_administrador'),
    path('administrador/', views.administrador, name='administrador'),
    path('bienestar/', views.bienestar, name='bienestar'),
    path('usuarios_listar/', views.usuarios_listar, name='usuarios_listar'),
    path('usuarios_bienestar/', views.usuarios_bienestar, name='usuarios_bienestar'),
    path('citas/', views.citass, name='citas'),
    path('miperfil/', views.miperfil, name='miperfil'),
    path('miperfil_bienestar/', views.miperfil_bienestar, name='miperfil_bienestar'),
    path('editarUsuario/<int:id>/', views.editarUsuario, name='editarUsuario'),
    path("mail", views.correo, name="email"),
    path('rechazar_cita/<int:id>/', views.rechazar_cita, name='rechazar_cita'),
]