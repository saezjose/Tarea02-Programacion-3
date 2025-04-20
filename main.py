# main.py

#para ejecutar la fast api utiliza#

#python -m uvicorn main:app --reload#

#en http://localhost:8000/docs #


from fastapi import FastAPI, HTTPException
from database import engine
from models import Base
from vuelos import (
    crear_vuelo,
    insertar_en_posicion,
    eliminar_vuelo,
    obtener_vuelos,
    obtener_primero,
    obtener_ultimo,
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestión de Vuelos - Lista Doblemente Enlazada")


@app.post("/vuelos/emergencia")
def agregar_emergencia(codigo: str, destino: str):
    return crear_vuelo(codigo=codigo, destino=destino, prioridad="emergencia")

@app.post("/vuelos/regular")
def agregar_regular(codigo: str, destino: str):
    return crear_vuelo(codigo=codigo, destino=destino, prioridad="regular")


@app.post("/vuelos/insertar/{posicion}")
def insertar_en_pos(posicion: int, codigo: str, destino: str, prioridad: str = "regular"):
    return insertar_en_posicion(codigo, destino, prioridad, posicion)


@app.delete("/vuelos/{posicion}")
def eliminar(posicion: int):
    vuelo = eliminar_vuelo(posicion)
    if vuelo is None:
        raise HTTPException(status_code=404, detail="No se encontró un vuelo en esa posición")
    return {"mensaje": "Vuelo eliminado", "codigo": vuelo.codigo}

@app.get("/vuelos")
def listar():
    return obtener_vuelos()


@app.get("/vuelos/primero")
def primero():
    vuelo = obtener_primero()
    if vuelo is None:
        raise HTTPException(status_code=404, detail="No hay vuelos en la lista")
    return vuelo


@app.get("/vuelos/ultimo")
def ultimo():
    vuelo = obtener_ultimo()
    if vuelo is None:
        raise HTTPException(status_code=404, detail="No hay vuelos en la lista")
    return vuelo
