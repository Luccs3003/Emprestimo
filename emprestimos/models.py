from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Empréstimo de Livro ID {self.livro.id} para {self.usuario.nome}"