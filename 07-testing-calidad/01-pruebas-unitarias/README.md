# Pruebas Unitarias

Verifican el comportamiento de la unidad mas pequena de codigo (funcion, metodo) de forma aislada.

## assert

```python
assert 2 + 2 == 4
assert suma(2, 3) == 5, "mensaje si falla"
```

## pytest

Framework de pruebas para Python. Archivos `test_*.py`, funciones `test_*()`.

```python
# test_ejemplo.py
def test_suma():
    assert 1 + 1 == 2
```

Ejecutar: `pytest test_ejemplo.py -v`

## Ejercicios

1. **Escribir funcion es_par() y probarla con assert**
   **Ejecuta:** `python scripts/runner.py 7 1 1`

2. **Escribir test para funcion que suma lista**
   **Ejecuta:** `python scripts/runner.py 7 1 2`

3. **Usar pytest (funcion test_...)**
   **Ejecuta:** `python scripts/runner.py 7 1 3`
