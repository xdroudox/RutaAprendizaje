# OAuth2

OAuth2 es un protocolo de autorizacion que permite a aplicaciones obtener
acceso limitado a recursos de un usuario sin compartir sus credenciales.

## Roles

| Rol | Descripcion |
|-----|-------------|
| Resource Owner | Usuario propietario de los datos |
| Client | Aplicacion que solicita acceso |
| Authorization Server | Servidor que autentica y otorga tokens |
| Resource Server | Servidor que sirve los recursos protegidos |

## Flujos (Grant Types)

### Authorization Code (el mas comun)

```
Usuario -> Client: Quiero iniciar sesion con Google
Client -> Auth Server: Redirige al usuario
Usuario -> Auth Server: Inicia sesion y autoriza
Auth Server -> Client: Codigo de autorizacion (callback)
Client -> Auth Server: Codigo + Client Secret -> Access Token
Client -> Resource Server: Access Token -> Recursos
```

Usado por: aplicaciones web con backend.

### Implicit (deprecado)

Flujo simplificado para aplicaciones del lado del cliente (SPA).
Ya no se recomienda; se usa Authorization Code con PKCE.

### Client Credentials

Para comunicacion servidor-a-servidor sin usuario.

```
Client -> Auth Server: Client ID + Client Secret -> Access Token
Client -> Resource Server: Access Token -> Recursos
```

## Conceptos clave

- Access Token: credencial temporar para acceder a recursos
- Refresh Token: para obtener nuevos access tokens
- Scope: permisos solicitados (read, write, etc.)
- Client ID: identificador publico de la aplicacion
- Client Secret: clave secreta del cliente (solo backend)

```python
# Simulacion de flujo Client Credentials
def obtener_token(client_id, client_secret):
    # Normalmente una peticion POST al auth server
    if client_id == "mi-app" and client_secret == "secret123":
        return {
            "access_token": "eyJhbGciOiJIUzI1NiJ9...",
            "token_type": "Bearer",
            "expires_in": 3600
        }
    return None
```

Ejecuta: python ejercicios.py 1
