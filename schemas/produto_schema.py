from typing import Optional
from pydantic import BaseModel as SCBaseModel

class ProdutoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    valor: float

    class Config:
        from_attributes = True