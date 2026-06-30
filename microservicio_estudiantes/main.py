from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importamos nuestros archivos locales
from . import models, schemas, database

# ¡Magia pura! Esto le dice a SQLAlchemy que cree las tablas en SQL Server si no existen
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Microservicio de Estudiantes",
    description="API RESTful para la gestión de estudiantes de la Universidad Tecnológica XYZ",
    version="1.0.0"
)

# --- ENDPOINTS CRUD ---

# 1. Listar todos los estudiantes (GET)
@app.get("/estudiantes/", response_model=List[schemas.EstudianteResponse], tags=["Estudiantes"])
def listar_estudiantes(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    estudiantes = db.query(models.Estudiante).offset(skip).limit(limit).all()
    return estudiantes

# 2. Consultar un estudiante por ID (GET)
@app.get("/estudiantes/{estudiante_id}", response_model=schemas.EstudianteResponse, tags=["Estudiantes"])
def consultar_estudiante(estudiante_id: int, db: Session = Depends(database.get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

# 3. Registrar estudiante (POST)
@app.post("/estudiantes/", response_model=schemas.EstudianteResponse, tags=["Estudiantes"])
def registrar_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(database.get_db)):
    # Verificamos que el código no exista ya
    db_estudiante = db.query(models.Estudiante).filter(models.Estudiante.codigo == estudiante.codigo).first()
    if db_estudiante:
        raise HTTPException(status_code=400, detail="El código de estudiante ya está registrado")
    
    nuevo_estudiante = models.Estudiante(**estudiante.model_dump())
    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante)
    return nuevo_estudiante

# 4. Actualizar estudiante (PUT)
@app.put("/estudiantes/{estudiante_id}", response_model=schemas.EstudianteResponse, tags=["Estudiantes"])
def actualizar_estudiante(estudiante_id: int, estudiante_actualizado: schemas.EstudianteCreate, db: Session = Depends(database.get_db)):
    estudiante_db = db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    if estudiante_db is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    
    for key, value in estudiante_actualizado.model_dump().items():
        setattr(estudiante_db, key, value)
        
    db.commit()
    db.refresh(estudiante_db)
    return estudiante_db

# 5. Eliminar estudiante (DELETE)
@app.delete("/estudiantes/{estudiante_id}", tags=["Estudiantes"])
def eliminar_estudiante(estudiante_id: int, db: Session = Depends(database.get_db)):
    estudiante_db = db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    if estudiante_db is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    
    db.delete(estudiante_db)
    db.commit()
    return {"mensaje": "Estudiante eliminado correctamente"}