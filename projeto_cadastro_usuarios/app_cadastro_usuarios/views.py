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

def edit(request, id_usuario):
    usuario =  Usuario.objects.get(id_usuario=id_usuario)

    return render(request, "usuarios/update.html", {"usuario":usuario})

def delete(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.delete()
    
    return redirect(home)

def update(request, id_usuario):
    new_name = request.POST.get("nome")
    new_age = request.POST.get("idade")
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.nome = new_name
    usuario.idade = new_age
    usuario.save()

    return redirect(home)