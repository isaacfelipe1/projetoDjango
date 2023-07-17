from django.shortcuts import render

from .models  import Usuarios


# Create your views here.


def home(request):

    return render(request,'usuarios/home.html')


def usuarios(request):

    #salvar os dados da tela para o banco de dados

    novo_usuario=Usuarios()

    novo_usuario.nome=request.POST.get('nome')

    novo_usuario.idade=request.POST.get('idade')

    novo_usuario.save()


    #Exibir todos os Usuários já cadastrado em uma nova Página

    usuarios={

        'usuarios':Usuarios.objects.all()


    }

    #retornar os dados para a página de listagem em uma nova página

    return render(request,'usuarios/usuarios.html', usuarios)