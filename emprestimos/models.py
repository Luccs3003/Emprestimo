from django.db import models

class Emprestimo(models.Model):
    livro_titulo = models.CharField(max_length=100)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    emprestado_para = models.CharField(max_length=100)

    def __str__(self):
        return f"Empréstimo de Livro ID {self.livro_titulo} para {self.emprestado_para}"

class Livro(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField()
    autor = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo 
    
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)  # Supondo que CPF seja único

    def __str__(self):
        return self.nome
