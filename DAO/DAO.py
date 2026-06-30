# Arquivo: DAO.py
import json
import os

class DAO:
    arquivo = ""
    objetos = []
    classe_modelo = None

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def atualizar(cls, obj_atualizado):
        cls.abrir()
        for i, obj in enumerate(cls.objetos):
            if obj.id == obj_atualizado.id:
                cls.objetos[i] = obj_atualizado
                break
        cls.salvar()

    @classmethod
    def excluir(cls, id_obj):
        cls.abrir()
        cls.objetos = [obj for obj in cls.objetos if obj.id != id_obj]
        cls.salvar()

    @classmethod
    def salvar(cls):
        caminho_arquivo = os.path.join("Jsons", cls.arquivo)
        with open(caminho_arquivo, mode="w", encoding="utf-8") as f:
            lista_dicts = [obj.to_dict() for obj in cls.objetos]
            json.dump(lista_dicts, f, indent=4, ensure_ascii=False)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        caminho_arquivo = os.path.join("Jsons", cls.arquivo)
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, mode="r", encoding="utf-8") as f:
                texto = f.read()
                if texto.strip():
                    lista_dicts = json.loads(texto)
                    # Polimorfismo: reconstrói dinamicamente os objetos baseados na classe filha
                    cls.objetos = [cls.classe_modelo.from_dict(d) for d in lista_dicts]