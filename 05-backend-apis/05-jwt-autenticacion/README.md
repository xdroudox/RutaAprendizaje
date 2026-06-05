# JWT y Autenticacion

JWT (JSON Web Token) es un estandar para crear tokens de autenticacion con tres partes codificadas en Base64.

## Estructura
`header.payload.firma`

- **Header:** algoritmo y tipo (`{"alg": "HS256", "typ": "JWT"}`)
- **Payload:** datos (claims) como `sub`, `iat`, `exp`
- **Firma:** verificacion con clave secreta

## Flujo
1. Usuario se autentica -> servidor genera JWT
2. Cliente envia JWT en header `Authorization: Bearer <token>`
3. Servidor verifica firma y claims

## Ejercicios

1. **Crear un JWT simple** - Construir un token con formato header.payload.firma (Base64).
   **Ejecuta:** `python scripts/runner.py 5 5 1`

2. **Decodificar un JWT** - Extraer el payload de un token JWT.
   **Ejecuta:** `python scripts/runner.py 5 5 2`

3. **Verificar expiracion de JWT** - Comprobar si un token ha expirado usando el claim `exp`.
   **Ejecuta:** `python scripts/runner.py 5 5 3`
