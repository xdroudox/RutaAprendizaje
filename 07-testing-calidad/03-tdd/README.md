# TDD - Test Driven Development

## Que es TDD

TDD (Desarrollo Guiado por Pruebas) es una metodologia de desarrollo donde las pruebas se escriben ANTES del codigo de produccion.

## El ciclo Red-Green-Refactor

```
1. RED: Escribir una prueba que falle (aun no hay implementacion)
2. GREEN: Escribir el codigo minimo necesario para que la prueba pase
3. REFACTOR: Mejorar el codigo manteniendo las pruebas verdes
```

```
    [RED] -> [GREEN] -> [REFACTOR] -> [RED] -> ...
```

## Beneficios de TDD

- Codigo mas limpio y modular
- Mayor cobertura de pruebas
- Diseno emerge naturalmente (YAGNI - You Ain't Gonna Need It)
- Refactorizacion segura
- Documentacion viva del sistema
- Reduce el tiempo de debugging

## Ejemplo: FizzBuzz con TDD

### Paso 1 - RED: Escribir la prueba

```python
def test_fizzbuzz_retorna_numero():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
```

### Paso 2 - GREEN: Codigo minimo

```python
def fizzbuzz(n):
    return str(n)
```

### Paso 3 - REFACTOR: No hay nada que refactorizar aun

### Siguiente prueba - RED

```python
def test_fizzbuzz_multiplo_de_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
```

### GREEN

```python
def fizzbuzz(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)
```

Y asi sucesivamente hasta completar la implementacion.

## Consejos para TDD

- Escribe la prueba mas simple que pueda fallar
- Escribe el codigo mas simple que haga pasar la prueba
- Refactoriza solo cuando todas las pruebas esten verdes
- No escribas codigo de produccion sin una prueba que falle
- Ejecuta todas las pruebas frecuentemente
