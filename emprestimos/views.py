from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests, rest_framework

from emprestimos.serializers import LivroSerializer, UsuarioSerializer
from .models import Emprestimo, Livro, Usuario
from .forms import EmprestimoForm, UsuarioForm

def lista_emprestimos(request):
    emprestimos = Emprestimo.objects.select_related('livro', 'usuario').all()
    return render(request, 'emprestimos/lista_emprestimos.html', {'emprestimos': emprestimos})



def adicionar_emprestimo(request):
    # Chama a função para obter e salvar os livros quando o formulário for renderizado
    IntegracaoAPIFacade.obter_e_salvar_livros()
    IntegracaoAPIFacade.obter_e_salvar_usuarios()

    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_emprestimos')
    else:
        form = EmprestimoForm()
    
    context = {'form': form}
    return render(request, 'emprestimos/adicionar_emprestimo.html', context)


def emprestimos_json(request):
    emprestimos = Emprestimo.objects.all()
    data = [
        {
            'id_livro': emprestimo.livro.id,
            'titulo_livro': emprestimo.livro.titulo,
            'data_emprestimo': emprestimo.data_emprestimo,
            'data_devolucao': emprestimo.data_devolucao,
            'emprestado_para': emprestimo.usuario.nome,
            'id_usuario': emprestimo.usuario.id,
        }
        for emprestimo in emprestimos
    ]
    return JsonResponse(data, safe=False)


class IntegracaoAPIFacade:
    @staticmethod
    def obter_e_salvar_usuarios():
        try:
            response = requests.get('https://cadastrocliente-production.up.railway.app/api/usuarios')
            response.raise_for_status()  # Verifica se houve algum erro na requisição

            users_json = response.json()  # Converte a resposta para JSON

            # Para cada usuário na resposta da API
            for user_data in users_json:
                cpf = user_data.get('cpf')  # Obtenha o CPF do usuário da API
                # Verifique se o usuário já existe no banco de dados pelo CPF
                existing_user = Usuario.objects.filter(cpf=cpf).first()
                if existing_user:
                    # Se o usuário já existir, atualize os detalhes do usuário
                    serializer = UsuarioSerializer(existing_user, data=user_data)
                else:
                    # Se o usuário não existir, crie um novo registro
                    serializer = UsuarioSerializer(data=user_data)

                if serializer.is_valid():
                    serializer.save()
        except requests.RequestException as e:
            # Em caso de erro na requisição, exibe uma mensagem de erro ou log
            print('Erro ao obter os usuários da API:', e)


    @staticmethod
    def obter_e_salvar_livros():
        try:
            response = requests.get('https://cadastro-livros.onrender.com/biblioteca/listar_livros/')
            response.raise_for_status()  # Verifica se houve algum erro na requisição

            livros_json = response.json()  # Converte a resposta para JSON

            # Para cada livro na resposta da API
            for livro_data in livros_json:
                isbn = livro_data.get('isbn')  # Obtenha o ISBN do livro da API
                # Verifique se o livro já existe no banco de dados pelo ISBN
                existing_livro = Livro.objects.filter(isbn=isbn).first()
                if existing_livro:
                    # Se o livro já existir, atualize os detalhes do livro
                    serializer = LivroSerializer(existing_livro, data=livro_data)
                else:
                    # Se o livro não existir, crie um novo registro
                    serializer = LivroSerializer(data=livro_data)

                if serializer.is_valid():
                    serializer.save()
        except requests.RequestException as e:
            # Em caso de erro na requisição, exibe uma mensagem de erro ou log
            print('Erro ao obter os livros da API:', e)
