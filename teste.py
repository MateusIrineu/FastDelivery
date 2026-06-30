# Arquivo: teste.py
from Modules.Categoria.CategoriaDAO import CategoriaDAO
from Modules.Categoria.Categoria import Categoria
from Modules.Autor.AutorDAO import AutorDAO
from Modules.Autor.Autor import Autor
from Modules.Editora.EditoraDAO import EditoraDAO
from Modules.Editora.Editora import Editora
from Modules.Livro.LivroDAO import LivroDAO
from Modules.Livro.Livro import Livro
from Modules.Usuario.UsuarioDAO import UsuarioDAO
from Modules.Usuario.Usuario import Usuario
from Modules.Emprestimo.EmprestimoDAO import EmprestimoDAO
from Modules.Emprestimo.Emprestimo import Emprestimo

if __name__ == "__main__":
    print("====== INICIANDO SISTEMA DE BIBLIOTECA (BIBLIOTECH) ======\n")

    # 1. Populando Cadastros Básicos (CRUD - Inserir)
    cat = Categoria(1, "Fantasia Épica")
    CategoriaDAO.inserir(cat)

    aut = Autor(50, "J.R.R. Tolkien", "Britânico")
    AutorDAO.inserir(aut)

    edi = Editora(900, "HarperCollins", "São Paulo")
    EditoraDAO.inserir(edi)

    user = Usuario(10, "Gabriel Medeiros", "gabriel@email.com", "1234", "leitor")
    UsuarioDAO.inserir(user)
    
    print("✓ Entidades base inseridas e arquivos JSON criados com sucesso.")

    # 2. Cadastro do Livro (Aplicando as Associações 1:N passando os IDs cadastrados)
    livro = Livro(id_livro=101, titulo="O Senhor dos Anéis", id_categoria=1, id_autor=50, id_editora=900)
    LivroDAO.inserir(livro)
    print("✓ Livro cadastrado com sucesso associando Categoria, Autor e Editora.")

    # 3. Teste do Requisito de Busca Parcial
    print("\n--- TESTANDO PESQUISA PARCIAL DE LIVROS ---")
    resultado_busca = LivroDAO.pesquisar_por_titulo("Senhor")
    for l in resultado_busca:
        print(f" Encontrado: ID {l.id} - Título: '{l.titulo}'")

    # 4. Teste do Requisito de Regra de Negócio (Empréstimo Multi-Entidade)
    print("\n--- TESTANDO REGRA DE NEGÓCIO (REALIZAR EMPRÉSTIMO) ---")
    emp = Emprestimo(id_emprestimo=777, id_livro=101, id_usuario=10, data_retirada="30/06/2026")
    
    # Chama a operação que manipula o EmprestimoDAO e altera o status dentro do LivroDAO simultaneamente
    EmprestimoDAO.registrar_emprestimo(emp)

    # 5. Lendo os dados salvos para comprovar a alteração conjunta
    print("\n--- PROVA DE PERSISTÊNCIA DOS ARQUIVOS ---")
    livro_atualizado = LivroDAO.listar()[0]
    print(f"Status Atual do Livro ID 101 após empréstimo: ['Disponível' = {livro_atualizado.disponivel}]")
    
    historico_emp = EmprestimoDAO.listar()
    print(f"Quantidade de Empréstimos salvos no JSON: {len(historico_emp)}")
    print("\n====== TESTE FINALIZADO COM SUCESSO TOTAL ======")