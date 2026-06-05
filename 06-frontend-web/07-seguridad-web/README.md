# Seguridad Web

## Introduccion

La seguridad web es fundamental para proteger a los usuarios y sus datos. Este modulo cubre las vulnerabilidades mas comunes y como prevenirlas.

## CORS (Cross-Origin Resource Sharing)

CORS es un mecanismo de seguridad del navegador que controla que origenes pueden acceder a recursos de un servidor.

### El problema del mismo origen (Same-Origin Policy)

```
  Pagina: https://miapp.com
       │
       │  fetch('https://miapp.com/api/datos')    -> PERMITIDO (mismo origen)
       │  fetch('https://api.otro.com/datos')      -> BLOQUEADO (otro origen)
       │  fetch('https://miapp.com:3000/datos')    -> BLOQUEADO (puerto diferente)
       │  fetch('http://miapp.com/datos')          -> BLOQUEADO (protocolo diferente)
       ▼
  NAVEGADOR bloquea la peticion a otro origen
```

### Solucion: Headers CORS en el servidor

```
  Access-Control-Allow-Origin: https://miapp.com
  Access-Control-Allow-Methods: GET, POST, PUT, DELETE
  Access-Control-Allow-Headers: Content-Type, Authorization
  Access-Control-Allow-Credentials: true
```

Para permitir cualquier origen (solo en desarrollo):
```
  Access-Control-Allow-Origin: *
```

## XSS (Cross-Site Scripting)

XSS ocurre cuando un atacante inserta codigo malicioso en una pagina web que otros usuarios van a ver.

### Tipos de XSS

| Tipo | Descripcion |
|------|-------------|
| **Reflejado** | El codigo malicioso viene en la URL (parametro GET) |
| **Almacenado** | El codigo se guarda en la BD (comentarios, perfiles) |
| **DOM-based** | La vulnerabilidad esta en el codigo JS del cliente |

### Ejemplo de XSS

```javascript
// VULNERABLE: el atacante puede inyectar <script>alert('XSS')</script>
const usuario = urlParams.get('usuario');
document.getElementById('saludo').innerHTML = 'Hola ' + usuario;

// SEGURO: textContent escapa el HTML
document.getElementById('saludo').textContent = 'Hola ' + usuario;
```

### Prevencion

1. Usar `textContent` en vez de `innerHTML` cuando sea posible
2. Sanitizar entrada del usuario (DOMPurify)
3. Escapar caracteres: `<` → `&lt;`, `>` → `&gt;`, `"` → `&quot;`
4. Content Security Policy (CSP)

## CSRF (Cross-Site Request Forgery)

CSRF ocurre cuando un sitio malicioso hace que el navegador de un usuario autenticado envie peticiones a otro sitio donde el usuario esta logueado.

### Como funciona

```
  1. Usuario logueado en bancoseguro.com (tiene cookie de sesion)
  2. Usuario visita sitiomalicioso.com
  3. sitiomalicioso.com tiene:
     <img src="https://bancoseguro.com/transferir?monto=10000&cuenta=12345">
  4. El navegador envia la peticion con la cookie automaticamente
  5. El banco procesa la transferencia (porque la cookie es valida)
```

### Prevencion

1. **CSRF Tokens**: Token unico generado por el servidor, incluido en formularios
2. **SameSite Cookies**: `Set-Cookie: sessionid=abc; SameSite=Strict`
3. **Verificar Referer/Origin header**
4. **No usar GET para acciones que modifican datos**

## Content Security Policy (CSP)

CSP es un header HTTP que permite controlar que recursos puede cargar una pagina.

```http
Content-Security-Policy: default-src 'self';
                         script-src 'self' https://apis.google.com;
                         style-src 'self' https://fonts.googleapis.com;
                         img-src 'self' data:;
                         font-src 'self' https://fonts.gstatic.com;
                         connect-src 'self' https://api.miapp.com;
```

### Directivas comunes

| Directiva | Controla |
|-----------|----------|
| `default-src` | Recurso por defecto si no hay directiva especifica |
| `script-src` | Fuentes permitidas para scripts |
| `style-src` | Fuentes permitidas para CSS |
| `img-src` | Fuentes permitidas para imagenes |
| `connect-src` | URL permitidas para fetch, XHR, WebSocket |
| `font-src` | Fuentes permitidas para tipografias |
| `frame-src` | Fuentes permitidas para iframes |

## HTTPS

HTTPS cifra la comunicacion entre el navegador y el servidor usando TLS/SSL.

```
  HTTP (sin cifrar)                HTTPS (cifrado)
  ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
  │ Cliente │────▶│  Texto  │     │ Cliente │────▶│ Cifrado │
  │         │     │  plano  │     │         │     │ TLS     │
  └─────────┘     └─────────┘     └─────────┘     └─────────┘
  Cualquiera en la red puede      Solo el servidor puede
  leer los datos                  descifrar los datos
```

### Beneficios

- **Confidencialidad**: Los datos viajan cifrados
- **Integridad**: Los datos no pueden ser modificados en transito
- **Autenticacion**: El cliente verifica que el servidor es quien dice ser (certificados)

## Same-Origin Policy

Politica de seguridad fundamental del navegador. Un origen se define por: protocolo + dominio + puerto.

```
  https://miapp.com:443
  │        │      │
  │        │      └── Puerto
  │        └───────── Dominio
  └─────────────────── Protocolo
```

### Que esta permitido entre origenes?

| Accion | Permitido? |
|--------|-----------|
| Escribir en iframe de otro origen | Si (formularios, enlaces) |
| Leer contenido de iframe de otro origen | NO |
| Hacer fetch a otro origen | NO (sin CORS) |
| Cargar scripts (script src) | Si |
| Cargar imagenes (img src) | Si |
| Cargar CSS (link href) | Si |

## Buenas practicas de seguridad

1. **Validacion del lado del servidor**: Nunca confies solo en validacion del cliente
2. **Parametrizacion de consultas SQL**: Prevenir SQL Injection
3. **Hash de contrasenas**: Usar bcrypt, no SHA1/MD5
4. **Principio de minimo privilegio**: Solo dar los permisos necesarios
5. **Mantener dependencias actualizadas**: npm audit, dependabot
6. **Usar Helmet.js** (Express): Agrega headers de seguridad automaticamente
7. **Rate limiting**: Limitar peticiones por IP para prevenir ataques de fuerza bruta

## Ejercicios

Abre `ejercicios.html` en tu navegador y completa los 3 ejercicios.
