from pydantic import BaseModel, field_validator
from typing import Optional


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    valor: float

    @field_validator("nome")
    def nome_nao_vazio(cls, valor):
        palavras = valor.split(" ")
        if len(palavras) < 3:
            raise ValueError("O produto deve ter no mínimo 3 palavras no nome")
        if not valor.istitle():
            raise ValueError("o valor de cada palavra deve começar com letra maiúscula")
        return valor
    

produtos = {

    1: {
        "nome": "celular",
        "valor": 2000
    },

    2: {
        "nome": "notebook",
        "valor": 5000
    }

}