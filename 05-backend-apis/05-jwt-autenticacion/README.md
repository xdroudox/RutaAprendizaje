# JWT y Autenticacion

## Contenido
- Estructura de un JWT (header.payload.firma)
- Codificacion Base64 URL-safe
- Claims (sub, iat, exp)
- Verificacion de expiracion

---

## 1. Que es JWT?

JWT (JSON Web Token) es un estandar (RFC 7519) para crear tokens de autenticacion que contienen informacion en formato JSON, codificada en Base64 y firmada digitalmente.

### Estructura
```
header.payload.firma
```

Cada parte es un JSON codificado en Base64 URL-safe y separado por puntos.

### Header
```json
{"alg": "HS256", "typ": "JWT"}
```
- `alg`: algoritmo de firma (HS256, RS256, etc.)
- `typ`: tipo de token (JWT)

### Payload (claims)
```json
{"sub": "123", "name": "Ana", "iat": 1700000000, "exp": 1700003600}
```
- `sub` (subject): identificador del usuario
- `iat` (issued at): timestamp de creacion
- `exp` (expiration): timestamp de expiracion
- `name`, `email`, `role`: claims personalizados

### Firma
Se genera con el algoritmo especificado en el header usando una clave secreta. Esto evita que el token sea modificado sin deteccion.

---

## 2. Flujo de autenticacion con JWT

```
1. Login:   Usuario envia credenciales → Servidor valida → genera JWT
2. Almacen: Cliente guarda el JWT (localStorage, cookie)
3. Request: Cliente envia JWT en header: Authorization: Bearer <token>
4. Verify:  Servidor verifica firma y claims → procesa request
```

---

## 3. Glosario

| Termino     | Definicion |
|------------|-----------|
| **JWT**    | JSON Web Token - formato de token de autenticacion |
| **Claim**  | Declaracion dentro del payload del JWT |
| **sub**    | Subject - identificador del usuario |
| **iat**    | Issued At - timestamp de creacion |
| **exp**    | Expiration - timestamp de expiracion |
| **Base64 URL-safe** | Codificacion Base64 que reemplaza +/ por -_ y quita = |
| **HMAC**   | Hash-based Message Authentication Code (firma simetrica) |

---

## 4. Comparativa entre lenguajes

### Python (PyJWT)
```python
import jwt
token = jwt.encode({"sub": "123", "name": "Ana"}, "secreto", algorithm="HS256")
datos = jwt.decode(token, "secreto", algorithms=["HS256"])
```

### JavaScript (jsonwebtoken)
```javascript
const token = jwt.sign({sub: "123", name: "Ana"}, "secreto");
const datos = jwt.verify(token, "secreto");
```

### Java (jjwt)
```java
String token = Jwts.builder().setSubject("123").claim("name", "Ana")
    .signWith(SignatureAlgorithm.HS256, "secreto").compact();
```

---

## 5. Ejemplo guiado paso a paso

**Problema:** Crear un JWT para el usuario Ana (id=123) que expire en 1 hora.

1. Crear header: `{"alg": "HS256", "typ": "JWT"}`
2. Crear payload: `{"sub": "123", "name": "Ana", "iat": now, "exp": now+3600}`
3. Codificar header y payload en Base64 URL-safe
4. Firmar con HMAC usando clave secreta
5. Concatenar: `base64(header).base64(payload).base64(firma)`

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Crear JWT simple (header.payload.firma) | 🟢 |
| 2  | Decodificar JWT y extraer payload | 🟡 |
| 3  | Verificar expiracion de JWT | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 5 1
python scripts/runner.py 5 5 2
python scripts/runner.py 5 5 3
python scripts/runner.py 5 5 1 -p 1
python scripts/runner.py 5 5 3 -s
```
