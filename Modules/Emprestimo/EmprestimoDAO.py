# Arquivo: EmprestimoDAO.py
from DAO.DAO import DAO
from Modules.Emprestimo.Emprestimo import Emprestimo
from Modules.Livro.LivroDAO import LivroDAO

class EmprestimoDAO(DAO):
    arquivo = "emprestimos.json"
    objetos = []
    classe_modelo = Emprestimo

    # ATENDE AO REQUISITO: Regra de negócio complexa envolvendo múltiplas entidades
    @classmethod
    def registrar_emprestimo(cls, novo_emprestimo):
        cls.abrir()
        
        # 1. Busca o livro correspondente via LivroDAO para verificar o estoque/disponibilidade
        livros = LivroDAO.listar()
        livro_encontrado = None
        for l in livros:
            if l.id == novo_emprestimo.id_livro:
                livro_encontrado = l
                break

        # 2. Aplica a Regra de Negócio: Se o livro existe e está disponível, realiza a operação
        if livro_encontrado and livro_encontrado.disponivel:
            # Altera a entidade Livro (Status passa a ser Indisponível)
            livro_encontrado.disponivel = False
            LivroDAO.atualizar(livro_encontrado)
            
            # Insere o novo empréstimo no arquivo correspondente
            cls.inserir(novo_emprestimo)
            print(f"-> SUCESSO: O livro '{livro_encontrado.titulo}' foi emprestado.")
            return True
        else:
            print(f"-> ERRO: Não foi possível emprestar. Livro ocupado ou inexistente.")
            return False