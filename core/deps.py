from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session


async def pegar_sessao() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()
