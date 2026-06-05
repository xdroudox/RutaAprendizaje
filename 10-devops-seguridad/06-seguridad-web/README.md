# 06 - Seguridad Web

## Conceptos clave

- **SQL Injection**: inyeccion de SQL malicioso en entradas de usuario.
- **XSS (Cross-Site Scripting)**: inyeccion de scripts en paginas vistas por otros usuarios.
- **CSRF (Cross-Site Request Forgery)**: forzar a un usuario autenticado a ejecutar acciones no deseadas.
- **CSP (Content Security Policy)**: header HTTP que restringe fuentes de contenido.
- **CORS**: politica de acceso cruzado entre origenes.

## Headers de seguridad importantes

| Header | Funcion |
|--------|---------|
| Content-Security-Policy | Restringir origenes de scripts |
| X-Content-Type-Options | Evitar MIME sniffing |
| X-Frame-Options | Prevenir clickjacking |
| Strict-Transport-Security | Forzar HTTPS |

## Ejercicios

1. **SQL Injection** - Simula consulta vulnerable vs parametrizada.
2. **Prevenir XSS** - Escapa HTML con html.escape().
3. **Headers de seguridad** - Verifica headers en una respuesta simulada.

**Ejecuta:** `python scripts/runner.py 10 06 [ejercicio]`
