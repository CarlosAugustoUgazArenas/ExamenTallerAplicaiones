from django.shortcuts import get_object_or_404, redirect, render
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm

# Create your views here.


def index(request):
    usuarios = Usuario.objects.all()
    return render(
        request, 'usuarios/index.html',
        {
            'usuarios': usuarios
        }
    )


def detalles_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    return render(
        request, 'usuarios/detalles_usuario.html',
        {
            'usuario': usuario
        }
    )


def crear_nuevo_usuario(request):
    formulario = UsuarioForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        return redirect('indexUsuario')
    else:
        formulario = UsuarioForm()
    return render(request, 'usuarios/crear_nuevo_usuario.html',{'formulario': formulario})


def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)

    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('indexUsuario')
    else:
        usuario_form = UsuarioForm(instance=usuario)

    return render(
        request, 'usuarios/editar_usuario.html',
        {
            'usuario_form': usuario_form
        }
    )


def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)

    if usuario:
        usuario.delete()

    return redirect('indexUsuario')
