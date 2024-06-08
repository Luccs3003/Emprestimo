from django import forms
from .models import Emprestimo, Livro, Usuario

class EmprestimoForm(forms.ModelForm):
    livro_titulo = forms.ModelChoiceField(queryset=Livro.objects.all(), to_field_name='titulo', empty_label=None)

    class Meta:
        model = Emprestimo
        fields = ['livro_titulo', 'data_emprestimo', 'data_devolucao', 'emprestado_para']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'telefone', 'cpf']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'descricao']
