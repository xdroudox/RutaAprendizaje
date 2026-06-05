# Pruebas de Integracion

## Que son las pruebas de integracion

Las pruebas de integracion verifican que multiples componentes funcionen correctamente juntos. Mientras las pruebas unitarias aï¿½lan una unidad, las de integracion prueban la interaccion entre unidades.

Ejemplos:
- Una funcion que consulta una base de datos
- Un modulo que llama a otro modulo
- Un servicio que se comunica con una API externa

## Pruebas de integracion con base de datos

SQLite en memoria es ideal para pruebas de integracion:

```python
import sqlite3
import pytest

@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT)")
    conn.execute("INSERT INTO usuarios VALUES (1, 'Ana')")
    yield conn
    conn.close()

def test_obtener_usuario(db):
    cursor = db.execute("SELECT nombre FROM usuarios WHERE id = 1")
    assert cursor.fetchone()[0] == "Ana"
```

## Setup y Teardown

Setup: prepara el entorno antes de cada prueba.
Teardown: limpia los recursos despues de cada prueba.

En pytest, se usa `yield` en un fixture para separar setup y teardown:

```python
@pytest.fixture
def recurso():
    # Setup
    db = conectar_base_datos()
    yield db
    # Teardown
    db.cerrar_conexion()
```

## Pruebas entre modulos

Cuando un modulo depende de otro, se prueba la integracion:

```python
# modulo_usuarios.py
def crear_usuario(db, nombre):
    db.execute("INSERT INTO usuarios (nombre) VALUES (?)", (nombre,))
    db.commit()
    return db.lastrowid

# test_integracion.py
def test_crear_y_consultar_usuario(db):
    id_usuario = crear_usuario(db, "Luis")
    cursor = db.execute("SELECT nombre FROM usuarios WHERE id = ?", (id_usuario,))
    assert cursor.fetchone()[0] == "Luis"
```
