# Pruebas Unitarias

## Que son las pruebas unitarias

Las pruebas unitarias verifican el comportamiento de la unidad mas pequena de codigo (una funcion, un metodo, una clase) de forma aislada.

Beneficios:
- Detectan errores temprano
- Facilitan la refactorizacion
- Sirven como documentacion viva
- Dan confianza al desplegar

## La sentencia assert

Python tiene la palabra reservada `assert` para verificar condiciones:

```python
assert 2 + 2 == 4
assert suma(2, 3) == 5, "La suma deberia ser 5"
```

Si la condicion es `False`, lanza `AssertionError`.

## pytest

pytest es el framework de pruebas mas popular de Python. Se instala con pip:

```
pip install pytest
```

Convenciones de pytest:
- Los archivos de prueba deben llamarse `test_*.py` o `*_test.py`
- Las funciones de prueba deben empezar con `test_`
- Las clases de prueba deben empezar con `Test`

## Funciones de prueba

```python
# test_calculadora.py
def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2
```

Ejecutar: `pytest test_calculadora.py`

## Fixtures

Los fixtures son funciones que proveen datos o configuracion a las pruebas:

```python
import pytest

@pytest.fixture
def calculadora():
    return Calculadora()

def test_suma(calculadora):
    assert calculadora.sumar(2, 3) == 5
```

Los fixtures se ejecutan antes de cada prueba y pueden tener alcance (scope) de funcion, clase, modulo o sesion.

## Probar excepciones

Con pytest se usa `pytest.raises`:

```python
import pytest

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
```
