# Recursion

Una funcion **recursiva** es aquella que se llama a si misma para resolver un problema dividiendolo en subproblemas mas pequenos del mismo tipo.

---

## 1. TEORIA

### 1.1 Componentes de la recursion

Toda funcion recursiva tiene dos partes:

```
def funcion(parametro):
    if CASO_BASE:        ← Condicion que DETIENE la recursion
        return resultado
    else:
        return CASO_RECURSIVO  ← Llamada a si misma con parametro reducido
```

| Componente | Que hace | Ejemplo (factorial) |
|------------|----------|---------------------|
| **Caso base** | Detiene la recursion | `if n <= 1: return 1` |
| **Caso recursivo** | Se llama a si misma | `return n * factorial(n - 1)` |
| **Progreso** | Reduce el problema | `n - 1` se acerca a 1 |

### 1.2 Factorial — n!

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

```python
def factorial(n):
    if n <= 1:          # Caso base
        return 1
    return n * factorial(n - 1)  # Caso recursivo

# Traza de ejecucion para factorial(5):
# factorial(5) = 5 * factorial(4)
#              = 5 * (4 * factorial(3))
#              = 5 * (4 * (3 * factorial(2)))
#              = 5 * (4 * (3 * (2 * factorial(1))))
#              = 5 * (4 * (3 * (2 * 1)))
#              = 5 * 4 * 3 * 2 * 1
#              = 120
```

### 1.3 Fibonacci

```
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)
```

```python
def fibonacci(n):
    if n <= 1:           # Caso base
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo

# Serie: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# fib(7) = 13
```

**Atencion:** fibonacci recursivo SIN optimizacion tiene complejidad O(2^n). Para n=50 ya es impracticable.

### 1.4 Suma de digitos

Suma los digitos de un numero recursivamente.

```python
def suma_digitos(n):
    if n < 10:           # Caso base: un solo digito
        return n
    return n % 10 + suma_digitos(n // 10)

# suma_digitos(1234) = 4 + suma_digitos(123)
#                    = 4 + (3 + suma_digitos(12))
#                    = 4 + (3 + (2 + suma_digitos(1)))
#                    = 4 + 3 + 2 + 1
#                    = 10
```

### 1.5 Recursion vs Iteracion

| Aspecto | Recursion | Iteracion (bucle) |
|---------|-----------|-------------------|
| Codigo | Mas conciso, refleja la formula matematica | Mas explicito |
| Memoria | Cada llamada ocupa espacio en el stack | O(1) adicional |
| Riesgos | Stack overflow si es muy profunda | No hay overflow |
| Rendimiento | Mas lento por overhead de llamadas | Mas rapido |
| Cuando usarla | Arboles, grafos, backtracking, divide y conquista | Problemas lineales simples |

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Recursion** | Tecnica donde una funcion se llama a si misma |
| **Caso base** | Condicion que detiene la recursion |
| **Caso recursivo** | Llamada a la funcion con parametros reducidos |
| **Stack de llamadas** | Pila de llamadas de funcion pendientes de resolver |
| **Stack overflow** | Cuando el stack de llamadas excede la memoria disponible |
| **Recursion directa** | La funcion se llama a si misma directamente |
| **Recursion indirecta** | A llama a B, B llama a A |
| **Tail recursion** | La llamada recursiva es la ULTIMA operacion |
| **Backtracking** | Tecnica que prueba opciones y retrocede si falla |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Factorial

```python
# PYTHON
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)
```

```java
// JAVA
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

```javascript
// JAVASCRIPT
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

### Fibonacci

```python
# PYTHON
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)
```

```java
// JAVA
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

```javascript
// JAVASCRIPT
function fib(n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

---

## 4. EJEMPLO GUIADO: Calculadora de potencia

**Problema:** Implementar `potencia(base, exp)` que calcula base^exp recursivamente.

### Paso 1: Definir la recursion

```
base^exp = base * base^(exp-1)
base^0 = 1
```

### Paso 2: Implementar

```python
def potencia(base, exp):
    if exp == 0:              # Caso base: cualquier numero ^ 0 = 1
        return 1
    return base * potencia(base, exp - 1)  # Caso recursivo
```

### Paso 3: Traza de ejecucion

```
potencia(2, 4):
  2 * potencia(2, 3)
  2 * (2 * potencia(2, 2))
  2 * (2 * (2 * potencia(2, 1)))
  2 * (2 * (2 * (2 * potencia(2, 0))))
  2 * (2 * (2 * (2 * 1)))
  2 * (2 * (2 * 2))
  2 * (2 * 4)
  2 * 8
  = 16
```

### Paso 4: Version optimizada (exponente par)

```python
def potencia_opt(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:                     # Si exp es par
        mitad = potencia_opt(base, exp // 2)
        return mitad * mitad             # base^exp = (base^(exp/2))^2
    else:                                # Si exp es impar
        return base * potencia_opt(base, exp - 1)

# potencia_opt(2, 100): ~7 llamadas en vez de 100
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Factorial recursivo

Implementa `factorial(n)` que calcula n! de forma recursiva.

**Ejecuta:** `python scripts/runner.py 3 8 1`

---

### 🟡 Ejercicio 2: Fibonacci recursivo

Implementa `fibonacci(n)` que devuelve el n-esimo numero de Fibonacci.

**Ejecuta:** `python scripts/runner.py 3 8 2`

---

### 🔴 Ejercicio 3: Suma de digitos recursiva

Implementa `suma_digitos(n)` que suma los digitos de un numero recursivamente. Ej: `1234` → `1+2+3+4 = 10`

**Ejecuta:** `python scripts/runner.py 3 8 3`
