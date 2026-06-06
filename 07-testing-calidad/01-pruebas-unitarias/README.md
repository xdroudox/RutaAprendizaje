# Pruebas Unitarias

Verifican el comportamiento de la unidad mas pequena de codigo (funcion, metodo) de forma aislada.

## Conceptos Basicos

- **Unidad**: la porcion mas pequena de codigo que se puede probar (una funcion, un metodo, una clase).
- **Assert**: declaracion que verifica si una condicion es verdadera. Si es falsa, lanza una excepcion.
- **Test case**: conjunto de entradas, ejecucion y resultado esperado.
- **Cobertura**: porcentaje del codigo que es ejecutado por las pruebas.

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Assertion** | Condicion booleana que debe cumplirse para que la prueba pase |
| **Fixture** | Estado o datos preparados antes de ejecutar una prueba |
| **Test Runner** | Herramienta que descubre y ejecuta las pruebas (pytest, unittest) |
| **TestCase** | Clase o funcion que contiene una o mas pruebas |
| **Red-Green-Refactor** | Ciclo de TDD: escribir prueba fallida, hacerla pasar, refactorizar |
| **assert** | Palabra clave de Python que verifica una condicion |
| **pytest** | Framework de pruebas para Python, mas conciso que unittest |

## Comparativa entre Lenguajes

### Python (pytest)
```python
def test_suma():
    assert 1 + 1 == 2

def test_suma_lista():
    assert sum([1, 2, 3]) == 6
```
Ejecutar: `pytest test_archivo.py -v`

### Java (JUnit 5)
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculadoraTest {
    @Test
    void testSuma() {
        assertEquals(2, 1 + 1);
    }

    @Test
    void testSumaLista() {
        assertEquals(6, Arrays.asList(1,2,3).stream().mapToInt(i->i).sum());
    }
}
```
Ejecutar: `mvn test` o `gradle test`

### JavaScript (Jest)
```javascript
test('suma 1 + 2 = 3', () => {
    expect(1 + 2).toBe(3);
});

test('suma lista', () => {
    expect([1,2,3].reduce((a,b) => a+b, 0)).toBe(6);
});
```
Ejecutar: `npx jest`

## assert en Python

La forma mas basica de probar. Ideal para aprender los fundamentos:

```python
assert 2 + 2 == 4
assert suma(2, 3) == 5, "mensaje personalizado si falla"
assert resultado is not None
assert len(lista) > 0
```

## pytest

Framework de pruebas estandar para Python. Descubre automaticamente archivos `test_*.py` y funciones `test_*()`.

### Instalacion
```bash
pip install pytest
```

### Ejemplo basico
```python
# test_ejemplo.py
def test_suma():
    assert 1 + 1 == 2

def test_resta():
    assert 3 - 1 == 2
```

### Ejecucion
```bash
pytest                          # Descubre y ejecuta todas las pruebas
pytest test_ejemplo.py -v       # Archivo especifico con verbose
pytest -k "suma"                # Filtra por nombre
pytest --coverage               # Con cobertura (requiere pytest-cov)
```

### Fixtures
```python
@pytest.fixture
def datos_prueba():
    return {"nombre": "Ana", "edad": 30}

def test_usuario(datos_prueba):
    assert datos_prueba["nombre"] == "Ana"
```

## Ejemplo Guiado: Probar una funcion de calculadora

Paso 1: Escribir la funcion
```python
def calcular_descuento(precio, porcentaje):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("Porcentaje debe estar entre 0 y 100")
    return precio * (1 - porcentaje / 100)
```

Paso 2: Escribir pruebas
```python
def test_descuento_normal():
    assert calcular_descuento(100, 20) == 80.0

def test_descuento_cero():
    assert calcular_descuento(100, 0) == 100.0

def test_descuento_total():
    assert calcular_descuento(100, 100) == 0.0

def test_precio_negativo():
    try:
        calcular_descuento(-10, 20)
        assert False, "Debio lanzar ValueError"
    except ValueError:
        pass
```

Paso 3: Ejecutar
```bash
pytest test_calculadora.py -v
```

## Referencia rapida de pytest

| Comando | Descripcion |
|---------|------------|
| `pytest` | Ejecuta todas las pruebas |
| `pytest -v` | Modo verbose (muestra cada test) |
| `pytest -k "palabra"` | Filtra pruebas por nombre |
| `pytest -x` | Detiene en el primer fallo |
| `pytest --maxfail=3` | Detiene despues de N fallos |
| `pytest -s` | Muestra prints dentro de las pruebas |
| `pytest --tb=short` | Traza de error mas corta |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 7 1 [ejercicio] [-p N]`

1. 🟢 **Escribir funcion es_par() y probarla con assert**
2. 🟢 **Escribir test para funcion que suma lista**
3. 🟡 **Usar pytest (funcion test_...)**
