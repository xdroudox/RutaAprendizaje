# Clean Code

Principios para codigo legible, mantenible y eficiente.

## SRP (Single Responsibility Principle)

Cada funcion debe hacer una sola cosa.

```java
// Mal: una funcion hace todo
void procesar(int[] nums) { ... }

// Bien: funciones especificas
int calcularSuma(int[] nums) { ... }
double calcularPromedio(int[] nums) { ... }
```

## Nombres descriptivos

El codigo debe explicarse por si mismo.

```java
// Mal
double cf(double pb, double iv, double d) { ... }

// Bien
double calcularPrecioFinal(double precioBase, double tasaIVA, double descuento) { ... }
```

## DRY (Don't Repeat Yourself)

Cada conocimiento debe tener una unica representacion.

```java
// Extraer metodo comun en vez de repetir
String formatearNombre(String nombre, String apellido) {
    return "Nombre: " + nombre + " " + apellido;
}
```

## Ejercicios

1. **Refactorizar funcion larga en funciones pequenas (SRP)**
   **Ejecuta:** `python scripts/runner.py 8 5 1`

2. **Renombrar variables y metodos con nombres descriptivos**
   **Ejecuta:** `python scripts/runner.py 8 5 2`

3. **Eliminar codigo duplicado (DRY) extrayendo metodo**
   **Ejecuta:** `python scripts/runner.py 8 5 3`
