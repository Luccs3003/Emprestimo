from rest_framework import serializers
from .models import Emprestimo, Livro, Usuario

class EmprestimoSerializer(serializers.ModelSerializer):
    livro_id = serializers.IntegerField(source='livro.id')
    livro_titulo = serializers.CharField(source='livro.titulo')
    usuario_id = serializers.IntegerField(source='usuario.id')
    emprestado_para = serializers.CharField(source='usuario.nome')
    
    class Meta:
        model = Emprestimo
        fields = ['livro_id', 'livro_titulo', 'data_emprestimo', 'data_devolucao', 'usuario_id', 'emprestado_para']

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'isbn', 'autor', 'descricao']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'endereco', 'telefone', 'cpf']
