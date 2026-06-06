# Protocolo HTTP

## Contenido
- Estructura de una URL
- Metodos HTTP (GET, POST, PUT, DELETE)
- Formato de Request y Response HTTP
- Headers, body, status codes

---

## 1. Que es HTTP?

HTTP (HyperText Transfer Protocol) es el protocolo de comunicacion entre clientes (navegadores, apps) y servidores web. Usa un modelo **request-response sin estado** (cada request es independiente).

### Flujo basico
```
Cliente                    Servidor
   |                          |
   |---- REQUEST ----------->|
   |                          |
   |<--- RESPONSE ------------|
   |                          |
```

---

## 2. Estructura de una URL

`esquema://host:puerto/ruta?query=valor#fragmento`

| Componente  | Ejemplo            | Descripcion |
|-------------|-------------------|-------------|
| esquema     | `https`           | Protocolo (http, https, ftp) |
| host        | `api.ejemplo.com` | Dominio o IP |
| puerto      | `:443`            | Opcional (default: 80 http, 443 https) |
| ruta        | `/usuarios`       | Recurso en el servidor |
| query       | `?rol=admin`      | Parametros clave=valor (& separa multiples) |
| fragmento   | `#seccion`        | Seccion interna del recurso (no se envia al servidor) |

---

## 3. Metodos HTTP

| Metodo  | Proposito          | Tiene body? | Idempotente? | Ejemplo |
|---------|-------------------|-------------|-------------|---------|
| **GET**    | Obtener recurso    | No          | Si          | `GET /usuarios` |
| **POST**   | Crear recurso      | Si          | No          | `POST /usuarios` con JSON |
| **PUT**    | Reemplazar recurso | Si          | Si          | `PUT /usuarios/1` |
| **DELETE** | Eliminar recurso   | No          | Si          | `DELETE /usuarios/1` |

> **Idempotente:** multiples requests identicos producen el mismo resultado que uno solo.

---

## 4. Request HTTP

```
POST /api/usuarios HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json
Authorization: Bearer token123

{"nombre": "Ana", "email": "ana@ejemplo.com"}
```

Partes:
- **Linea inicial:** `METODO RUTA HTTP/version`
- **Headers:** metadatos en formato `Clave: Valor`
- **Linea vacia:** separa headers del body
- **Body:** datos (solo POST/PUT)

---

## 5. Response HTTP

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 45

{"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com"}
```

Partes:
- **Linea inicial:** `HTTP/version CODIGO MENSAJE`
- **Headers:** metadatos de la respuesta
- **Body:** datos solicitados

---

## 6. Glosario

| Termino        | Definicion |
|---------------|-----------|
| **HTTP**      | Protocolo de transferencia de hipertexto |
| **URL**       | Localizador uniforme de recursos |
| **Request**   | Peticion del cliente al servidor |
| **Response**  | Respuesta del servidor al cliente |
| **Header**    | Metadato en formato clave:valor |
| **Body**      | Cuerpo del mensaje (datos) |
| **Idempotente** | Multiples requests identicos = mismo resultado |
| **Stateless** | Cada request es independiente, no hay estado previo |

---

## 7. Comparativa entre lenguajes

### Python (http.client / urllib)
```python
import http.client
conn = http.client.HTTPSConnection("api.ejemplo.com")
conn.request("GET", "/usuarios")
resp = conn.getresponse()
print(resp.status, resp.read().decode())
```

### JavaScript (fetch)
```javascript
fetch("https://api.ejemplo.com/usuarios")
  .then(res => res.json())
  .then(data => console.log(data));
```

### Java (HttpURLConnection)
```java
URL url = new URL("https://api.ejemplo.com/usuarios");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("GET");
int status = conn.getResponseCode();
```

---

## 8. Ejemplo guiado paso a paso

**Problema:** Hacer un GET a `https://api.ejemplo.com/usuarios?rol=admin`

1. El cliente construye la URL: `https://api.ejemplo.com/usuarios?rol=admin`
2. Abre conexion TCP al host `api.ejemplo.com` en puerto 443 (HTTPS)
3. Envia request HTTP:
   ```
   GET /usuarios?rol=admin HTTP/1.1
   Host: api.ejemplo.com
   Accept: application/json
   ```
4. El servidor procesa y responde:
   ```
   HTTP/1.1 200 OK
   Content-Type: application/json
   
   [{"id": 1, "nombre": "Ana", "rol": "admin"}]
   ```
5. El cliente lee y procesa la respuesta

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Construir URL desde componentes | 🟢 |
| 2  | Simular request HTTP como diccionario | 🟡 |
| 3  | Parsear response HTTP desde string | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 1 1
python scripts/runner.py 5 1 2
python scripts/runner.py 5 1 3
python scripts/runner.py 5 1 1 -p 1   # Pista 1
python scripts/runner.py 5 1 3 -s     # Solucion
```
