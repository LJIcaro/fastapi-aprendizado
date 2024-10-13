from fastapi import APIRouter

api_router = APIRouter()
@api_router.get('/usuarios/')
async def listar_todos_usuarios():
    return {"Info": "Listando todos os usuarios"}
