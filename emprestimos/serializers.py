from rest_framework import serializers
from .models import Emprestimo, Livro, Usuario

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['livro_titulo', 'data_emprestimo', 'data_devolucao', 'emprestado_para']

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['titulo', 'isbn', 'autor', 'descricao']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'telefone', 'cpf']
