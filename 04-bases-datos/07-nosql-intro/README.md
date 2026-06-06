# NoSQL Introduccion

## Contenido
- Documentos vs modelo relacional
- Conceptos de MongoDB (colecciones, documentos, schemas flexibles)
- Modelado de datos anidados
- Cuando usar SQL vs NoSQL

---

## 1. Que es NoSQL?

NoSQL = "Not Only SQL". Es una familia de bases de datos que NO usan el modelo relacional (tablas, filas, JOINs).

### Diferencias clave SQL vs NoSQL

| Caracteristica       | SQL                        | NoSQL (Documentos)          |
|---------------------|----------------------------|-----------------------------|
| **Estructura**      | Tablas, filas, columnas    | Colecciones, documentos     |
| **Esquema**         | Fijo (definido al crear)   | Flexible (cada documento diferente) |
| **Relaciones**      | JOINs con claves foraneas  | Anidacion o referencias     |
| **Escalabilidad**   | Vertical (mas CPU/RAM)     | Horizontal (mas servidores) |
| **Consistencia**    | Fuerte (ACID)              | Eventual (BASE) |
| **Lenguaje**        | SQL estandar               | API propia (JSON, BSON)     |
| **Casos tipicos**   | Bancos, facturacion, ERP  | Redes sociales, analytics, IoT |

### Ejemplo visual: Mismo dato en SQL vs NoSQL

**SQL (2 tablas normalizadas):**
```sql
-- Tabla clientes
CREATE TABLE clientes (id INT, nombre TEXT, ciudad TEXT);
INSERT INTO clientes VALUES (1, 'Ana', 'Madrid');

-- Tabla pedidos (FK a clientes)
CREATE TABLE pedidos (id INT, cliente_id INT, producto TEXT, total REAL);
INSERT INTO pedidos VALUES (1, 1, 'Laptop', 999.99);
INSERT INTO pedidos VALUES (2, 1, 'Mouse', 25.50);

-- Consulta con JOIN
SELECT * FROM clientes c JOIN pedidos p ON c.id = p.cliente_id;
```

**NoSQL (1 unico documento):**
```json
{
  "cliente": {
    "nombre": "Ana",
    "ciudad": "Madrid"
  },
  "pedidos": [
    { "producto": "Laptop", "total": 999.99 },
    { "producto": "Mouse", "total": 25.50 }
  ]
}
```

---

## 2. Conceptos NoSQL

| Concepto       | Equivalente SQL    | Descripcion breve |
|---------------|-------------------|-------------------|
| Coleccion     | Tabla             | Grupo de documentos |
| Documento     | Fila              | Unidad de datos (JSON/BSON) |
| Campo         | Columna           | Atributo del documento |
| Id            | Primary Key       | Identificador unico |
| Anidacion     | JOIN              | Datos relacionados dentro del mismo documento |
| Schema-less   | Schema fijo       | Cada documento puede tener campos diferentes |

### Documento MongoDB tipico
```python
usuario = {
    "_id": 1,
    "nombre": "Ana Garcia",
    "email": "ana@email.com",
    "direccion": {
        "calle": "Calle Mayor 10",
        "ciudad": "Madrid",
        "pais": "Espana"
    },
    "intereses": ["lectura", "viajes", "fotografia"],
    "activo": True
}
```

Ventajas del documento anidado:
- Lectura mas rapida (1 sola consulta vs 1 consulta + JOIN)
- Datos que se acceden juntos se almacenan juntos
- Esquema flexible (cada usuario puede tener campos distintos)

Desventajas:
- Duplicacion de datos (si el cliente cambia de direccion, hay que actualizar multiples documentos)
- Dificil para relaciones muchos-a-muchos

---

## 3. Glosario

| Termino          | Definicion |
|-----------------|-----------|
| **NoSQL**       | Familia de BD no relacionales (documentos, clave-valor, grafos, columnas) |
| **Documento**   | Unidad de datos en formato JSON/BSON (similar a un dict de Python) |
| **Coleccion**   | Grupo de documentos (similar a una tabla SQL) |
| **BSON**        | Binary JSON, formato binario que usa MongoDB internamente |
| **Anidacion**   | Incluir datos relacionados dentro del mismo documento |
| **Schema-less** | Los documentos de una coleccion pueden tener campos distintos |
| **BASE**        | Basically Available, Soft state, Eventual consistency (opuesto a ACID) |
| **Escalabilidad horizontal** | Agregar mas servidores en lugar de mejorar el hardware |
| **TTL**         | Time To Live - documentos que se borran automaticamente tras un tiempo |

---

## 4. Comparativa entre lenguajes

### Python (dicts)
```python
# Documento NoSQL en Python
usuario = {
    "nombre": "Ana Garcia",
    "email": "ana@email.com",
    "direcciones": [
        {"tipo": "casa", "calle": "Mayor 10"},
        {"tipo": "trabajo", "calle": "Gran Via 5"}
    ]
}
# Acceso
print(usuario["direcciones"][0]["calle"])  # Mayor 10
```

### JavaScript (objetos)
```javascript
// Documento NoSQL en JavaScript
const usuario = {
    nombre: "Ana Garcia",
    email: "ana@email.com",
    direcciones: [
        { tipo: "casa", calle: "Mayor 10" },
        { tipo: "trabajo", calle: "Gran Via 5" }
    ]
};
// Acceso
console.log(usuario.direcciones[0].calle);  // Mayor 10
```

### Java (Mapas)
```java
// Documento NoSQL en Java (con Map)
Map<String, Object> usuario = new HashMap<>();
usuario.put("nombre", "Ana Garcia");
usuario.put("email", "ana@email.com");
List<Map<String, String>> direcciones = new ArrayList<>();
direcciones.add(Map.of("tipo", "casa", "calle", "Mayor 10"));
direcciones.add(Map.of("tipo", "trabajo", "calle", "Gran Via 5"));
usuario.put("direcciones", direcciones);
// Acceso (requiere casteo)
System.out.println(((Map<String, String>)((List<?>)usuario.get("direcciones")).get(0)).get("calle"));
```

---

## 5. Cuando usar SQL vs NoSQL

### Usa SQL cuando:
- ✅ Necesitas transacciones ACID (bancos, facturacion, reservas)
- ✅ Datos con estructura fija y relaciones bien definidas
- ✅ Consultas complejas con multiples JOINs y agregaciones
- ✅ Integridad referencial estricta (FK, constraints)
- ✅ Reportes financieros donde los totales deben ser exactos

### Usa NoSQL cuando:
- ✅ Estructura variable (productos con atributos distintos)
- ✅ Alta escalabilidad horizontal (redes sociales, IoT)
- ✅ Alto volumen de escritura (logs, eventos, analytics)
- ✅ Datos temporales con TTL (sesiones, cache)
- ✅ Prototipos rapidos (schema flexible acelera el desarrollo)

### Regla practica
- Si tus datos se parecen a una hoja de calculo → SQL
- Si tus datos se parecen a un JSON complejo → NoSQL
- La mayoria de aplicaciones reales usan AMBOS (poliglota persistence)

---

## 6. Ejemplo guiado paso a paso

**Problema:** Modelar un blog con articulos y comentarios.

**Enfoque SQL (normalizado):**
```sql
CREATE TABLE articulos (id INT, titulo TEXT, contenido TEXT);
CREATE TABLE comentarios (id INT, articulo_id INT, texto TEXT, autor TEXT);
-- Consulta: SELECT * FROM articulos JOIN comentarios ON ...
```

**Enfoque NoSQL (anidado):**
```python
articulo = {
    "titulo": "Introduccion a NoSQL",
    "contenido": "NoSQL es...",
    "comentarios": [
        {"texto": "Muy buen articulo", "autor": "Carlos"},
        {"texto": "Me ayudo mucho", "autor": "Maria"}
    ]
}
```

Ventajas del enfoque NoSQL:
- 1 sola consulta vs 1 consulta + JOIN
- Los comentarios siempre se leen junto con el articulo
- Schema flexible (cada comentario podria tener campos extra como "likes")

Desventajas:
- Si un comentario se reporta como inapropiado, hay que buscarlo dentro del documento
- Si los comentarios crecen mucho, el documento se vuelve grande

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Modelar documento MongoDB para usuario (dict anidado) | 🟢 |
| 2  | Convertir esquema SQL normalizado a documento NoSQL | 🟡 |
| 3  | Clasificar casos de uso: cuando usar SQL vs NoSQL | 🔴 |

## Comandos

```bash
python scripts/runner.py 4 7 1
python scripts/runner.py 4 7 2
python scripts/runner.py 4 7 3
python scripts/runner.py 4 7 1 -p 1   # Pista 1
python scripts/runner.py 4 7 3 -s     # Solucion
```
