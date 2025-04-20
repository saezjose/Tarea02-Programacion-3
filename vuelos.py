# vuelos.py

from models import Vuelo
from database import SessionLocal
from TDA_ListaDoblementeEnlazada import ListaDoblementeEnlazada

# Instancia global de la lista enlazada
lista_vuelos = ListaDoblementeEnlazada()

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para crear un vuelo (y guardarlo en la base de datos)
def crear_vuelo(codigo, destino, prioridad):
    db = SessionLocal()
    vuelo = Vuelo(codigo=codigo, destino=destino, prioridad=prioridad)
    db.add(vuelo)
    db.commit()
    db.refresh(vuelo)

    # Insertar en la lista dependiendo de prioridad
    if prioridad.lower() == "emergencia":
        lista_vuelos.insertar_al_frente(vuelo)
    else:
        lista_vuelos.insertar_al_final(vuelo)

    db.close()
    return vuelo

# Insertar vuelo en una posición específica
def insertar_en_posicion(codigo, destino, prioridad, posicion):
    db = SessionLocal()
    vuelo = Vuelo(codigo=codigo, destino=destino, prioridad=prioridad)
    db.add(vuelo)
    db.commit()
    db.refresh(vuelo)

    lista_vuelos.insertar_en_posicion(vuelo, posicion)
    db.close()
    return vuelo

# Extraer vuelo de una posición
def eliminar_vuelo(posicion):
    vuelo = lista_vuelos.extraer_de_posicion(posicion)
    if vuelo is None:
        return None

    db = SessionLocal()
    vuelo_en_bd = db.query(Vuelo).filter(Vuelo.id == vuelo.id).first()
    if vuelo_en_bd:
        db.delete(vuelo_en_bd)
        db.commit()
    db.close()
    return vuelo

# Obtener todos los vuelos en orden
def obtener_vuelos():
    return lista_vuelos.obtener_todos()

# Ver primer vuelo
def obtener_primero():
    return lista_vuelos.obtener_primero()

# Ver último vuelo
def obtener_ultimo():
    return lista_vuelos.obtener_ultimo()

