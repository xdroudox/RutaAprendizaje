# Eventos y Asincronia en JavaScript

## Eventos del DOM

Los eventos son acciones que ocurren en el navegador: clics, tecleo, movimiento del raton, carga de pagina, etc.

### addEventListener

```javascript
const boton = document.getElementById('miBoton');

boton.addEventListener('click', function(event) {
    console.log('Boton clickeado');
    console.log(event.target); // elemento que disparo el evento
});
```

### Eventos comunes

| Evento | Descripcion |
|--------|-------------|
| `click` | Clic del raton |
| `dblclick` | Doble clic |
| `mouseenter` / `mouseleave` | Raton entra/sale de un elemento |
| `keydown` / `keyup` | Tecla presionada/soltada |
| `submit` | Formulario enviado |
| `change` | Valor de input cambiado |
| `input` | Cada vez que se escribe en un input |
| `load` | Pagina o recurso cargado |
| `scroll` | Scroll de la pagina |
| `focus` / `blur` | Elemento gana/pierde foco |

### Event object

```javascript
elemento.addEventListener('click', function(e) {
    e.preventDefault();    // Evita comportamiento default
    e.stopPropagation();   // Detiene la propagacion (burbujeo)
    console.log(e.type);   // Tipo de evento
    console.log(e.target); // Elemento que recibio el evento
    console.log(e.key);    // Tecla presionada (keydown/keyup)
});
```

## Asincronia en JavaScript

JavaScript es de un solo hilo (single thread), pero puede manejar operaciones asincronas mediante:
1. Callbacks
2. Promises
3. async/await

### Callbacks

```javascript
function saludar(nombre, callback) {
    console.log('Hola ' + nombre);
    callback();
}

function despedida() {
    console.log('Adios!');
}

saludar('Juan', despedida);
// "Hola Juan"
// "Adios!"
```

### setTimeout y setInterval

```javascript
// Ejecuta una vez despues de N milisegundos
setTimeout(function() {
    console.log('Pasaron 2 segundos');
}, 2000);

// Ejecuta cada N milisegundos
const intervalo = setInterval(function() {
    console.log('Cada 1 segundo');
}, 1000);

// Detener el intervalo
clearInterval(intervalo);
```

### Promises

```javascript
const promesa = new Promise(function(resolve, reject) {
    const exito = true;

    if (exito) {
        resolve('Operacion exitosa');
    } else {
        reject('Algo salio mal');
    }
});

promesa
    .then(function(resultado) {
        console.log(resultado); // "Operacion exitosa"
    })
    .catch(function(error) {
        console.error(error);   // "Algo salio mal"
    })
    .finally(function() {
        console.log('Siempre se ejecuta');
    });
```

### async / await

```javascript
function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function ejecutar() {
    console.log('Inicio');
    await esperar(2000);
    console.log('Pasaron 2 segundos');
    await esperar(1000);
    console.log('Pasaron 3 segundos en total');
}

ejecutar();

// Manejo de errores con try/catch
async function obtenerDatos() {
    try {
        const respuesta = await fetch('https://api.example.com/datos');
        const datos = await respuesta.json();
        console.log(datos);
    } catch (error) {
        console.error('Error:', error);
    }
}
```

## El Event Loop

```
    Call Stack                Web APIs
    +-----------+            +-----------+
    | script    |            | setTimeout |
    | console   |            | fetch     |
    |           |            | click     |
    +-----------+            +-----------+
          |                       |
          ▼                       ▼
    +-------------------------------+
    |        Callback Queue         |
    |  [callback1, callback2, ...]  |
    +-------------------------------+
          |
          ▼ (Event Loop mueve tareas cuando Call Stack esta vacio)
    +-----------+
    | Call Stack|
    +-----------+
```

## Ejercicios

Abre `ejercicios.html` en tu navegador y completa los 3 ejercicios.
