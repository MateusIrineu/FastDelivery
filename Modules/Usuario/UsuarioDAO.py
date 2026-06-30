# Arquivo: UsuarioDAO.py
from DAO.DAO import DAO
from Modules.Usuario.Usuario import Usuario

class UsuarioDAO(DAO):
    arquivo = "usuarios.json"
    objetos = []
    classe_modelo = Usuario