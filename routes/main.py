from fastapi import FastAPI
from routes import produtos_router, usuarios_router

app = FastAPI()
app.include_router(produtos_router.api_router, tags=["Produtos"])
app.include_router(usuarios_router.api_router, tags=["Usuarios"])