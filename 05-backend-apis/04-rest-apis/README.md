# REST APIs

## Contenido
- Principios REST (recursos, metodos HTTP, stateless)
- CRUD a HTTP mapping
- Idempotencia
- Diseño de endpoints

---

## 1. Que es REST?

REST (Representational State Transfer) es un estilo arquitectonico para disenar APIs web. Cada "recurso" (usuario, post, producto) se identifica por una URL y se manipula con metodos HTTP.

### Principios REST
1. **Recursos** → cada entidad tiene una URL: `/api/usuarios`, `/api/posts/1`
2. **Metodos HTTP** → GET (leer), POST (crear), PUT (reemplazar), DELETE (eliminar)
3. **Stateless** → cada request contiene toda la informacion necesaria (no hay sesion en el servidor)
4. **Representaciones** → JSON, XML, etc.

---

## 2. CRUD a HTTP

| Operacion SQL | Operacion CRUD | Metodo HTTP | URL ejemplo | Idempotente |
|--------------|----------------|-------------|-------------|-------------|
| SELECT       | Leer           | GET         | `/api/posts` | Si |
| INSERT       | Crear          | POST        | `/api/posts` | No |
| UPDATE       | Actualizar     | PUT         | `/api/posts/1` | Si |
| DELETE       | Eliminar       | DELETE      | `/api/posts/1` | Si |

### Idempotencia
- Un metodo es **idempotente** si hacer el mismo request N veces produce el mismo resultado que hacerlo 1 vez.
- GET `/api/posts/1` → siempre devuelve el mismo post (si no cambio)
- PUT `/api/posts/1` → reemplaza el post, da igual cuantas veces se ejecute
- DELETE `/api/posts/1` → eliminar algo ya eliminado no cambia el estado
- POST `/api/posts` → CADA request crea un NUEVO post (NO idempotente)

---

## 3. Convenciones de endpoints

| Recurso  | GET (listar)        | GET (obtener)        | POST (crear)         | PUT (actualizar)     | DELETE (eliminar)    |
|----------|--------------------|----------------------|----------------------|----------------------|----------------------|
| posts    | `GET /api/posts`   | `GET /api/posts/1`   | `POST /api/posts`    | `PUT /api/posts/1`   | `DELETE /api/posts/1` |
| comments | `GET /api/posts/1/comments` | `GET /api/comments/1` | `POST /api/posts/1/comments` | `PUT /api/comments/1` | `DELETE /api/comments/1` |
| users    | `GET /api/users`   | `GET /api/users/1`   | `POST /api/users`    | `PUT /api/users/1`   | `DELETE /api/users/1` |

---

## 4. Glosario

| Termino        | Definicion |
|---------------|-----------|
| **REST**      | Estilo arquitectonico para APIs web basado en recursos y metodos HTTP |
| **Recurso**   | Entidad del dominio (usuario, post, producto) identificada por URL |
| **Endpoint**  | URL + metodo HTTP que expone una funcionalidad |
| **Idempotente** | Propiedad de que multiples requests identicos produzcan el mismo resultado |
| **CRUD**      | Create, Read, Update, Delete (operaciones basicas sobre datos) |
| **Stateless** | El servidor no almacena estado de la sesion entre requests |

---

## 5. Comparativa entre lenguajes

### Python (Flask)
```python
@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(Usuario.query.all())
```

### JavaScript (Express)
```javascript
app.get('/api/usuarios', (req, res) => {
    res.json(usuarios);
});
```

### Java (Spring Boot)
```java
@GetMapping("/api/usuarios")
public List<Usuario> listar() {
    return usuarioRepository.findAll();
}
```

---

## 6. Ejemplo guiado paso a paso

**Problema:** Disenar endpoints REST para un blog con posts, comments y users.

1. Identificamos los recursos: `posts`, `comments`, `users`
2. Para cada recurso definimos:
   - `GET /api/posts` → lista todos los posts
   - `POST /api/posts` → crea un nuevo post
   - `GET /api/posts/1` → obtiene el post 1
   - `PUT /api/posts/1` → reemplaza el post 1
   - `DELETE /api/posts/1` → elimina el post 1
3. Para recursos anidados (comments de un post):
   - `GET /api/posts/1/comments` → lista comments del post 1
   - `POST /api/posts/1/comments` → crea comment en el post 1

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Disenar endpoints REST para un blog | 🟢 |
| 2  | Mapear CRUD a metodos HTTP | 🟡 |
| 3  | Identificar endpoints idempotentes | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 4 1
python scripts/runner.py 5 4 2
python scripts/runner.py 5 4 3
python scripts/runner.py 5 4 1 -p 1
python scripts/runner.py 5 4 3 -s
```
