from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    valor: float

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