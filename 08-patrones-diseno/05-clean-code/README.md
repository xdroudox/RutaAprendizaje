# Clean Code

Principios para escribir codigo legible, mantenible y eficiente.

## Conceptos Basicos

- **SRP (Single Responsibility Principle)**: cada clase o metodo debe tener una unica responsabilidad. Si haces varias cosas, dividelas.
- **Nombres descriptivos**: el codigo debe explicarse por si mismo. Los nombres de variables, metodos y clases deben revelar la intencion.
- **DRY (Don't Repeat Yourself)**: cada pieza de conocimiento debe tener una representacion unica y no ambigua en el sistema.

## Glosario

| Termino | Definicion |
|---------|-----------|
| **SRP** | Principio de Responsabilidad Unica: una razon para cambiar |
| **DRY** | No te repitas: extrae codigo repetido a metodos reutilizables |
| **KISS** | Mantenlo simple: la solucion mas simple suele ser la mejor |
| **YAGNI** | No lo vas a necesitar: no anadas funcionalidad hasta que sea necesaria |
| **Code Smell** | Indicador superficial de que hay un problema mas profundo |
| **Refactor** | Mejorar el codigo sin cambiar su comportamiento |
| **Magic Number** | Numero literal sin explicacion (ej: 86400 en vez de SEGUNDOS_POR_DIA) |

## Comparativa entre Lenguajes

### Java
```java
// Mal
double cf(double pb, double iv, double d) {
    double ci = pb * iv;
    double cd = pb * d;
    return pb + ci - cd;
}

// Bien
double calcularPrecioFinal(double precioBase, double tasaIVA, double descuento) {
    double iva = precioBase * tasaIVA;
    double descuentoAplicado = precioBase * descuento;
    return precioBase + iva - descuentoAplicado;
}
```

### Python
```python
# Mal
def cf(pb, iv, d):
    return pb + (pb * iv) - (pb * d)

# Bien
def calcular_precio_final(precio_base, tasa_iva, descuento):
    iva = precio_base * tasa_iva
    desc = precio_base * descuento
    return precio_base + iva - desc
```

### JavaScript
```javascript
// Mal
const calc = (a, b, c) => a + (a * b) - (a * c);

// Bien
const calcularPrecioFinal = (precioBase, tasaIVA, descuento) => {
    const iva = precioBase * tasaIVA;
    const desc = precioBase * descuento;
    return precioBase + iva - desc;
};
```

## Ejemplo Guiado: Refactorizar aplicando SRP y DRY

### Codigo original (todo en una funcion)
```java
void procesar(int[] nums) {
    int s = 0;
    for (int n : nums) s += n;
    double p = (double) s / nums.length;
    int mx = nums[0], mn = nums[0];
    for (int n : nums) {
        if (n > mx) mx = n;
        if (n < mn) mn = n;
    }
    System.out.println("Suma: " + s);
    System.out.println("Prom: " + p);
    System.out.println("Max: " + mx);
    System.out.println("Min: " + mn);
}
```

### Codigo refactorizado (SRP)
```java
int calcularSuma(int[] nums) {
    int suma = 0;
    for (int n : nums) suma += n;
    return suma;
}

double calcularPromedio(int[] nums) {
    return (double) calcularSuma(nums) / nums.length;
}

int encontrarMaximo(int[] nums) {
    int max = nums[0];
    for (int n : nums) if (n > max) max = n;
    return max;
}

int encontrarMinimo(int[] nums) {
    int min = nums[0];
    for (int n : nums) if (n < min) min = n;
    return min;
}

void mostrarEstadisticas(int[] nums) {
    System.out.println("Suma: " + calcularSuma(nums));
    System.out.println("Promedio: " + calcularPromedio(nums));
    System.out.println("Maximo: " + encontrarMaximo(nums));
    System.out.println("Minimo: " + encontrarMinimo(nums));
}
```

## Principios clave

| Principio | Que significa | Ejemplo |
|-----------|--------------|---------|
| **SRP** | Una clase/metodo = una responsabilidad | No mezclar calculo con impresion |
| **Nombres descriptivos** | El nombre explica el proposito | `calcularPrecioFinal()` no `cf()` |
| **DRY** | No copies y pegues codigo | Extraer metodo comun en vez de repetir |
| **Sin magic numbers** | Las constantes tienen nombre | `final int IVA = 21` no `0.21` |
| **Funciones pequenas** | Maximo 20-30 lineas | Dividir funciones largas |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 8 5 [ejercicio] [-p N]`

1. 🟢 **Refactorizar funcion larga en funciones pequenas (SRP)**
2. 🟡 **Renombrar variables y metodos con nombres descriptivos**
3. 🟡 **Eliminar codigo duplicado (DRY) extrayendo metodo**
