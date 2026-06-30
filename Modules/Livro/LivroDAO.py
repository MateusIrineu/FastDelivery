# Arquivo: LivroDAO.py
from DAO.DAO import DAO
from Modules.Livro.Livro import Livro

class LivroDAO(DAO):
    arquivo = "livros.json"
    objetos = []
    classe_modelo = Livro

    # ATENDE AO REQUISITO: Operação de Pesquisa Parcial
    @classmethod
    def pesquisar_por_titulo(cls, termo: str):
        cls.abrir()
        return [l for l in cls.objetos if termo.lower() in l.titulo.lower()]