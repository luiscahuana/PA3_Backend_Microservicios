from sqlalchemy import Column, Integer, String
from .database import Base

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, index=True)
    nombre = Column(String(100))
    creditos = Column(Integer)
    docente = Column(String(100))