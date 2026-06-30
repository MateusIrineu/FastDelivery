# Arquivo: Autor.py

class Autor:
    def __init__(self, id_autor: int, nome: str, nacionalidade: str):
        self.id = id_autor
        self.nome = nome
        self.nacionalidade = nacionalidade

    def to_dict(self) -> dict:
        return {"id": self.id, "nome": self.nome, "nacionalidade": self.nacionalidade}

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(dados["id"], dados["nome"], dados["nacionalidade"])