from fastapi import FastAPI
from routers import api

app = FastAPI()

app.include_router(api.router, prefix="", tags=["api"])


@app.get("/")
def root():
    return {"message": "API para detectar número faltante de un conjunto de 1 al 100"}
