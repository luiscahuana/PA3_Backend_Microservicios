from fastapi.testclient import TestClient
from microservicio_estudiantes.main import app

# Inicializamos el cliente de pruebas
client = TestClient(app)

def test_listar_estudiantes():
    # Simulamos una petición GET a la ruta de estudiantes
    response = client.get("/estudiantes/")
    
    # Verificamos que el servidor responda con un código 200 (Éxito)
    assert response.status_code == 200
    
    # Verificamos que la respuesta sea una lista (el JSON que devuelve FastAPI)
    assert isinstance(response.json(), list)

def test_registrar_estudiante_datos_invalidos():
    # Simulamos enviar un JSON incompleto para ver si la API lo rechaza correctamente
    response = client.post(
        "/estudiantes/",
        json={"codigo": "E999", "nombres": "Juan"} # Faltan apellidos, correo y carrera
    )
    
    # Debería devolver 422 Unprocessable Entity por faltar datos obligatorios
    assert response.status_code == 422