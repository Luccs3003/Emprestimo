from django import forms
from .models import Emprestimo, Livro, Usuario

class EmprestimoForm(forms.ModelForm):
    livro = forms.ModelChoiceField(queryset=Livro.objects.all(), empty_label=None)
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), empty_label=None)
    
    class Meta:
        model = Emprestimo
        fields = ['livro', 'data_emprestimo', 'data_devolucao', 'usuario']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'telefone', 'cpf']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'descricao']
