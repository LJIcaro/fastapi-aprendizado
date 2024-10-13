from typing import Union, List, Any, Dict
from fastapi import FastAPI
from fastapi import status
from fastapi import Response
from fastapi import Path
from fastapi import Header
from fastapi import Depends
from fastapi import HTTPException
from models import Produto, produtos
from time import sleep


app = FastAPI(
    title="API de Produtos - Simulação",
    version="0.0.1",
    description="API de produtos para simular um CRUD voltada para estudos",)


def falso_db():
    try:
        print("Abrindo a conexão com o banco de dados")
        sleep(1)
    finally:
        print("Fechando a conexão com o banco de dados")
        sleep(1)




@app.get('/produtos/{id_produtos}',
        description="Retorna um produto específico",
        summary="Listar um produto",
        response_model = Produto)
async def listar_produtos_por_id(id_produtos: int, db: Any = Depends(falso_db)):
    try:
        produto = produtos[id_produtos]
        return produto
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"O Produto com {id_produtos} não foi encontrado, verifique o id novamente")
    

@app.get('/produtos', 
        description="Retorna todos os produtos ou uma lista vazia",
        summary="Listar todos os produtos")
async def listar_todos_produtos(cabecalho: str = Header(default=None), db: Any = Depends(falso_db)):
        return produtos
    

@app.post('/produtos', 
        description="Cadastra um novo produto",
        summary="Cadastrar um produto")
async def cadastrar_produtos(produto: Produto, db: Any = Depends(falso_db)):
    # Verifica se já existe um produto com o mesmo nome e valor
    for existe in produtos.values():
        if existe['nome'] == produto.nome and existe['valor'] == produto.valor:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um produto com o mesmo nome e valor"
            )

    # Verifica se o id do produto já existe
    if produto.id not in produtos:
        if produtos:
            novo_id = max(produtos.keys()) + 1
        else:
            novo_id = 1
        produtos[novo_id] = produto.model_dump()
        return {"sucesso": f"O produto {produto.nome} com id {novo_id} foi cadastrado!"}
    else: 
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Já existe um produto com esse id"
        )
    

@app.put('/produtos/{id_produtos}',
        description="Atualiza um produto",
        summary="Atualizar um produto")
async def atualizar_produto(id_produtos: int, produto: Produto, db: Any = Depends(falso_db)):
    if id_produtos in produtos:
        produtos[id_produtos] = produto.model_dump()
        return {"message": f"Produto {produto.nome}; id {id_produtos} atualizado com sucesso", "produto": produtos[id_produtos]}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto com id {id_produtos} não encontrado"
        )

     
@app.delete('/produtos/{id_produtos}', 
            description="Deleta um produto", 
            summary="Deletar um produto")
async def deletar_produtos(id_produtos: int, response: Response, db: Any = Depends(falso_db)):
     if id_produtos in produtos:
        produto_removido = produtos[id_produtos]
        del produtos[id_produtos]
        return {"Sucesso": f"O produto {produto_removido["nome"]}; id {id_produtos} foi removido!"}
     else:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe produto com o id {id_produtos}"
          )
     

