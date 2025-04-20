# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Dirección de la base de datos (SQLite local)
DATABASE_URL = "sqlite:///./vuelos.db"

# Crear el motor de conexión
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear sesión de conexión a la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declaración base para los modelos (Vuelo en este caso)
Base = declarative_base()
