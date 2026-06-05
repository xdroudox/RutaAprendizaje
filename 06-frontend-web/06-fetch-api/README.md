# Fetch API

## Que es Fetch API?

Fetch API es la forma moderna de hacer peticiones HTTP desde el navegador. Reemplazo a XMLHttpRequest (XHR). Usa Promises, lo que facilita el manejo de respuestas asincronas.

## Sintaxis basica

```javascript
fetch(url, opciones)
    .then(function(respuesta) {
        // Manejar la respuesta
    })
    .catch(function(error) {
        // Manejar errores de red
    });
```

Con async/await:

```javascript
async function obtenerDatos() {
    try {
        const respuesta = await fetch(url);
        const datos = await respuesta.json();
        console.log(datos);
    } catch (error) {
        console.error('Error:', error);
    }
}
```

## Metodos HTTP

### GET (obtener datos)

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then(respuesta => respuesta.json())
    .then(datos => console.log(datos));
// { userId: 1, id: 1, title: "...", body: "..." }
```

### POST (crear datos)

```javascript
fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        title: 'Nuevo Post',
        body: 'Contenido del post',
        userId: 1
    })
})
    .then(respuesta => respuesta.json())
    .then(datos => console.log('Creado:', datos));
```

### PUT (actualizar datos)

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        id: 1,
        title: 'Actualizado',
        body: 'Nuevo contenido',
        userId: 1
    })
});
```

### DELETE (eliminar datos)

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1', {
    method: 'DELETE'
});
```

## Manejo de respuestas

```javascript
async function manejarRespuesta() {
    const respuesta = await fetch('https://api.example.com/datos');

    console.log(respuesta.status);      // 200, 404, 500, etc.
    console.log(respuesta.ok);          // true si status es 200-299
    console.log(respuesta.headers.get('Content-Type'));

    if (!respuesta.ok) {
        throw new Error('Error HTTP: ' + respuesta.status);
    }

    // Diferentes formatos de respuesta
    const json = await respuesta.json();        // JSON
    const texto = await respuesta.text();       // Texto plano
    const blob = await respuesta.blob();        // Archivos binarios
    const formData = await respuesta.formData(); // FormData
}
```

## CORS (Cross-Origin Resource Sharing)

CORS es un mecanismo de seguridad del navegador que controla las peticiones entre diferentes origenes.

```
  Navegador (origin: https://miapp.com)
       │
       │  fetch('https://api.otrodominio.com/datos')
       ▼
  El navegador envia un preflight (OPTIONS) si es necesario
       │
       ▼
  El servidor responde con headers CORS:
  Access-Control-Allow-Origin: https://miapp.com
  Access-Control-Allow-Methods: GET, POST
  Access-Control-Allow-Headers: Content-Type
       │
       ▼
  Si los headers son correctos, el navegador permite la peticion
```

## JSONPlaceholder (API de prueba)

Usaremos JSONPlaceholder para los ejercicios:
- `GET https://jsonplaceholder.typicode.com/posts` - Listar posts
- `GET https://jsonplaceholder.typicode.com/posts/1` - Un post
- `POST https://jsonplaceholder.typicode.com/posts` - Crear post
- `GET https://jsonplaceholder.typicode.com/users` - Listar usuarios

## Ejercicios

### Ejercicio 1: GET request con fetch
Usa fetch() para obtener los primeros 5 posts de JSONPlaceholder y muestralos en pantalla.
**Ejecuta:** `python scripts/runner.py 6 6 1`
**O abre directo:** `06-frontend-web/06-fetch-api/ejercicios.html`

### Ejercicio 2: POST request con JSON body
Envia un POST a JSONPlaceholder con los datos del formulario usando method, headers y body.
**Ejecuta:** `python scripts/runner.py 6 6 2`
**O abre directo:** `06-frontend-web/06-fetch-api/ejercicios.html`

### Ejercicio 3: Manejar errores de fetch con catch
Usa async/await con try/catch y verifica respuesta.ok para manejar errores HTTP y de red.
**Ejecuta:** `python scripts/runner.py 6 6 3`
**O abre directo:** `06-frontend-web/06-fetch-api/ejercicios.html`
