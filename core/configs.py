from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from sqlalchemy.orm import declarative_base
from typing import List, ClassVar

class Settings(BaseSettings):
    # Configurações gerais usadas em todo o projeto
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:ljicaro1@localhost:5432/loja"
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()   


