# Middleware y Filtros

## Contenido
- Concepto de middleware (pipeline de procesamiento)
- Middleware de logging
- Middleware de autenticacion
- Pipeline de middlewares

---

## 1. Que es Middleware?

Middleware es software que se ejecuta entre la peticion y la respuesta del servidor, formando un **pipeline** de procesamiento. Cada middleware puede examinar, modificar o rechazar la request antes de pasarla al siguiente.

### Pipeline tipico
```
Request → Logger → Auth → CORS → Rate Limit → Handler → Response
```

---

## 2. Patron de diseno

Cada middleware es una funcion que:
1. Recibe la request
2. Hace algo (log, validar, modificar)
3. Devuelve la request modificada (o None para rechazar)

```python
def middleware(req):
    # procesar
    return req  # o None para detener
```

---

## 3. Middlewares comunes

| Middleware      | Funcion |
|----------------|---------|
| **Logger**     | Registra cada request (metodo, ruta, timestamp) |
| **Auth**       | Verifica token JWT en header Authorization |
| **CORS**       | Agrega headers Access-Control-Allow-Origin |
| **Rate Limit** | Limita requests por IP en un periodo |
| **Compresion** | Comprime la respuesta (gzip) |
| **Parser**     | Parsea el body (JSON, form, etc.) |

---

## 4. Glosario

| Termino       | Definicion |
|--------------|-----------|
| **Middleware** | Funcion en el pipeline request/response |
| **Pipeline**  | Secuencia de middlewares que procesan la request |
| **Handler**   | Funcion final que maneja la request y genera la response |
| **Chain**     | Cadena de responsabilidad (design pattern) |
| **Reject**    | Cuando un middleware detiene el pipeline (devuelve None) |

---

## 5. Comparativa entre lenguajes

### Python (Flask)
```python
@app.before_request
def log_request():
    print(f"{request.method} {request.path}")
```

### JavaScript (Express)
```javascript
app.use((req, res, next) => {
    console.log(`${req.method} ${req.path}`);
    next();
});
```

### Java (Spring Boot)
```java
@Component
public class LoggingFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) {
        System.out.println("Request received");
        chain.doFilter(req, res);
    }
}
```

---

## 6. Ejemplo guiado paso a paso

**Problema:** Pipeline con 3 middlewares: Logger → Auth → CORS

1. **Logger:** imprime `[LOG] GET /api/usuarios`
2. **Auth:** verifica header Authorization, si falta → rechaza
3. **CORS:** agrega `Access-Control-Allow-Origin: *`
4. **Handler:** procesa la request y genera respuesta

```python
def run_pipeline(request, middlewares):
    for mw in middlewares:
        if request is None:
            break
        request = mw(request)
    return request
```

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Middleware de logging | 🟢 |
| 2  | Middleware de autenticacion | 🟡 |
| 3  | Pipeline de middlewares | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 8 1
python scripts/runner.py 5 8 2
python scripts/runner.py 5 8 3
python scripts/runner.py 5 8 1 -p 1
python scripts/runner.py 5 8 3 -s
```
