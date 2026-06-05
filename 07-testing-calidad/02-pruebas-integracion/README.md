# Pruebas de Integracion

Verifican que multiples componentes funcionen correctamente juntos.

## SQLite en memoria

Ideal para pruebas sin afectar datos reales:

```python
conn = sqlite3.connect(':memory:')
```

## Fixtures con setup/teardown

```python
@pytest.fixture
def db():
    conn = sqlite3.connect(':memory:')
    conn.execute("CREATE TABLE test (id INT)")
    yield conn
    conn.close()
```

## Ejercicios

1. **Probar funcion que inserta y consulta SQLite**
   **Ejecuta:** `python scripts/runner.py 7 2 1`

2. **Setup/teardown de base de datos en memoria**
   **Ejecuta:** `python scripts/runner.py 7 2 2`

3. **Probar integracion entre 2 modulos**
   **Ejecuta:** `python scripts/runner.py 7 2 3`
