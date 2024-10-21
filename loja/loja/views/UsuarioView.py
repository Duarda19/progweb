from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm
def list_usuario_view(request, id=None):
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
        'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context,status=200)
def edit_usuario_view(request):
    usuario = get_object_or_404(Usuario, user=request.user)
    usuarioForm = UserUsuarioForm(instance=usuario)
    context = {
        'usuarioForm': usuarioForm
    }
    return render(request, template_name='usuario/usuario-edit.html', context=context,status=200) 