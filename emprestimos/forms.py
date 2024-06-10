from django import forms
from .models import Emprestimo, Livro, Usuario

class EmprestimoForm(forms.ModelForm):
    livro = forms.ModelChoiceField(queryset=Livro.objects.none(), empty_label=None)
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), empty_label=None)
    
    class Meta:
        model = Emprestimo
        fields = ['livro', 'data_emprestimo', 'data_devolucao', 'usuario']

    def __init__(self, *args, **kwargs):
        super(EmprestimoForm, self).__init__(*args, **kwargs)
        # Obter IDs dos livros que estão atualmente emprestados e não devolvidos
        livros_emprestados = Emprestimo.objects.filter(data_devolucao__isnull=False).values_list('livro_id', flat=True)
        # Excluir livros emprestados do queryset
        self.fields['livro'].queryset = Livro.objects.exclude(id__in=livros_emprestados)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'telefone', 'cpf']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'descricao']
