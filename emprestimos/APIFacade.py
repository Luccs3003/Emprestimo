import requests
from emprestimos.models import Emprestimo, Livro, Usuario
from emprestimos.serializers import LivroSerializer, UsuarioSerializer


class IntegracaoAPIFacade:
    @staticmethod
    def obter_e_salvar_usuarios():
        try:
            response = requests.get('https://cadastrocliente-production.up.railway.app/api/usuarios')
            response.raise_for_status()  # Verifica se houve algum erro na requisição

            users_json = response.json()  # Converte a resposta para JSON

            # Para cada usuário na resposta da API
            for user_data in users_json:
                cpf = user_data.get('cpf')  # Obtenha o CPF do usuário da API
                # Verifique se o usuário já existe no banco de dados pelo CPF
                existing_user = Usuario.objects.filter(cpf=cpf).first()
                if existing_user:
                    # Se o usuário já existir, atualize os detalhes do usuário
                    serializer = UsuarioSerializer(existing_user, data=user_data)
                else:
                    # Se o usuário não existir, crie um novo registro
                    serializer = UsuarioSerializer(data=user_data)

                if serializer.is_valid():
                    serializer.save()
        except requests.RequestException as e:
            # Em caso de erro na requisição, exibe uma mensagem de erro ou log
            print('Erro ao obter os usuários da API:', e)


    @staticmethod
    def obter_e_salvar_livros():
        try:
            response = requests.get('https://cadastro-livros.onrender.com/biblioteca/listar_livros/')
            response.raise_for_status()  # Verifica se houve algum erro na requisição

            livros_json = response.json()  # Converte a resposta para JSON

            # Para cada livro na resposta da API
            for livro_data in livros_json:
                isbn = livro_data.get('isbn')  # Obtenha o ISBN do livro da API
                # Verifique se o livro já existe no banco de dados pelo ISBN
                existing_livro = Livro.objects.filter(isbn=isbn).first()
                if existing_livro:
                    # Se o livro já existir, atualize os detalhes do livro
                    serializer = LivroSerializer(existing_livro, data=livro_data)
                else:
                    # Se o livro não existir, crie um novo registro
                    serializer = LivroSerializer(data=livro_data)

                if serializer.is_valid():
                    serializer.save()
        except requests.RequestException as e:
            # Em caso de erro na requisição, exibe uma mensagem de erro ou log
            print('Erro ao obter os livros da API:', e)


    @staticmethod
    def sincronizar_devolucoes():
        try:
            response = requests.get('https://devolucao-production.up.railway.app/emprestimos/json')
            response.raise_for_status()
            devolucoes_json = response.json()

            for devolucao in devolucoes_json:
                if devolucao['mensagensEstado'] == "Devolução concluída.":
                    livro_id = devolucao['idLivro']
                    try:
                        emprestimo = Emprestimo.objects.get(livro_id=livro_id, data_devolucao__isnull=False)
                        emprestimo.delete()
                    except Emprestimo.DoesNotExist:
                        continue  # Se o empréstimo não existir, continue para o próximo
        
            print("Sincronização de devoluções concluída.")
        except requests.RequestException as e:
            print(f'Erro ao sincronizar devoluções: {e}')
