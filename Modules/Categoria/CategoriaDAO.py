# Dentro de Modules/Categoria/CategoriaDAO.py
from DAO.DAO import DAO  # Aponta para a pasta DAO e depois para o arquivo DAO.py
from Modules.Categoria.Categoria import Categoria # Aponta o caminho completo da entidade

class CategoriaDAO(DAO):
    arquivo = "categorias.json"
    objetos = []
    classe_modelo = Categoria