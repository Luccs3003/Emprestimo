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
    get_and_save_livros_from_api()
    get_and_save_users_from_api()

    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_emprestimos')
    else:
        form = EmprestimoForm()
    
    context = {'form': form}
    return render(request, 'emprestimos/adicionar_emprestimo.html', context)

#get_usuarios n funcional ainda
def get_and_save_users_from_api():
    try:
        response = requests.get('https://cadastrocliente-production.up.railway.app/api/usuarios')
        response.raise_for_status()  # Verifica se houve algum erro na requisição

        users_json = response.json()  # Converte a resposta para JSON

        # Serializa e salva os usuarios no banco de dados do Django
        for user_data in users_json:
            serializer = UsuarioSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
    except requests.RequestException as e:
        # Em caso de erro na requisição, exibe uma mensagem de erro ou log
        print('Erro ao obter os livros da API:', e)
        

def get_and_save_livros_from_api():
    try:
        response = requests.get('https://cadastro-livros.onrender.com/biblioteca/listar_livros/')
        response.raise_for_status()  # Verifica se houve algum erro na requisição

        livros_json = response.json()  # Converte a resposta para JSON

        # Serializa e salva os livros no banco de dados do Django
        for livro_data in livros_json:
            serializer = LivroSerializer(data=livro_data)
            if serializer.is_valid():
                serializer.save()
    except requests.RequestException as e:
        # Em caso de erro na requisição, exibe uma mensagem de erro ou log
        print('Erro ao obter os livros da API:', e)

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