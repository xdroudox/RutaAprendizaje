# JWT y Autenticacion

JWT (JSON Web Token) es un estandar abierto (RFC 7519) para transmitir
informacion entre partes como un objeto JSON firmado digitalmente.

## Estructura de un JWT

Un JWT tiene tres partes separadas por puntos:

```
header.payload.signature
```

### Header

Indica el algoritmo de firma y el tipo de token.

```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

### Payload

Contiene los claims (declaraciones) sobre el usuario y metadatos.

```json
{
    "sub": "1234567890",
    "name": "Ana Lopez",
    "iat": 1516239022,
    "exp": 1516242622
}
```

Claims comunes:
- sub: subject (identificador del usuario)
- iat: issued at (creado en)
- exp: expiration (expiracion)
- iss: issuer (emisor)
- aud: audience (destinatario)

### Signature

Se genera codificando header y payload en base64url y firmando con
el algoritmo especificado.

```
HMACSHA256(
    base64UrlEncode(header) + "." + base64UrlEncode(payload),
    secret
)
```

## Como funciona

1. El usuario inicia sesion con credenciales
2. El servidor verifica las credenciales y genera un JWT
3. El cliente almacena el JWT (localStorage, cookie)
4. El cliente envia el JWT en cada peticion (header Authorization)
5. El servidor verifica la firma del JWT en cada peticion

```python
import hashlib, base64, json

def crear_jwt(payload, secreto):
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).rstrip(b"=").decode()
    payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=").decode()
    firma_input = f"{header_b64}.{payload_b64}".encode()
    firma = hashlib.sha256(firma_input + secreto.encode()).hexdigest()
    return f"{header_b64}.{payload_b64}.{firma}"
```

## Refresh Tokens

- Access token: corta duracion (15 min), se envia en cada request
- Refresh token: larga duracion (7 dias), solo para obtener nuevos access tokens

Ejecuta: python ejercicios.py 1
