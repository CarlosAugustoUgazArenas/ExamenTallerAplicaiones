from django.shortcuts import get_object_or_404, redirect, render
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request) :
    usuario = Usuario.objects.all()
    return render(
        request , 'usuarios/inicio.html' , 
        {
            'usuarios' : usuario
        }
    )
def detalles_usuario(request , id) :
    usuario = get_object_or_404(Usuario , pk = id) 
    return render(
        request , 'usuarios/detalles_usuario.html' ,
        {
            'usuarios' : usuario
        }
    )

def crear_nuevo_usuario(request) :
    if request.method == "POST" :
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid() :
            usuario_form.save()
            return redirect('index')
    else :
        usuario_form = UsuarioForm()

    return render(
        request , 'usuarios/crear_nuevo_usuario.html' ,
        {
            'usuaro_form' : usuario_form
        }
    )

    

def editar_usuario(request , id) :
    usuario = get_object_or_404(Usuario , pk = id)

    if request.method == "POST" :
        usuario_form = UsuarioForm(request.POST , instance = usuario) 
        if usuario_form.is_valid() :
            usuario_form.save()
            return redirect('index')
    else :
        usuario_form = UsuarioForm(instance = usuario)

    return render(
        request , 'usuarios/editar_usuario.html' ,
        {
            'usuario_form' : usuario_form
        }
    )

def eliminar_usuario(request , id) :
    usuario = get_object_or_404(Usuario , pk = id)

    if usuario :
        usuario.delete()

    return redirect('inicio')