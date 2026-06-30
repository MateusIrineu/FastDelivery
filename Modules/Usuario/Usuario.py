# Arquivo: Usuario.py

class Usuario:
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str, perfil: str):
        self.id = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil  # 'admin' (Bibliotecário) ou 'leitor' (Cliente)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "perfil": self.perfil
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(dados["id"], dados["nome"], dados["email"], dados["senha"], dados["perfil"])