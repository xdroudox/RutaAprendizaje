# Nivel 7: Testing y Calidad

Aprende a escribir pruebas automatizadas: unitarias, integracion, TDD, mocking y APIs.

## Modulos

### 1. Pruebas Unitarias (01-pruebas-unitarias)
assert, pytest, funciones test_*, fixtures.

### 2. Pruebas de Integracion (02-pruebas-integracion)
SQLite en memoria, setup/teardown, integracion entre modulos.

### 3. TDD (03-tdd)
Ciclo Red-Green-Refactor, escribir prueba primero.

### 4. Mocking (04-mocking)
unittest.mock, Mock, patch, side_effect.

### 5. Pruebas de API (05-pruebas-api)
requests, GET, POST, validacion de respuestas.

## Como ejecutar

```bash
python scripts/runner.py 7 [modulo] [ejercicio]
```

Ejemplo: `python scripts/runner.py 7 1 1`

## Requisitos

- Python 3.6+
- pytest (`pip install pytest`)
- requests (`pip install requests`)
