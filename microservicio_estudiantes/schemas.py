from pydantic import BaseModel

# Esquema para crear un estudiante (lo que el usuario envía)
class EstudianteCreate(BaseModel):
    codigo: str
    nombres: str
    apellidos: str
    correo: str
    carrera: str

# Esquema para responder (lo que la API devuelve, incluye el ID)
class EstudianteResponse(EstudianteCreate):
    id: int

    class Config:
        from_attributes = True