from django.shortcuts import render, redirect,  get_object_or_404
from django.views import View
# Create your views here.
from django.http import Http404, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from .models import Solicitante, Usuario, Evento, Cita
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from builtins import print
from django.shortcuts import get_object_or_404
from .forms import UsuarioForm
from datetime import datetime
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage

def index(request):
    return render(request,'index.html')

def arte_cultura(request):
    return render(request, 'arte_cultura.html')

def apoyos(request):
    return render(request, 'Apoyos_Sena.html')

def deportes(request):
    return render(request, 'deportes.html')

def enfermeria(request):
    return render(request, 'enfermeria.html')

def psicosocial(request):
    return render(request, 'psicosocial.html')

def liderazgo(request):
    return render(request, 'liderazgo.html')

def miperfil_bienestar(request):
    return render(request, 'miperfil_bienestar.html')

def usuarios_bienestar(request):
    usuarios = Usuario.objects.filter(tipo_usuario='usuario_bienestar')
    return render(request, 'usuarios_bienestar.html', {'usuarios': usuarios})
    
def registrar(request):
    if request.method == 'POST':
        tipo_usuario = request.POST['tipo_usuario']
        tipo_documento = request.POST['tipo_documento']
        numero_documento = request.POST['numero_documento']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        celular = request.POST['celular']
        correo_sena = request.POST['correo_sena']
        area_bienestar = request.POST['area_bienestar']
        contraseña = request.POST['contraseña']
        
        registro = Usuario.objects.create(
           tipo_usuario= tipo_usuario,  # Asignar el valor correcto a 'tipo_usuario'
           tipo_documento=tipo_documento,
           numero_documento=numero_documento,
           nombres=nombres,
           apellidos=apellidos,
           celular=celular,
           correo_sena=correo_sena,
           area_bienestar=area_bienestar,
           contrasena=contraseña,
        )
        registro.save()
        success_message = "El usuario se ha creado exitosamente."
        return render(request, 'registrar.html', {'success_message': success_message})
    else:
        return render(request, 'registrar.html')
   

def registrar_bienestar(request):
    if request.method == 'POST':
        tipo_documento = request.POST['tipo_documento']
        numero_documento = request.POST['numero_documento']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        celular = request.POST['celular']
        if celular < 10 or celular > 12:
            mesage = "El numero debe tener 10 numeros"
        correo_sena = request.POST['correo_sena']
        area_bienestar = request.POST['area_bienestar']
        contrasena = request.POST['contrasena']
        
        registro = Usuario.objects.create(
           tipo_documento = tipo_documento,
           numero_documento = numero_documento,
           nombres= nombres,
           apellidos = apellidos,
           celular = celular,
           correo_sena = correo_sena,
           area_bienestar = area_bienestar,
           contrasena = contrasena,
        )
        registro.save()
        success_message = "El usuario de bienestar se a creado exitosamente."
        return render(request, 'registrar_bienestar.html', {'success_message': success_message}, {'success_message': mesage})
    else:
        return render(request, 'registrar_bienestar.html')


def formulario(request):
    mensaje_error = None
    mensaje_exito = None

    if request.method == 'POST':

        if form.is_valid():
            solicitud = form.save(commit=False)
            area_bienestar = solicitud.area_bienestar

            # Busca el usuario en base al área de bienestar seleccionada
            try:
                usuario = usuario.objects.get(area_bienestar=area_bienestar)
            except usuario.DoesNotExist:
                usuario = None

            if usuario:
                # Crear una instancia de Solicitante relacionada con el Usuario encontrado
                solicitante = Solicitante.objects.create(
                    nombre_solicitante=form.cleaned_data['nombre_solicitante'],
                    programa_formacion=form.cleaned_data['programa_formacion'],
                    numero_ficha=form.cleaned_data['numero_ficha'],
                    celular=form.cleaned_data['celular'],
                    correo_sena=form.cleaned_data['correo_sena'],
                    area_bienestar=area_bienestar,
                )

                mensaje_exito = 'La solicitud de cita se ha registrado correctamente.'

                # Envío de correos electrónicos a usuario del área y al aprendiz
                # (Código para enviar correos)

            else:
                mensaje_error = 'No se encontró ningún usuario en el área de bienestar seleccionada.'
        else:
            mensaje_error = 'Por favor, corrija los errores en el formulario.'

    return render(request, 'formulario.html', {'form': form, 'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})


def login(request):
    if request.method == 'POST':
        try:
            usuario_logeado = Usuario.objects.get(numero_documento=request.POST['numero_documento'], contrasena=request.POST['contrasena'])
            if usuario_logeado.tipo_usuario == 'super_administrador':
                return redirect('super_administrador')
            elif usuario_logeado.tipo_usuario == 'administrador':
                return render(request, 'administrador.html', {'usuario_logeado': usuario_logeado})
            elif usuario_logeado.tipo_usuario == 'bienestar': 
                return redirect('bienestar')
        except Usuario.DoesNotExist as e:
            error_message = "El funcionamiento es inválido"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def super_administrador(request):
    return render(request, 'super_administrador.html')

def administrador(request):
    return render(request, 'administrador.html')

def bienestar(request):
    return render(request, 'bienestar.html')

def citass(request):
    if request.method == 'POST':
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        estado_cita = request.POST['estado_cita']
        
        # Buscar el objeto Solicitante en función del ID
        solicitante = Solicitante.objects.first()
        usuario = request.user
    
        # Crea una instancia de Cita con los datos proporcionados
        cita_aceptada = Cita.objects.create(
            fecha=fecha,
            hora=hora,
            estado_cita=estado_cita,
        )
        cita_aceptada.save()
        # Puedes redirigir al usuario a una página de éxito o mostrar un mensaje de éxito.
        return redirect('citas')  # Redirige a la página de citas después de guardar la cita.
    solicitantes = Solicitante.objects.all()
    return render(request, 'citas.html', {'citas': solicitantes})
    
def usuarios_listar(request,id):
    if request.method == "POST":
        # Verifica si se ha enviado un formulario para eliminar un usuario.
        id = request.POST.get("eliminar_usuario")
        if id:
            try:
                usuario_a_eliminar = Usuario.objects.get(pk=id)
                usuario_a_eliminar.delete()
                # Redirige a la misma página después de la eliminación o a donde desees.
                return redirect('usuarios_listar')
            except Usuario.DoesNotExist:
                # Maneja el caso en el que el usuario no existe.
                pass
    # Obtiene la lista de usuarios.
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios_listar.html', {'usuarios': usuarios})
    
def miperfil(request):
    usuario_logeado = None
    if 'contrasena' in request.POST: 
        contrasena = request.POST['contrasena']
        nueva_contraseña = request.POST['nueva_contraseña']
        confirmacion = request.POST['confirmacion']
        try: 
            usuario_logeado = Usuario.objects.get(nombres = request.POST['nombres'], apellidos = request.POST['apellidos'], tipo_documento = request.POST['tipo_documento'], numero_documento = request.POST['numero_documento'], celular = request.POST['celular'], correo_sena = request.POST['correo_sena'])
            
            info = get_object_or_404(Usuario, contrasena=contrasena)
            if contrasena == info.contrasena:
                if contrasena == nueva_contraseña:
                    error_message = "La contraseña no puede ser igual a la anterior"
                    return render(request, 'miperfil.html', {'error_message': error_message})
                elif nueva_contraseña == confirmacion:
                    succes_message = "Actualización exitosa."
                    info.contrasena=nueva_contraseña
                    info.save()
                    return render(request, 'miperfil.html', {'succes_message': succes_message})
                else:
                    error_message = "La nueva contrasena y la confirmacion no coinciden"
                    return render(request, 'miperfil.html', {'error_message': error_message})
            else:
                error_message = "No coindice con la contraseña anterior"
                return render(request, 'miperfil.html', {'error_message': error_message})
        except Usuario.DoesNotExist:
            mensaje_error = "No se encontró el usuario."
            return render(request, 'miperfil.html', {'mensaje_error': mensaje_error})
        
    
    return render(request, 'miperfil.html')


def editarUsuario(request, id):
    user = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('usuarios_listar')
    else:
        form = UsuarioForm(instance=user)

    return render(request, 'editarUsuario.html', {'form': form, 'user': user})


def correo(request):
    if request.method=="POST":
        fecha=request.POST.get("Fecha")
        email=request.POST.get("campoHora")

        email=EmailMessage("Mensaje de app Django",
        "Mensaje de prueba :\n\n {}".format(fecha), 
        '',
        [email], 
        reply_to=[email])

        try:
            email.send()

            return render(request, "correo.html", {'valido': True})  # Envío exitoso, mostrar mensaje

        except:
            return render(request, "correo.html", {'error': True})  # Error al enviar, mostrar mensaje de error

    return render(request, "correo.html")
        


@login_required
def rechazar_cita(request):
    if request.method == 'POST':
        try:
            usuario_autenticado = request.user
            id = usuario_autenticado.id

            solicitante = get_object_or_404(Solicitante)

            Cita.estado_cita = 'cancelada'
            Cita.fecha = None
            Cita.hora = None
            Cita.save()

            return JsonResponse({'success': True, 'message': 'La cita ha sido rechazada y actualizada en la base de datos.'})

        except Solicitante.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El solicitante no existe.'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})

    return HttpResponse('Solicitud no válida')
