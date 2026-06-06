# RUTA DE APRENDIZAJE — Full Stack → Arquitecto de Software

```python
print("Bienvenido a tu viaje para convertirte en Arquitecto de Software")
print("Preparate para: codigo, cafes, bugs y muchas victorias epicas")
```

## Que es esto?

Un **roadmap RPG interactivo** para aprender desarrollo full-stack desde cero hasta arquitectura de software. No es solo teoria: **cada tema tiene ejercicios practicos que puedes ejecutar desde la terminal**, con explicaciones paso a paso y comparativas entre lenguajes.

---

## Metodologia de Aprendizaje

Este curso no solo te muestra codigo: **te explica cada linea, cada termino, cada concepto**. Asumimos que NO conoces los terminos tecnicos, y los vamos definiendo uno por uno.

### Como usar este curso

```
PASO 1: Lee la TEORIA
  - No solo leas el codigo, lee las explicaciones de CADA linea
  - Si encuentras un termino que no entiendes, revisa el GLOSARIO
  - Los terminos nuevos aparecen en NEGRITA la primera vez

PASO 2: Revisa la COMPARATIVA entre lenguajes
  - El mismo concepto en Python, Java y JavaScript
  - Esto te ayuda a entender el PATRON, no solo la sintaxis

PASO 3: Sigue el EJEMPLO GUIADO paso a paso
  - Vemos un problema completo: desde analisis hasta codigo final
  - Cada linea del codigo esta explicada: QUE hace y POR QUE

PASO 4: Practica con EJERCICIOS PROGRESIVOS
  - 🟢 Basico: aplicas 1 concepto nuevo
  - 🟡 Intermedio: combinas 2 o mas conceptos
  - 🔴 Avanzado: problema real que integra todo lo aprendido

PASO 5: Usa PISTAS si te atascas
  - python scripts/runner.py N M E -p 1  (pista suave)
  - python scripts/runner.py N M E -p 2  (pista media)
  - python scripts/runner.py N M E -p 3  (pista fuerte)

PASO 6: Revisa la SOLUCION
  - No solo copies: lee la explicacion de POR QUE funciona
  - Compara con tu solucion y entiende las diferencias
```

### Niveles de dificultad de los ejercicios

Cada tema tiene 3 ejercicios en dificultad creciente:

| Nivel | Icono | Descripcion | Ejemplo |
|-------|-------|-------------|---------|
| Basico | 🟢 | Aplicas 1 concepto nuevo, muy guiado | Usar un if para clasificar una nota |
| Intermedio | 🟡 | Combinas 2+ conceptos del tema | Usar un for con listas y condicionales |
| Avanzado | 🔴 | Problema integrador, como en el mundo real | Mini-juego, validador, herramienta util |

### Sistema de pistas

Cada ejercicio tiene 3 pistas progresivas. Usalas cuando te atores:

```bash
# Pista 1: Te dice por donde empezar (estructura general)
python scripts/runner.py 1 4 1 -p 1

# Pista 2: Te muestra el pseudocodigo o la logica clave
python scripts/runner.py 1 4 1 -p 2

# Pista 3: Te da una parte del codigo resuelto
python scripts/runner.py 1 4 1 -p 3
```

El objetivo es que llegues a la solucion por ti mismo. Las pistas son ayudas progresivas, no la respuesta final.

---

## Glosario General

Estos son terminos que aparecen desde el principio y que NO debes dar por sabidos. Si en cualquier momento ves un termino que no entiendes, vuelve aqui.

### Terminos fundamentales

| Termino | Que significa | Analogia |
|---------|---------------|----------|
| **Algoritmo** | Secuencia de pasos ordenados para resolver un problema | Una receta de cocina: pasos para hacer un pastel |
| **Programa** | Conjunto de instrucciones que una computadora ejecuta | Un manual de instrucciones para un robot |
| **Codigo fuente** | El texto que escribes en un lenguaje de programacion | Los ingredientes escritos en la receta |
| **Ejecutar/Correr** | Hacer que la computadora lea y ejecute tu codigo | Poner la receta en accion y cocinar |
| **Lenguaje de programacion** | Idioma artificial que usas para dar instrucciones a la computadora | El idioma en que esta escrita la receta (español, ingles...) |
| **Sintaxis** | Reglas de escritura de un lenguaje de programacion | La gramatica de un idioma: sujeto-verbo-predicado |
| **Compilar** | Traducir todo el codigo de una vez a lenguaje de maquina (Java) | Traducir un libro completo antes de leerlo |
| **Interpretar** | Traducir y ejecutar linea por linea (Python) | Traduccion simultanea: se traduce mientras se habla |

### Terminos de datos

| Termino | Que significa | Ejemplo |
|---------|---------------|---------|
| **Variable** | "Caja" donde guardas un dato. Tiene nombre y valor | `edad = 25` → la caja se llama "edad" y contiene 25 |
| **Tipo de dato** | Categoria del valor que guarda una variable: numero, texto, etc. | `25` es entero, `"Hola"` es texto (string) |
| **Entero / int** | Numero sin decimales | `42`, `-5`, `0` |
| **Float / decimal** | Numero con decimales | `3.14`, `-0.5` |
| **String / cadena** | Texto, siempre entre comillas | `"Hola mundo"`, `'Python'` |
| **Boolean / bool** | Solo puede ser `True` o `False` (verdadero o falso) | `5 > 3` → `True` |
| **Null / None** | Ausencia de valor, "vacio" | Una caja que existe pero esta vacia |
| **Expresion** | Combinacion de valores y operadores que producen un resultado | `(5 + 3) * 2` → `16` |

### Terminos de control de flujo

| Termino | Que significa | Ejemplo |
|---------|---------------|----------|
| **Condicional** | Estructura que ejecuta codigo SOLO si se cumple una condicion | `if edad >= 18: print("Mayor de edad")` |
| **Bucle / Loop** | Estructura que REPITE codigo multiples veces | `for i in range(5):` repite 5 veces |
| **Iteracion** | Cada repeticion individual dentro de un bucle | En un bucle de 5 vueltas, hay 5 iteraciones |
| **Indice** | Numero que indica la posicion de un elemento. **Siempre empieza en 0** | En `[10, 20, 30]`, el 10 esta en indice 0, el 20 en 1 |
| **Iterable** | Algo que se puede recorrer elemento por elemento (lista, string, rango) | `for letra in "Hola":` recorre cada caracter |
| **Range** | Funcion que genera una secuencia de numeros | `range(5)` genera `[0, 1, 2, 3, 4]` |

### Terminos de colecciones

| Termino | Que significa | Ejemplo |
|---------|---------------|----------|
| **Lista / Array** | Coleccion ordenada de elementos, puede cambiar | `[1, 2, 3]` |
| **Tupla** | Coleccion ordenada que NO puede cambiar | `(1, 2, 3)` |
| **Diccionario / Dict** | Coleccion de pares clave:valor | `{"nombre": "Ana", "edad": 25}` |
| **Set / Conjunto** | Coleccion SIN duplicados y SIN orden | `{1, 2, 3}` |
| **Mutable** | Que puede cambiar despues de creado | Las listas son mutables: `lista.append(4)` |
| **Inmutable** | Que NO puede cambiar despues de creado | Las tuplas son inmutables |
| **Clave / Key** | Identificador unico en un diccionario para acceder a un valor | En `{"nombre": "Ana"}`, la clave es `"nombre"` |
| **Valor / Value** | El dato asociado a una clave en un diccionario | En `{"nombre": "Ana"}`, el valor es `"Ana"` |

### Terminos de funciones

| Termino | Que significa | Ejemplo |
|---------|---------------|----------|
| **Funcion** | Bloque de codigo reutilizable con nombre propio | `def saludar():` |
| **Parametro** | Variable que recibe una funcion para trabajar con ella | `def suma(a, b):` → `a` y `b` son parametros |
| **Argumento** | Valor real que le pasas a la funcion al llamarla | `suma(5, 3)` → `5` y `3` son argumentos |
| **Retorno / Return** | Valor que devuelve la funcion para usarlo fuera | `return resultado` |
| **Scope / Ambito** | Region del codigo donde una variable existe y es accesible | Una variable dentro de una funcion solo existe alli |

---

## Los 11 Niveles

```
N1  ──→  N2  ──→  N3  ──→  N4  ──→  N5  ──→  N6
 │                            │        │
 └──────→  N7  ──→  N8  ──→  N9  ──→  N10 ──→  N11
```

| # | Nivel | Lenguaje | Que aprenderas |
|---|-------|----------|----------------|
| 1 | Fundamentos | Python | Logica, variables, control de flujo, funciones, colecciones |
| 2 | POO + SOLID | Java | Clases, herencia, polimorfismo, interfaces, SOLID |
| 3 | Estructuras de Datos | Python | Big O, listas, arboles, grafos, algoritmos de ordenamiento |
| 4 | Bases de Datos | SQL + Python | SQL, normalizacion, joins, transacciones, NoSQL |
| 5 | Backend y APIs | Python | HTTP, REST, JWT, JSON, redes |
| 6 | Frontend | HTML/CSS/JS | DOM, eventos, fetch, navegadores |
| 7 | Testing | Python | Unit tests, TDD, mocking, integracion |
| 8 | Patrones de Diseno | Java | Creacionales, estructurales, comportamiento, Clean Code |
| 9 | Arquitecturas | Teoria+Diagramas | Capas, hexagonal, microservicios, DDD |
| 10 | DevOps y Seguridad | Docker/Git/YAML | Git, Docker, CI/CD, OWASP, cifrado |
| 11 | Proyecto Final | Todos | App full-stack completa con todo lo aprendido |

---

## Estructura de cada tema

Cada tema tiene esta estructura:

```
📁 YY-tema/
├── 📖 README.md       → Teoria + glosario + comparativa + ejemplo guiado
├── 🎯 ejercicios.py   → Ejercicios con sistema de pistas
└── 🔍 soluciones.py   → Soluciones explicadas paso a paso
```

El README esta dividido en secciones claras:

```
1. TEORIA → Explicacion del concepto con ejemplos
2. GLOSARIO DEL TEMA → Terminos especificos de este tema
3. COMPARATIVA ENTRE LENGUAJES → Mismo concepto en Python, Java, JS
4. EJEMPLO GUIADO → Problema resuelto paso a paso
5. EJERCICIOS → Descripcion de los 3 ejercicios (🟢🟡🔴)
```

---

## Comparativa entre lenguajes

A lo largo del curso, cada concepto se muestra en los lenguajes que corresponden al nivel. Esto es INTENCIONAL: aprender a ver el patron detras de la sintaxis te hace un mejor programador.

```python
# Python
for i in range(5):
    print(i)
```

```java
// Java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

```javascript
// JavaScript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

Los tres hacen lo mismo (imprimir 0, 1, 2, 3, 4). Cambia la sintaxis, pero el **patron** es el mismo: inicializar, condicion, incremento.

---

## Requisitos

- **Python 3.8+** → `python --version`
- **Java 17+** → `java -version` y `javac -version`
- **SQLite3** (viene con Python)
- **Git** → `git --version`

> Ejecuta `python scripts/check-requirements.py` para verificar tu setup

## Empieza aqui

```bash
# 1. Verifica requisitos
python scripts/check-requirements.py

# 2. Abre el roadmap
code 00-roadmap/README.md

# 3. Comienza tu viaje en el Nivel 1
code 01-fundamentos-python/README.md
```

---

> *"El codigo es como el humor. Cuando tienes que explicarlo, es malo."* — Un sabio developer
