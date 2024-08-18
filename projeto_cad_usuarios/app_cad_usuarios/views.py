from django.shortcuts import render, redirect
from django.core.management import call_command
from .models import Usuario

#função 
def home(request):
    return render(request, 'usuarios/home.html') #renderiza a página

def usuarios(request): 
    if request.method == 'POST':
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

def limpar_banco(request):
    if request.method == 'POST':
        # Executa o comando flush para limpar o banco de dados
        call_command('flush', '--noinput')
        # Executa as migrações para recriar as tabelas do banco de dados
        call_command('migrate')
        # (Opcional) Executa um script de seed para popular o banco de dados
        # call_command('loaddata', 'initial_data.json')
        
        # Redireciona de volta para a página de usuários
        return redirect('listagem_usuarios')