from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from core.configs import settings

# Variavel Assincrona para a conexão com o banco de dados (classe settings em core.configs.py)
engine: AsyncEngine = create_async_engine(settings.DB_URL)

# Variavel Assincrona para a abrir e fechar a conexão com o banco de dados com o banco de dados em sí
Session: AsyncSession = sessionmaker(bind=engine,
                                    class_=AsyncSession,
                                    expire_on_commit=False,
                                    autoflush=False,
                                    autocommit=False,)