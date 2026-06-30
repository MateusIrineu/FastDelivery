# Arquivo: Emprestimo.py

class Emprestimo:
    def __init__(self, id_emprestimo: int, id_livro: int, id_usuario: int, data_retirada: str, ativo: bool = True):
        self.id = id_emprestimo
        self.id_livro = id_livro       # Associação com Livro
        self.id_usuario = id_usuario   # Associação com Usuário
        self.data_retirada = data_retirada
        self.ativo = ativo

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "id_livro": self.id_livro,
            "id_usuario": self.id_usuario,
            "data_retirada": self.data_retirada,
            "ativo": self.ativo
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(dados["id"], dados["id_livro"], dados["id_usuario"], dados["data_retirada"], dados["ativo"])