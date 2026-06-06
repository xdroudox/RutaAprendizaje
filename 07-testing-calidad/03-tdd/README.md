# TDD - Test Driven Development

Metodologia donde las pruebas se escriben ANTES del codigo de produccion.

## Conceptos Basicos

- **TDD (Test-Driven Development)**: metodologia de desarrollo donde primero se escribe la prueba, luego el codigo minimo para que pase, y finalmente se refactoriza.
- **Red-Green-Refactor**: ciclo fundamental de TDD.
- **Baby steps**: cambios minimos para pasar de rojo a verde rapidamente.
- **Triangulacion**: escribir multiples casos de prueba para generalizar la solucion.
- **Refactor**: mejora del codigo sin cambiar su comportamiento externo.

## Glosario

| Termino | Definicion |
|---------|-----------|
| **RED** | Escribir una prueba que falla (aun no hay codigo de produccion) |
| **GREEN** | Escribir el codigo minimo necesario para que la prueba pase |
| **REFACTOR** | Mejorar el codigo manteniendo todas las pruebas verdes |
| **Baby Step** | Cambio minimo que hace pasar una prueba |
| **Triangulation** | Agregar casos de prueba para forzar una solucion general |
| **False Positive** | Prueba que pasa por error (codigo incorrecto, prueba mal escrita) |
| **Regression** | Prueba que asegura que cambios nuevos no rompan funcionalidad existente |

## El Ciclo Red-Green-Refactor

```
[RED]    -> Escribes una prueba que falla
[GREEN]  -> Escribes el codigo MINIMO para que pase
[REFACTOR] -> Mejoras el codigo (las pruebas siguen pasando)
    |
    v (siguiente funcionalidad)
  [RED] -> ...
```

## Comparativa entre Lenguajes

### Python
```python
# RED: escribimos la prueba primero
def test_fizzbuzz_retorna_numero():
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(2) == '2'

# GREEN: codigo minimo
def fizzbuzz(n):
    return str(n)

# REFACTOR: mejorar (cuando tengamos mas tests)
```

### Java (JUnit 5)
```java
// RED
@Test
void testFizzBuzzRetornaNumero() {
    assertEquals("1", FizzBuzz.fizzbuzz(1));
    assertEquals("2", FizzBuzz.fizzbuzz(2));
}

// GREEN
public class FizzBuzz {
    public static String fizzbuzz(int n) {
        return String.valueOf(n);
    }
}
```

### JavaScript (Jest)
```javascript
// RED
test('fizzbuzz retorna string para 1 y 2', () => {
    expect(fizzbuzz(1)).toBe('1');
    expect(fizzbuzz(2)).toBe('2');
});

// GREEN
function fizzbuzz(n) {
    return String(n);
}
```

## Ejemplo Guiado: FizzBuzz con TDD paso a paso

### Paso 1 - RED
Escribimos la prueba que falla:
```python
def test_fizzbuzz_retorna_numero():
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(2) == '2'
```
Ejecutamos: `pytest` -> FALLA (fizzbuzz no existe)

### Paso 2 - GREEN
Codigo minimo para que pase:
```python
def fizzbuzz(n):
    return str(n)
```
Ejecutamos: `pytest` -> PASA

### Paso 3 - RED (siguiente requerimiento)
```python
def test_fizzbuzz_multiplo_de_3():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(6) == 'Fizz'
```
Ejecutamos: FALLA (retorna '3', espera 'Fizz')

### Paso 4 - GREEN
```python
def fizzbuzz(n):
    if n % 3 == 0:
        return 'Fizz'
    return str(n)
```
Ejecutamos: PASA

### Paso 5 - Repetir para Buzz y FizzBuzz
```python
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return str(n)
```

## Beneficios de TDD

- **Diseno emergente**: el codigo surge de las necesidades de las pruebas
- **Documentacion viva**: las pruebas documentan como debe usarse el codigo
- **Red de seguridad**: cualquier cambio que rompa algo se detecta al instante
- **Menos debugging**: si una prueba falla, sabes exactamente donde esta el error
- **Confianza para refactorizar**: puedes mejorar el codigo sin miedo a romperlo

## Referencia rapida

| Fase | Que haces | Resultado |
|------|-----------|-----------|
| RED | Escribes una prueba | pytest: FALLA |
| GREEN | Codigo minimo para pasar | pytest: PASA |
| REFACTOR | Mejoras el codigo | pytest: PASA (sigue pasando) |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 7 3 [ejercicio] [-p N]`

1. 🟢 **FizzBuzz con TDD (escribir test primero)**
2. 🟡 **Validador de email con TDD**
3. 🟡 **Calculadora de promedios con TDD**
