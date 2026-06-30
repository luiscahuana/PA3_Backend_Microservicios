from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, database

# Crea la tabla en SQL Server automáticamente
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Microservicio de Cursos",
    description="API RESTful para la gestión de cursos de la Universidad Tecnológica XYZ",
    version="1.0.0"
)

# --- ENDPOINTS CRUD ---

@app.get("/cursos/", response_model=List[schemas.CursoResponse], tags=["Cursos"])
def listar_cursos(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    cursos = db.query(models.Curso).offset(skip).limit(limit).all()
    return cursos

@app.get("/cursos/{curso_id}", response_model=schemas.CursoResponse, tags=["Cursos"])
def consultar_curso(curso_id: int, db: Session = Depends(database.get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

@app.post("/cursos/", response_model=schemas.CursoResponse, tags=["Cursos"])
def registrar_curso(curso: schemas.CursoCreate, db: Session = Depends(database.get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.codigo == curso.codigo).first()
    if db_curso:
        raise HTTPException(status_code=400, detail="El código de curso ya está registrado")
    
    nuevo_curso = models.Curso(**curso.model_dump())
    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)
    return nuevo_curso

@app.put("/cursos/{curso_id}", response_model=schemas.CursoResponse, tags=["Cursos"])
def actualizar_curso(curso_id: int, curso_actualizado: schemas.CursoCreate, db: Session = Depends(database.get_db)):
    curso_db = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso_db:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    for key, value in curso_actualizado.model_dump().items():
        setattr(curso_db, key, value)
        
    db.commit()
    db.refresh(curso_db)
    return curso_db

@app.delete("/cursos/{curso_id}", tags=["Cursos"])
def eliminar_curso(curso_id: int, db: Session = Depends(database.get_db)):
    curso_db = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso_db:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    db.delete(curso_db)
    db.commit()
    return {"mensaje": "Curso eliminado correctamente"}