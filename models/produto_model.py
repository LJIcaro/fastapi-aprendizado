from core.configs import settings
from sqlalchemy import Column, Integer, String, Float

class ProdutoModel(settings.DBBaseModel):
    __tablename__ = "produtos"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo: str = Column(String(100))
    descricao: str = Column(String(100))
    valor: float = Column(Float)
 