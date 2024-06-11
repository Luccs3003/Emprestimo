from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests, rest_framework

from emprestimos.APIFacade import IntegracaoAPIFacade
from emprestimos.serializers import LivroSerializer, UsuarioSerializer
from .models import Emprestimo, Livro, Usuario
from .forms import EmprestimoForm, UsuarioForm

def lista_emprestimos(request):
    IntegracaoAPIFacade.sincronizar_devolucoes()

    emprestimos = Emprestimo.objects.select_related('livro', 'usuario').all()
    return render(request, 'emprestimos/lista_emprestimos.html', {'emprestimos': emprestimos})



def adicionar_emprestimo(request):
    IntegracaoAPIFacade.obter_e_salvar_livros()
    IntegracaoAPIFacade.obter_e_salvar_usuarios()

    emprestimos = Emprestimo.objects.all()
    for emprestimo in emprestimos:
        print(f"Empréstimo: {emprestimo}, Data de Devolução: {emprestimo.data_devolucao}")

    livros_emprestados = Emprestimo.objects.filter(data_devolucao__isnull=True).values_list('livro_id', flat=True)
    print(f"Livros emprestados: {list(livros_emprestados)}")  # Adicione este print para debug

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
