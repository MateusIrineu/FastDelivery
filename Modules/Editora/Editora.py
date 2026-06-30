# Arquivo: Editora.py

class Editora:
    def __init__(self, id_editora: int, nome: str, cidade: str):
        self.id = id_editora
        self.nome = nome
        self.cidade = cidade

    def to_dict(self) -> dict:
        return {"id": self.id, "nome": self.nome, "cidade": self.cidade}

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(dados["id"], dados["nome"], dados["cidade"])