# Arquivo: AutorDAO.py
from DAO.DAO import DAO
from Modules.Autor.Autor import Autor

class AutorDAO(DAO):
    arquivo = "autores.json"
    objetos = []
    classe_modelo = Autor