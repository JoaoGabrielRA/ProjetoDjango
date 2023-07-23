from django.shortcuts import render, redirect
from .models import Usuario
def home(request):
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    return render(request,'usuarios/home.html', usuarios)

def usuarios(request):
    #salva os dados do form no DB
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibe todos os users cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #retorna os dados para a listagem

    return redirect(home)

def delete(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.delete()
    
    return redirect(home)

