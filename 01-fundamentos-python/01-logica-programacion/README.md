# Logica de Programacion

Antes de escribir codigo, hay que aprender a PENSAR como programador. La **logica de programacion** es la base de todo: son las herramientas mentales para resolver problemas con una computadora.

---

## 1. TEORIA

### 1.1 Que es un algoritmo?

Un **algoritmo** es una secuencia de pasos ORDENADOS y FINITOS para resolver un problema.

**Analogia:** Una receta de cocina es un algoritmo:

```
1. Conseguir ingredientes
2. Pelar y cortar verduras
3. Cocinar a fuego medio por 20 minutos
4. Servir en un plato
```

Cada paso es claro (no hay ambiguedad), hay un orden (no cocinas antes de pelar), y tiene un final (se termina cuando sirves).

### 1.2 Caracteristicas de un buen algoritmo

| Caracteristica | Significa que... | Ejemplo MALO | Ejemplo BUENO |
|----------------|------------------|--------------|---------------|
| **Preciso** | Cada paso esta claramente definido | "Cocina un poco" | "Cocina por 20 minutos a 180 grados" |
| **Finito** | Tiene un final claro, no es infinito | "Sigue cocinando hasta que quede bien" | "Repite 5 veces: revuelve cada 2 minutos" |
| **Determinista** | Misma entrada = misma salida | "Agrega sal al gusto" | "Agrega 5 gramos de sal" |

### 1.3 Traducir problemas a algoritmos

Cuando te enfrentes a un problema de programacion, sigue estos pasos:

1. **Entender** el problema (que pide exactamente?)
2. **Dividir** en partes pequenas
3. **Escribir** los pasos en espanol (pseudocodigo)
4. **Traducir** a codigo Python

### 1.4 Pseudocodigo

El pseudocodigo es codigo escrito en lenguaje humano. No se ejecuta, se usa para PLANIFICAR.

```
Problema: "Calcular el promedio de 3 numeros"

Pseudocodigo:
1. PEDIR numero 1 al usuario
2. PEDIR numero 2 al usuario
3. PEDIR numero 3 al usuario
4. SUMAR los 3 numeros
5. DIVIDIR la suma entre 3
6. MOSTRAR el resultado
```

**Por que escribir pseudocodigo?** Porque separa el "QUE hacer" del "COMO hacerlo". Primero resuelves la logica, luego te preocupas por la sintaxis del lenguaje.

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Algoritmo** | Secuencia de pasos ordenados para resolver un problema | Una receta de cocina |
| **Programa** | Algoritmo escrito en un lenguaje de programacion | `print("Hola")` |
| **Pseudocodigo** | Algoritmo escrito en lenguaje humano (no se ejecuta) | `SI llueve: llevar paraguas` |
| **Dato** | Informacion que el programa procesa | Un numero, un texto, etc. |
| **Entrada / Input** | Datos que el programa recibe | Lo que escribe el usuario |
| **Procesamiento** | Operaciones que el programa hace con los datos | Calcular, comparar, transformar |
| **Salida / Output** | Resultado que el programa muestra | Lo que se imprime en pantalla |
| **Depuracion / Debugging** | Proceso de encontrar y corregir errores | Leer el error, entenderlo, arreglarlo |

---

## 3. COMPARATIVA ENTRE LENGUAJES

La logica de programacion es UNIVERSAL. El pseudocodigo no depende del lenguaje:

```
Pseudocodigo:
  PEDIR nombre
  MOSTRAR "Hola, " + nombre
```

| Python | Java | JavaScript |
|--------|------|------------|
| `nombre = input()` | `Scanner sc = new Scanner(System.in); String nombre = sc.nextLine();` | `let nombre = prompt();` |
| `print("Hola, " + nombre)` | `System.out.println("Hola, " + nombre);` | `console.log("Hola, " + nombre);` |

La LOGICA es identica: pedir un valor, guardarlo, mostrarlo. Cambia la sintaxis, no el pensamiento.

---

## 4. EJEMPLO GUIADO

### Problema: Calcular el area de un rectangulo

"Escribe un programa que pida el ancho y el alto de un rectangulo, y muestre su area (ancho * alto)"

---

**Paso 1: Analizar**
- Entrada: dos numeros (ancho, alto)
- Proceso: multiplicar ancho * alto
- Salida: el resultado de la multiplicacion

**Paso 2: Pseudocodigo**
```
PEDIR ancho
PEDIR alto
area = ancho * alto
MOSTRAR area
```

**Paso 3: Codigo**
```python
ancho = float(input("Ingresa el ancho: "))
alto = float(input("Ingresa el alto: "))
area = ancho * alto
print(f"El area del rectangulo es: {area}")
```

**Explicacion:**
1. `float(input(...))` — input() devuelve texto, float() lo convierte a numero decimal (por si las medidas no son enteras)
2. `area = ancho * alto` — Calculamos multiplicando, guardamos en variable
3. `print(f"...{area}")` — Mostramos el resultado con f-string

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Preparar un sandwich (Basico)

Escribe un programa que muestre los pasos para preparar un sandwich, un paso por linea usando `print()`.

**Conceptos que aplicas:** `print()`, pensar en secuencia de pasos.

**Ejecuta:** `python scripts/runner.py 1 1 1`

---

### 🟡 Ejercicio 2: Par o impar (Intermedio)

Pide un numero al usuario y determina si es par o impar usando el operador `%`.

**Conceptos que aplicas:** `input()`, `int()`, `%`, `if/else`.

**Ejecuta:** `python scripts/runner.py 1 1 2`

---

### 🔴 Ejercicio 3: Mayor de 3 numeros (Avanzado)

Pide 3 numeros al usuario y muestra el mayor de los 3, sin usar la funcion `max()`.

**Conceptos que aplicas:** `input()`, `int()`, `if/elif/else`, comparaciones multiples.

**Ejecuta:** `python scripts/runner.py 1 1 3`

---

## Soluciones

```bash
python scripts/runner.py 1 1 1 -s
python scripts/runner.py 1 1 2 -s
python scripts/runner.py 1 1 3 -s
```
