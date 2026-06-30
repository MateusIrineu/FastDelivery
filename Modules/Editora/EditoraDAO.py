# Arquivo: EditoraDAO.py
from DAO.DAO import DAO
from Modules.Editora.Editora import Editora

class EditoraDAO(DAO):
    arquivo = "editoras.json"
    objetos = []
    classe_modelo = Editora