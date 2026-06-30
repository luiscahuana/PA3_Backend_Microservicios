from pydantic import BaseModel

class CursoCreate(BaseModel):
    codigo: str
    nombre: str
    creditos: int
    docente: str

class CursoResponse(CursoCreate):
    id: int

    class Config:
        from_attributes = True