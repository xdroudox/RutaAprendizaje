# OAuth2

OAuth2 es un marco de autorizacion que permite a aplicaciones obtener acceso limitado a recursos de un usuario.

## Roles
- **Resource Owner:** dueno del recurso (usuario)
- **Client:** aplicacion que solicita acceso
- **Authorization Server:** emite tokens tras autenticacion
- **Resource Server:** aloja los recursos protegidos

## Flujos principales
- **Authorization Code:** para aplicaciones web/server-side
- **Client Credentials:** para comunicacion servidor-servidor
- **Implicit:** (deprecado) para apps client-side

## Ejercicios

1. **Identificar roles OAuth2** - Clasificar cada entidad en su rol correspondiente.
   **Ejecuta:** `python scripts/runner.py 5 6 1`

2. **Simular flujo Authorization Code** - Pasos: login -> auth code -> token -> recurso.
   **Ejecuta:** `python scripts/runner.py 5 6 2`

3. **Simular flujo Client Credentials** - Cliente se autentica directamente contra auth server.
   **Ejecuta:** `python scripts/runner.py 5 6 3`
