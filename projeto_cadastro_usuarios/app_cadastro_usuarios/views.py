from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,'usuarios/home.html')

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

    return render(request, 'usuarios/usuarios.html', usuarios)
