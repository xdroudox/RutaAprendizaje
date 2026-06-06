# 06 - Seguridad Web

## Glosario

- **SQL Injection**: vulnerabilidad que permite a un atacante ejecutar comandos SQL maliciosos a traves de entradas de usuario no validadas.
- **XSS (Cross-Site Scripting)**: vulnerabilidad que permite inyectar scripts en paginas web que otros usuarios ejecutan al visitarlas.
- **CSRF (Cross-Site Request Forgery)**: ataque que obliga a un usuario autenticado a realizar acciones no deseadas en una aplicacion.
- **CSP (Content Security Policy)**: header HTTP que controla que recursos (scripts, estilos, etc.) puede cargar el navegador.
- **CORS (Cross-Origin Resource Sharing)**: mecanismo del navegador que permite o bloquea peticiones entre origenes diferentes.
- **HTML Escaping**: reemplazar caracteres especiales (< > & " ') por sus entidades HTML para evitar que se interpreten como codigo.
- **Prepared Statement**: consulta SQL donde los datos se pasan como parametros separados del codigo SQL, eliminando la inyeccion.
- **Clickjacking**: tecnica que oculta contenido malicioso detras de elementos aparentemente inofensivos para engañar al usuario.
- **MIME Sniffing**: comportamiento del navegador que intenta adivinar el tipo MIME de un recurso, lo que puede ser explotado.
- **HTTPS**: protocolo HTTP sobre TLS/SSL que cifra la comunicacion entre el navegador y el servidor.

## Conceptos clave

- **Validacion de entrada**: nunca confies en datos del usuario. Valida y sanitiza toda entrada antes de procesarla.
- **Defensa en profundidad**: aplica multiples capas de seguridad (validacion, escaping, headers, parametrizacion).
- **Principio de minimo privilegio**: cada componente debe tener solo los permisos necesarios para funcionar.
- **Separacion de datos y codigo**: nunca concatenes entradas del usuario con codigo SQL, HTML o comandos del sistema.
- **Headers de seguridad**: configurar headers HTTP como CSP, X-Frame-Options y HSTS protege contra muchas vulnerabilidades comunes.
- **Same-Origin Policy**: politica del navegador que restringe como un documento puede interactuar con recursos de otro origen.

## Comparativa

| Medida de seguridad | Python | Java | JavaScript |
|---------------------|--------|------|------------|
| Escapar HTML | `html.escape(texto)` | `StringEscapeUtils.escapeHtml4()` | `textNode.textContent = texto` |
| SQL parametrizado | `cursor.execute(query, params)` | `PreparedStatement` | `db.query('?', [params])` |
| Verificar headers | `response.headers.get('X-Frame-Options')` | `response.getHeader("X-Frame-Options")` | `response.headers.get('X-Frame-Options')` |
| Generar CSRF token | `secrets.token_hex(16)` | `UUID.randomUUID().toString()` | `crypto.randomUUID()` |
| Validar JWT | `PyJWT.decode(token, key, algorithms)` | `Jwts.parser().verifyWith(key)` | `jwt.verify(token, secret)` |

## Ejemplo guiado

**Problema**: Tenemos un formulario de login vulnerable a SQL Injection. Queremos protegerlo.

**Paso 1**: Version vulnerable (concatenacion de strings).

```python
usuario = "admin' OR '1'='1"
query = f"SELECT * FROM usuarios WHERE nombre = '{usuario}'"
# La query resultante:
# SELECT * FROM usuarios WHERE nombre = 'admin' OR '1'='1'
# Esto retorna todos los usuarios, evadiendo la autenticacion.
```

**Paso 2**: Version segura (parametrizada).

```python
query = "SELECT * FROM usuarios WHERE nombre = ?"
# Los datos se pasan por separado: cursor.execute(query, (usuario,))
# El SQL y los datos nunca se mezclan.
```

**Paso 3**: Prevenir XSS escapando HTML.

```python
import html
comentario = "<script>alert('xss')</script>"
seguro = html.escape(comentario)
# Resultado: &lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;
```

**Paso 4**: Verificar headers de seguridad en una respuesta simulada.

```python
headers = {"Content-Type": "text/html"}
headers_requeridos = ["Content-Security-Policy", "X-Frame-Options",
                       "X-Content-Type-Options", "Strict-Transport-Security"]
for h in headers_requeridos:
    if h not in headers:
        print(f"Falta header: {h}")
```

## Referencia

| Funcion / Header | Descripcion |
|------------------|-------------|
| `html.escape(texto)` | Escapa caracteres < > & " ' a entidades HTML |
| `urllib.parse.quote(texto)` | Codifica URL characters |
| `Content-Security-Policy` | Header que restringe origenes de contenido permitido |
| `X-Frame-Options: DENY` | Header que evita que la pagina se muestre en un iframe |
| `X-Content-Type-Options: nosniff` | Header que evita MIME sniffing |
| `Strict-Transport-Security` | Header que fuerza conexiones HTTPS |
| `Referrer-Policy: no-referrer` | Header que controla informacion enviada en Referer |
| `Permission-Policy` | Header que controla acceso a APIs del navegador |

## Ejercicios

1. **SQL Injection** - Simula una consulta vulnerable y una parametrizada para ver la diferencia.
2. **Prevenir XSS** - Escapa HTML con html.escape() para evitar la ejecucion de scripts.
3. **Headers de seguridad** - Verifica que headers de seguridad esten presentes en una respuesta simulada.

**Ejecuta:** `python scripts/runner.py 10 06 [N]`
