# Nivel 7: Testing y Calidad

Bienvenido al nivel de Testing y Calidad de Software. Aqui aprenderas a escribir pruebas automatizadas, desde pruebas unitarias hasta pruebas de API, pasando por TDD y mocking.

## Modulos

### 1. Pruebas Unitarias (01-pruebas-unitarias)
Que son las pruebas unitarias, uso de assert, pytest, funciones de prueba, fixtures.

### 2. Pruebas de Integracion (02-pruebas-integracion)
Probar componentes juntos, pruebas con base de datos, setup/teardown.

### 3. TDD (03-tdd)
Ciclo Red-Green-Refactor, escribir prueba primero, implementar, refactorizar.

### 4. Mocking (04-mocking)
unittest.mock, Mock, patch, cuando mockear vs real, side effects.

### 5. Pruebas de API (05-pruebas-api)
Probar endpoints HTTP con requests, codigos de estado, validacion de respuestas.

## Como usar

Cada modulo contiene:

- `README.md` -- Explicacion teorica del tema
- `ejercicios.py` -- Ejercicios practicos
- `soluciones.py` -- Soluciones a los ejercicios

Ejecutar un ejercicio:

    python ejercicios.py 1
    python soluciones.py 1

## Requisitos

- Python 3.6+
- pytest (instalar con: pip install pytest)
- requests (instalar con: pip install requests)
