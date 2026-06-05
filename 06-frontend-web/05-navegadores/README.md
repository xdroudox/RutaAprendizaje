# Navegadores: Como funcionan por dentro

## Introduccion

El navegador es el entorno de ejecucion mas importante para el desarrollo web. Entender como funciona te permite optimizar rendimiento, depurar problemas y escribir mejor codigo.

## Arquitectura del navegador

```
  +----------------------------------------------------------+
  |                     NAVEGADOR                             |
  |                                                          |
  |  +------------------+  +------------------+              |
  |  |   User Interface |  |   Browser Engine |              |
  |  |  (barra dir,     |  |  (controla       |              |
  |  |   botones, etc)  |  |   interaccion)   |              |
  |  +------------------+  +--------+---------+              |
  |                                  |                        |
  |  +-------------------------------+------------------+    |
  |  |                    Rendering Engine               |    |
  |  |  +----------+  +----------+  +----------------+  |    |
  |  |  | HTML     |  | CSS      |  | Layout / Paint |  |    |
  |  |  | Parser   |  | Parser   |  | (reflow,       |  |    |
  |  |  | (DOM)    |  | (CSSOM)  |  |  repaint)      |  |    |
  |  |  +----------+  +----------+  +----------------+  |    |
  |  +--------------------------------------------------+    |
  |                                                          |
  |  +------------------+  +------------------+              |
  |  | JavaScript Engine |  |   Networking     |              |
  |  | (V8, SpiderMonkey)|  |   (HTTP, cache)  |              |
  |  +------------------+  +------------------+              |
  |                                                          |
  |  +------------------+  +------------------+              |
  |  |   UI Backend     |  |   Data Storage   |              |
  |  |  (dibuja widgets)|  |  (localStorage,   |              |
  |  |                  |  |   cookies, IndexDB)|             |
  |  +------------------+  +------------------+              |
  +----------------------------------------------------------+
```

## Pipeline de Rendering

Cuando el navegador carga una pagina, sigue estos pasos:

```
  HTML  ──→  Parse HTML  ──→  DOM Tree
  CSS   ──→  Parse CSS   ──→  CSSOM Tree
                                   │
                                   ▼
                            Render Tree
                            (DOM + CSSOM combinados)
                                   │
                                   ▼
                              Layout (Reflow)
                            (calcula posiciones
                             y tamanos)
                                   │
                                   ▼
                              Paint (Repaint)
                            (dibuja pixeles en
                             pantalla)
                                   │
                                   ▼
                              Composicion
                            (capas: GPU)
```

### 1. Parseo HTML y construccion del DOM

El navegador lee el HTML byte por byte y lo convierte en tokens, luego en nodos, y finalmente en un arbol DOM (Document Object Model).

```html
<html>
  <body>
    <h1>Titulo</h1>
    <p>Parrafo</p>
  </body>
</html>
```

Se convierte en:
```
document
 └── html
      └── body
           ├── h1  ("Titulo")
           └── p   ("Parrafo")
```

### 2. Parseo CSS y construccion del CSSOM

Similar al DOM, el CSS se parsea en un CSSOM (CSS Object Model) que contiene todas las reglas de estilo.

```css
h1 { color: blue; font-size: 24px; }
p { color: gray; }
```

### 3. Render Tree

Combina DOM + CSSOM. Solo incluye los elementos visibles (excluye `display: none`).

### 4. Layout (Reflow)

Calcula la posicion y tamano de cada elemento en la pantalla. Es uno de los procesos mas costosos.

**Que causa Reflow:**
- Cambiar tamano de ventana
- Manipular el DOM (agregar/eliminar elementos)
- Cambiar estilos que afectan layout (width, height, margin, padding, display, position)
- Leer propiedades como offsetHeight, offsetWidth (fuerza reflow)

### 5. Paint (Repaint)

Dibuja los pixeles: colores, fondos, sombras, bordes. No recalcula posiciones.

**Que causa Repaint:**
- Cambiar color, background-color, visibility, outline
- Cambiar box-shadow (si es muy complejo)

### 6. Composicion

El navegador divide la pagina en capas y las combina en la GPU para renderizado fluido (60fps). Propiedades como `transform` y `opacity` solo afectan la composicion, no causan reflow ni repaint.

## JavaScript Engine (V8)

V8 es el motor JavaScript de Chrome (tambien usado en Node.js). Funciona asi:

```
  JavaScript Source
       │
       ▼
    Parser ──→ AST (Abstract Syntax Tree)
       │
       ▼
  Interpreter (Ignition) ──→ Bytecode
       │
       ▼
  Compiler (TurboFan) ──→ Optimized Machine Code
       │
       ▼
    Execution
```

### Caracteristicas de V8

- **JIT Compilation**: Compila JavaScript a codigo maquina justo antes de ejecutarlo
- **Garbage Collection**: Libera memoria automaticamente (GC generacional)
- **Inline Caching**: Optimiza acceso a propiedades repetidas
- **Hidden Classes**: Asigna tipos internos a objetos para acelerar acceso

## Event Loop

JavaScript es single-threaded (un solo hilo), pero puede manejar operaciones asincronas gracias al Event Loop.

```
  ┌─────────────┐      ┌─────────────┐
  │ Call Stack  │      │  Web APIs   │
  │ (pila de    │      │ (setTimeout, │
  │  ejecucion) │      │  fetch, DOM)│
  └──────┬──────┘      └──────┬──────┘
         │                    │
         ▼                    ▼
  ┌───────────────────────────────────┐
  │         Callback Queue            │
  │  [macro: click, setTimeout]       │
  │  [micro: Promise.then]            │
  └───────────────┬───────────────────┘
                  │
                  ▼
  Event Loop: Si Call Stack esta vacio,
  mueve tareas de Queue a Stack
```

### Microtasks vs Macrotasks

```javascript
console.log('1');  // Sincrono

setTimeout(() => console.log('2'), 0);  // Macrotask

Promise.resolve().then(() => console.log('3'));  // Microtask

console.log('4');  // Sincrono

// Salida: 1, 4, 3, 2
```

Las microtasks (Promises) tienen prioridad sobre las macrotasks (setTimeout).

## localStorage y SessionStorage

### localStorage
- Persiste aunque se cierre el navegador
- Capacidad: ~5-10MB
- Solo strings
- Sincrono

```javascript
// Guardar
localStorage.setItem('nombre', 'Juan');
localStorage.setItem('objeto', JSON.stringify({a: 1, b: 2}));

// Leer
const nombre = localStorage.getItem('nombre');
const objeto = JSON.parse(localStorage.getItem('objeto'));

// Eliminar
localStorage.removeItem('nombre');
localStorage.clear(); // elimina todo
```

### sessionStorage
- Se borra al cerrar la pestana
- Misma API que localStorage

```javascript
sessionStorage.setItem('temporal', 'dato');
```

### Cookies vs Web Storage

| Caracteristica | Cookies | localStorage | sessionStorage |
|----------------|---------|--------------|----------------|
| Capacidad | 4KB | ~5-10MB | ~5-10MB |
| Envia al servidor | Si (cada request) | No | No |
| Persistencia | Configurable | Si | No (al cerrar pestana) |
| Acceso | JS + HTTP | Solo JS | Solo JS |

## Cuestionario (Auto-evaluacion)

Responde las siguientes preguntas para verificar tu comprension:

### Pregunta 1
Que etiqueta HTML se usa para contenido independiente como un blog post o una noticia?

a) `<section>`
b) `<article>`
c) `<div>`
d) `<main>`

<details>
<summary>Ver respuesta</summary>
b) `<article>` - Representa contenido independiente y auto-contenido.
</details>

### Pregunta 2
Que propiedad CSS de Flexbox centra elementos en el eje principal (horizontal por defecto)?

a) `align-items`
b) `justify-content`
c) `text-align`
d) `flex-center`

<details>
<summary>Ver respuesta</summary>
b) `justify-content: center` - Centra en el eje principal.
</details>

### Pregunta 3
Que metodo de JavaScript se usa para crear un nuevo elemento HTML en el DOM?

a) `document.newElement()`
b) `document.createElement()`
c) `document.makeElement()`
d) `document.buildElement()`

<details>
<summary>Ver respuesta</summary>
b) `document.createElement('div')` - Crea un nuevo elemento en memoria.
</details>

### Pregunta 4
Cual es la diferencia entre `textContent` e `innerHTML`?

a) No hay diferencia
b) `textContent` interpreta HTML, `innerHTML` no
c) `textContent` solo texto (seguro), `innerHTML` interpreta etiquetas HTML
d) `textContent` es mas lento

<details>
<summary>Ver respuesta</summary>
c) `textContent` asigna solo texto (escapa HTML), `innerHTML` interpreta etiquetas.
</details>

### Pregunta 5
Que metodo detiene la propagacion de un evento?

a) `e.preventDefault()`
b) `e.stopPropagation()`
c) `e.stopImmediate()`
d) `e.cancelBubble = true` (ambas b y d funcionan)

<details>
<summary>Ver respuesta</summary>
b) `e.stopPropagation()` y d) `e.cancelBubble = true` - Ambos detienen el burbujeo.
</details>

### Pregunta 6
Que es una Promise en JavaScript?

a) Una funcion que se ejecuta inmediatamente
b) Un objeto que representa la finalizacion (o falla) de una operacion asincrona
c) Una variable global
d) Un tipo de bucle

<details>
<summary>Ver respuesta</summary>
b) Una Promise es un objeto que representa un valor futuro (exito o error).
</details>

### Pregunta 7
Que proceso del pipeline de rendering calcula las posiciones y tamanos de los elementos?

a) Paint
b) Parse
c) Layout (Reflow)
d) Composicion

<details>
<summary>Ver respuesta</summary>
c) Layout (Reflow) - Calcula geometria de los elementos.
</details>

### Pregunta 8
Cual de estos NO causa reflow?

a) Cambiar `width` de un elemento
b) Cambiar `color` de un elemento
c) Agregar un elemento al DOM
d) Cambiar tamano de ventana

<details>
<summary>Ver respuesta</summary>
b) Cambiar `color` solo causa repaint (no afecta layout).
</details>

### Pregunta 9
Que almacena datos que persisten incluso despues de cerrar el navegador?

a) `sessionStorage`
b) `localStorage`
c) Variables globales
d) `sessionStorage` y `localStorage`

<details>
<summary>Ver respuesta</summary>
b) `localStorage` persiste los datos incluso al cerrar el navegador.
</details>

### Pregunta 10
Que es CSS Grid?

a) Un sistema de layout unidimensional
b) Un sistema de layout bidimensional (filas y columnas)
c) Un framework CSS
d) Una propiedad para colores

<details>
<summary>Ver respuesta</summary>
b) CSS Grid es un sistema de layout bidimensional que permite controlar filas y columnas.
</details>

---

## Preguntas de reflexion

Responde estas preguntas para profundizar tu comprension:

### Pregunta 1: DOM vs CSSOM
Explica la diferencia entre el DOM y el CSSOM. En que etapa del pipeline de rendering se combinan y cual es el resultado?

### Pregunta 2: Reflow vs Repaint
Un desarrollador cambia el `width` de un elemento y luego su `color`. Cual de estos cambios causa reflow y cual causa solo repaint? Por que es importante minimizar los reflows?

### Pregunta 3: Event Loop
Dado el siguiente codigo, explica en que orden se imprimen los mensajes y por que:
```javascript
console.log('Inicio');
setTimeout(() => console.log('Timeout'), 0);
Promise.resolve().then(() => console.log('Promise'));
console.log('Fin');
```
