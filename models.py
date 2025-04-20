# models.py

from sqlalchemy import Column, Integer, String
from database import Base

class Vuelo(Base):
    __tablename__ = "vuelos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False)  # Ej: LATAM123
    destino = Column(String, nullable=False)              # Ej: Santiago
    prioridad = Column(String, nullable=False)            # Ej: emergencia / regular