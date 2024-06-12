from abc import ABC, abstractmethod

class EmprestimoComponent(ABC):
    @abstractmethod
    def emprestar(self, emprestimo):
        pass

class ConcreteEmprestimo(EmprestimoComponent):
    def emprestar(self, emprestimo):
        emprestimo.save()

class EmprestimoDecorator(EmprestimoComponent):
    def __init__(self, component: EmprestimoComponent):
        self._component = component

    @abstractmethod
    def emprestar(self, emprestimo):
        return self._component.emprestar(emprestimo)

class LogEmprestimoDecorator(EmprestimoDecorator):
    def emprestar(self, emprestimo):
        print(f"Emprestando livro: {emprestimo.livro.titulo} para {emprestimo.usuario.nome}")
        super().emprestar(emprestimo)
        print(f"Livro {emprestimo.livro.titulo} emprestado com sucesso.")
