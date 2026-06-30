# 🎓 Plataforma Web - Universidad Tecnológica XYZ

Proyecto backend desarrollado con una arquitectura de microservicios para la gestión académica de estudiantes y cursos.

## 👥 Equipo de Desarrollo
* Luis Meliton Flores Cahuana

## 🛠️ Tecnologías Utilizadas
* **Framework Backend:** Python con FastAPI
* **Base de Datos:** SQL Server
* **ORM:** SQLAlchemy
* **Validación de Datos:** Pydantic
* **Testing:** Pytest y TestClient (HTTPX)

## 🏗️ Arquitectura de Microservicios
El proyecto está dividido en dos servicios independientes, cada uno con su propio CRUD RESTful:
1. **Microservicio de Estudiantes:** Gestión de matrículas, datos personales y carreras.
2. **Microservicio de Cursos:** Gestión de malla curricular, docentes y créditos (incluye un Procedimiento Almacenado para el cálculo de créditos totales).

## 🚀 Guía de Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone [https://github.com/luiscahuana/PA3_Backend_Microservicios.git](https://github.com/luiscahuana/PA3_Backend_Microservicios.git)
cd PA3_Backend_Microservicios

2. Crear y activar el entorno virtual
Bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate

3. Instalar dependencias
Bash
pip install -r requirements.txt

4. Configuración de Base de Datos (SQL Server)
Abrir SQL Server Management Studio (SSMS).

Crear la base de datos ejecutando: CREATE DATABASE universidad_xyz; GO

Crear el procedimiento almacenado ejecutando:

SQL
USE universidad_xyz;
GO
CREATE PROCEDURE sp_TotalCreditos
AS
BEGIN
    SELECT ISNULL(SUM(creditos), 0) AS TotalCreditos FROM cursos;
END;
GO
Nota: Las tablas se generarán automáticamente al iniciar los microservicios gracias a SQLAlchemy.

💻 Ejecución de los Microservicios
Para levantar el Microservicio de Estudiantes (Puerto 8000):

Bash
uvicorn microservicio_estudiantes.main:app --reload
Documentación interactiva: http://127.0.0.1:8000/docs

Para levantar el Microservicio de Cursos (Puerto 8001):

Bash
uvicorn microservicio_cursos.main:app --reload --port 8001
Documentación interactiva: http://127.0.0.1:8001/docs

🧪 Pruebas Automatizadas
Para ejecutar las pruebas unitarias y de integración de la API, ejecuta el siguiente comando en la raíz del proyecto:

Bash
python -m pytest

---

### Sube estos cambios finales
Una vez que guardes ambos archivos, sube esto a la rama principal para dar por cerrado el código en GitHub:
```bash
git add .
git commit -m "docs: se agrega README completo y requirements.txt"
git push origin main