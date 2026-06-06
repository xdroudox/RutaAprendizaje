# Pruebas de Integracion

Verifican que multiples componentes funcionen correctamente juntos.

## Conceptos Basicos

- **Prueba de integracion**: prueba que verifica la interaccion entre dos o mas modulos/servicios.
- **Base de datos en memoria**: BD que existe solo en RAM (ej: `:memory:` en SQLite), ideal para pruebas por ser rapida y sin efectos secundarios.
- **Setup/Teardown**: configuracion inicial y limpieza posterior a cada prueba.
- **Fixture**: mecanismo que prepara el entorno necesario para una prueba.

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Integracion** | Combinacion de modulos para que funcionen como un sistema |
| **SQLite :memory:** | Base de datos temporal en RAM que se elimina al cerrar la conexion |
| **Fixture** | Funcion decorada con `@pytest.fixture` que provee datos/configuracion |
| **Setup** | Codigo que se ejecuta antes de cada prueba para preparar el entorno |
| **Teardown** | Codigo que se ejecuta despues de cada prueba para limpiar recursos |
| **yield** | Palabra clave que separa el setup (antes) del teardown (despues) en fixtures |
| **Acoplamiento** | Grado de dependencia entre modulos; a menor acoplamiento, mas faciles las pruebas |

## Comparativa entre Lenguajes

### Python (pytest + SQLite)
```python
@pytest.fixture
def db():
    conn = sqlite3.connect(':memory:')
    conn.execute("CREATE TABLE test (id INT)")
    yield conn
    conn.close()

def test_insertar(db):
    db.execute("INSERT INTO test VALUES (1)")
    cursor = db.execute("SELECT * FROM test")
    assert cursor.fetchone() is not None
```

### Java (JUnit + H2)
```java
@BeforeEach
void setUp() {
    conn = DriverManager.getConnection("jdbc:h2:mem:test");
    conn.createStatement().execute("CREATE TABLE test (id INT)");
}

@AfterEach
void tearDown() throws Exception {
    conn.close();
}

@Test
void testInsertar() throws Exception {
    conn.createStatement().execute("INSERT INTO test VALUES (1)");
    var rs = conn.createStatement().executeQuery("SELECT * FROM test");
    assertTrue(rs.next());
}
```

### JavaScript (Jest + SQLite)
```javascript
const sqlite3 = require('sqlite3');
let db;

beforeEach(() => {
    db = new sqlite3.Database(':memory:');
    db.run("CREATE TABLE test (id INT)");
});

afterEach(() => {
    db.close();
});

test('insertar registro', (done) => {
    db.run("INSERT INTO test VALUES (1)", () => {
        db.get("SELECT * FROM test", (err, row) => {
            expect(row.id).toBe(1);
            done();
        });
    });
});
```

## SQLite en memoria para pruebas

Ideal para pruebas de integracion por ser rapida, aislada y sin configuracion:

```python
import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')
conn.execute("INSERT INTO usuarios (nombre, email) VALUES ('Ana', 'ana@test.com')")
conn.commit()

cursor = conn.execute("SELECT * FROM usuarios WHERE nombre = ?", ('Ana',))
usuario = cursor.fetchone()
print(usuario)  # (1, 'Ana', 'ana@test.com')

conn.close()  # La BD se elimina al cerrar
```

## Fixtures con setup/teardown en pytest

```python
import pytest
import sqlite3

@pytest.fixture
def db():
    # SETUP: crear conexion y tabla
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')
    yield conn  # La prueba recibe 'conn'
    # TEARDOWN: cerrar conexion (la BD en memoria se descarta)
    conn.close()

def test_insertar_usuario(db):
    db.execute("INSERT INTO usuarios (nombre, email) VALUES ('Luis', 'luis@test.com')")
    cursor = db.execute("SELECT * FROM usuarios WHERE nombre = 'Luis'")
    assert cursor.fetchone() is not None
```

## Ejemplo Guiado: Prueba de integracion completa

Paso 1: Modulo que procesa datos
```python
def procesar_datos(datos):
    """Convierte strings a mayusculas."""
    return [d.upper() for d in datos]
```

Paso 2: Modulo que guarda en BD
```python
def guardar_datos(conn, datos):
    for d in datos:
        conn.execute("INSERT INTO items (valor) VALUES (?)", (d,))
    conn.commit()
```

Paso 3: Prueba de integracion (verifica el flujo completo)
```python
import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, valor TEXT)")

datos = procesar_datos(['hola', 'mundo'])
guardar_datos(conn, datos)

cursor = conn.execute("SELECT valor FROM items ORDER BY id")
resultados = [row[0] for row in cursor.fetchall()]
assert resultados == ['HOLA', 'MUNDO']

conn.close()
```

## Referencia rapida

| Componente | Descripcion |
|------------|-------------|
| `sqlite3.connect(':memory:')` | Conexion a BD temporal en RAM |
| `conn.execute(sql)` | Ejecuta una sentencia SQL |
| `conn.commit()` | Confirma los cambios |
| `cursor.fetchone()` | Obtiene una fila del resultado |
| `cursor.fetchall()` | Obtiene todas las filas |
| `@pytest.fixture` | Decorador para crear fixtures |
| `yield conn` | Entrega el recurso y espera a que termine la prueba |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 7 2 [ejercicio] [-p N]`

1. 🟢 **Probar funcion que inserta y consulta SQLite**
2. 🟡 **Setup/teardown de base de datos en memoria**
3. 🟡 **Probar integracion entre 2 modulos**
