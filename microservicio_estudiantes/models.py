from sqlalchemy import Column, Integer, String
from .database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, index=True)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    correo = Column(String(100), unique=True, index=True)
    carrera = Column(String(100))