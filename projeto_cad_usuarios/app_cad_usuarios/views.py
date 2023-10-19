from django.shortcuts import render
from .models import Usuario

#função 
def home(request):
    return render(request, 'usuarios/home.html') #renderiza a página

def usuarios(request): 
    #Salvando os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    #Exibir todos os novo usuarios já cadastrados em uma nova página
    usuarios = { #Dicionário de dados
        'usuarios': Usuario.objects.all(), #retornando todos os usuários cadastrados
    }

    #Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)