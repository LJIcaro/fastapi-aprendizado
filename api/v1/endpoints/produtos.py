from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.produto_model import ProdutoModel
from schemas.produto_schema import ProdutoSchema
from core.deps import pegar_sessao

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProdutoSchema)
async def criar_produto(produto: ProdutoSchema, db: AsyncSession = Depends(pegar_sessao)):
    novo_produto = ProdutoModel(titulo=produto.titulo,
                                descricao=produto.descricao,
                                valor=produto.valor)
    db.add(novo_produto)
    await db.commit()  
    await db.refresh(novo_produto)
    return novo_produto


@router.get("/", response_model=List[ProdutoSchema], status_code=status.HTTP_200_OK)
async def listar_produtos(db: AsyncSession = Depends(pegar_sessao)):

    async with db as session:
        query = select(ProdutoModel)
        result = await session.execute(query)
        produtos: List[ProdutoModel] = result.scalars().all()
        return produtos


@router.get("/{id_produto}", response_model=ProdutoSchema, status_code=status.HTTP_200_OK)
async def pegar_produto(id_produto: int, db: AsyncSession = Depends(pegar_sessao)):

    async with db as session:
        query = select(ProdutoModel).where(ProdutoModel.id == id_produto)
        result = await session.execute(query)
        produto = result.scalars().first()

        if produto:
            return produto
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")


@router.put("/{id_produto}", response_model=ProdutoSchema, status_code=status.HTTP_200_OK)
async def atualizar_produto(id_produto: int, produto: ProdutoSchema, db: AsyncSession = Depends(pegar_sessao)):

    async with db as session:
        query = select(ProdutoModel).where(ProdutoModel.id == id_produto)
        result = await session.execute(query)
        produto_up = result.scalars().first()

        if produto_up:
            produto_up.titulo = produto.titulo
            produto_up.descricao = produto.descricao
            produto_up.valor = produto.valor

            await db.commit()
            return produto_up
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")


@router.delete("/{id_produto}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_produto(id_produto: int, db: AsyncSession = Depends(pegar_sessao)):

    async with db as session:
        query = select(ProdutoModel).where(ProdutoModel.id == id_produto)
        result = await session.execute(query)
        produto = result.scalars().first()

        if produto:
            await db.delete(produto)
            await db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado ou já deletado, verifique novamente")
        

        

