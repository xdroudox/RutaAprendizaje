# OAuth2

## Contenido
- Roles en OAuth2 (Resource Owner, Client, Auth Server, Resource Server)
- Flujo Authorization Code
- Flujo Client Credentials
- Tokens de acceso vs tokens de refresco

---

## 1. Que es OAuth2?

OAuth2 es un marco de autorizacion que permite a aplicaciones obtener acceso limitado a recursos de un usuario SIN compartir sus credenciales.

### El problema que resuelve
Sin OAuth2: le das tu password de Google a una app para que acceda a tu Drive → peligroso.
Con OAuth2: la app pide permiso → tu autorizas → Google da un token temporal a la app.

---

## 2. Roles

| Rol                | Quien es? | Ejemplo |
|-------------------|-----------|---------|
| **Resource Owner** | Dueno del recurso | Usuario con datos en Google Drive |
| **Client**        | App que solicita acceso | App web que quiere leer archivos |
| **Authorization Server** | Emite tokens | Servidor de Google (accounts.google.com) |
| **Resource Server** | Aloja los recursos | API de Google Drive |

---

## 3. Flujo Authorization Code

El flujo mas usado para aplicaciones web/server-side.

```
Usuario (Resource Owner)     App (Client)        Auth Server      Resource Server
     |                          |                     |                  |
     |-- Clic "Login Google" -->|                     |                  |
     |                          |-- Auth Request ---->|                  |
     |                          |   ?client_id=123    |                  |
     |                          |   &redirect_uri=... |                  |
     |<-- Login + Autorizar --> |                     |                  |
     |                          |                     |                  |
     |                          |<-- Auth Code -------|                  |
     |                          |                     |                  |
     |                          |-- POST code+secret->|                  |
     |                          |<-- access_token ----|                  |
     |                          |                     |                  |
     |                          |-- API call -------->|-- valida token ->|
     |                          |   Bearer token      |                  |
     |                          |<-- datos -----------|                  |
```

### Pasos:
1. Usuario hace clic en "Iniciar sesion con Google"
2. App redirige a Auth Server con `client_id` y `redirect_uri`
3. Usuario se autentica y autoriza permisos
4. Auth Server redirige a `redirect_uri?code=...`
5. App canjea `code` + `client_secret` por `access_token`
6. App usa `access_token` para llamar a la API

---

## 4. Flujo Client Credentials

Para comunicacion servidor-servidor (sin usuario).

```
App Backend              Auth Server        Resource Server
    |                        |                    |
    |-- POST /token -------->|                    |
    |   client_id+secret     |                    |
    |<-- access_token -------|                    |
    |                        |                    |
    |-- GET /api/data ------>|-- valida token --->|
    |   Bearer token         |                    |
    |<-- datos --------------|                    |
```

---

## 5. Glosario

| Termino             | Definicion |
|--------------------|-----------|
| **OAuth2**         | Marco de autorizacion para acceso delegado |
| **Access Token**   | Token que permite acceder a recursos protegidos |
| **Refresh Token**  | Token para obtener nuevos access tokens sin re-autenticar |
| **Authorization Code** | Codigo temporal de un solo uso para obtener tokens |
| **client_id**      | Identificador publico de la aplicacion |
| **client_secret**  | Clave secreta de la aplicacion (no compartir) |
| **redirect_uri**   | URL a la que el Auth Server redirige tras autorizar |
| **Scope**          | Permisos solicitados (read, write, etc.) |

---

## 6. Comparativa de flujos

| Flujo               | Usuario implicado? | Caso de uso tipico |
|--------------------|--------------------|--------------------|
| Authorization Code | Si                 | Apps web con backend |
| Client Credentials | No                 | Microservicios, APIs internas |
| Implicit (deprecado) | Si               | Apps SPA (reemplazado por PKCE) |

---

## 7. Ejemplo guiado paso a paso

**Problema:** App web quiere leer archivos de Google Drive del usuario.

1. App redirige a: `https://accounts.google.com/o/oauth2/auth?client_id=APP_ID&redirect_uri=APP/callback&response_type=code&scope=drive.readonly`
2. Usuario ve pantalla de Google: "APP quiere acceder a tus archivos de Drive"
3. Usuario hace clic en "Permitir"
4. Google redirige a: `APP/callback?code=AUTH_CODE_XYZ`
5. App envia POST a Google: `POST /token` con `code=AUTH_CODE_XYZ` + `client_secret`
6. Google responde: `{"access_token": "ya29...", "expires_in": 3600}`
7. App usa `access_token` en `Authorization: Bearer ya29...` para llamar a Drive API

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Identificar roles OAuth2 | 🟢 |
| 2  | Simular flujo Authorization Code | 🟡 |
| 3  | Simular flujo Client Credentials | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 6 1
python scripts/runner.py 5 6 2
python scripts/runner.py 5 6 3
python scripts/runner.py 5 6 1 -p 1
python scripts/runner.py 5 6 3 -s
```
