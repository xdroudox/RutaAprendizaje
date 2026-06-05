# JavaScript DOM

## Que es el DOM?

DOM (Document Object Model) es una representacion en memoria del documento HTML. JavaScript puede manipularlo para cambiar contenido, estilo y estructura en tiempo real.

```
    NAVEGADOR
    +--------------------------------------------------+
    |  Document (DOM)                                   |
    |  +--------------------------------------------+  |
    |  | html                                       |  |
    |  |  +--------------------------------------+  |  |
    |  |  | head                                |  |  |
    |  |  +--------------------------------------+  |  |
    |  |  +--------------------------------------+  |  |
    |  |  | body                                |  |  |
    |  |  |  +--------------------------------+  |  |  |
    |  |  |  | div#app                        |  |  |  |
    |  |  |  |  +--------+  +--------+        |  |  |  |
    |  |  |  |  |  h1    |  |  p     |        |  |  |  |
    |  |  |  |  +--------+  +--------+        |  |  |  |
    |  |  |  +--------------------------------+  |  |  |
    |  |  +--------------------------------------+  |  |
    |  +--------------------------------------------+  |
    +--------------------------------------------------+
```

## Seleccionar elementos

### getElementById
```javascript
const titulo = document.getElementById('titulo');
// Devuelve un elemento (o null si no existe)
```

### querySelector / querySelectorAll
```javascript
const primerParrafo = document.querySelector('p');
const todosLosParrafos = document.querySelectorAll('p');
const elemento = document.querySelector('.clase');
const item = document.querySelector('#lista li:first-child');
```

## Manipular contenido

```javascript
const div = document.getElementById('app');

div.textContent = 'Hola Mundo';      // Solo texto (seguro, escapa HTML)
div.innerHTML = '<b>Hola</b>';       // Interpreta HTML (cuidado con XSS)
div.innerText = 'Texto visible';     // Como textContent pero respeta CSS
```

## Crear y agregar elementos

```javascript
const nuevoParrafo = document.createElement('p');
nuevoParrafo.textContent = 'Soy nuevo';
nuevoParrafo.classList.add('destacado');
document.body.appendChild(nuevoParrafo);

// Insertar en una posicion especifica
const referencia = document.querySelector('#lista li:first-child');
referencia.before(nuevoParrafo);     // Antes
referencia.after(nuevoParrafo);      // Despues
referencia.prepend(nuevoParrafo);    // Primer hijo
referencia.append(nuevoParrafo);     // Ultimo hijo
```

## Manipular estilos y atributos

```javascript
elemento.style.color = 'red';
elemento.style.backgroundColor = '#f0f0f0';
elemento.classList.add('activo');
elemento.classList.remove('inactivo');
elemento.classList.toggle('visible');

elemento.setAttribute('data-id', '123');
elemento.getAttribute('data-id');    // "123"
elemento.removeAttribute('disabled');
```

## Navegar el DOM

```javascript
const elemento = document.querySelector('li');

elemento.parentElement;              // Nodo padre
elemento.children;                   // Coleccion de hijos
elemento.firstElementChild;          // Primer hijo
elemento.lastElementChild;           // Ultimo hijo
elemento.nextElementSibling;         // Siguiente hermano
elemento.previousElementSibling;     // Hermano anterior
```

## Ejemplo completo

```html
<!DOCTYPE html>
<html>
<body>
    <div id="app">
        <h1>Lista de Tareas</h1>
        <ul id="lista">
            <li>Aprender DOM</li>
        </ul>
        <input id="nuevaTarea" placeholder="Nueva tarea">
        <button id="btnAgregar">Agregar</button>
    </div>

    <script>
        const btn = document.getElementById('btnAgregar');
        const lista = document.getElementById('lista');
        const input = document.getElementById('nuevaTarea');

        btn.addEventListener('click', () => {
            const texto = input.value.trim();
            if (texto === '') return;

            const li = document.createElement('li');
            li.textContent = texto;
            lista.appendChild(li);
            input.value = '';
        });
    </script>
</body>
</html>
```

## Ejercicios

### Ejercicio 1: Manipular texto y estilos con DOM
Usa document.getElementById(), .textContent y .classList.add() para cambiar el texto y aplicar estilos.
**Ejecuta:** `python scripts/runner.py 6 3 1`
**O abre directo:** `06-frontend-web/03-javascript-dom/ejercicios.html`

### Ejercicio 2: Crear elementos con createElement y appendChild
Crea nuevos elementos HTML dinamicamente usando createElement, classList.add y appendChild.
**Ejecuta:** `python scripts/runner.py 6 3 2`
**O abre directo:** `06-frontend-web/03-javascript-dom/ejercicios.html`

### Ejercicio 3: Lista de tareas interactiva (to-do list)
Construye una to-do list completa: agregar tareas, eliminar y marcar como completadas.
**Ejecuta:** `python scripts/runner.py 6 3 3`
**O abre directo:** `06-frontend-web/03-javascript-dom/ejercicios.html`
