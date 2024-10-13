from fastapi import APIRouter

api_router = APIRouter()

@api_router.get('/produtos/')
async def listar_todos_produtos():
    return {"Info": "Listando todos os produtos"}