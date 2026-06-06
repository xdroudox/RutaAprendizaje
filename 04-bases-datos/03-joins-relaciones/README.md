# Joins y Relaciones

Los **JOINs** combinan filas de dos o mas tablas basandose en una condicion relacionada. Son esenciales para trabajar con bases de datos normalizadas.

---

## 1. TEORIA

### 1.1 Tipos de JOIN

#### INNER JOIN

Solo devuelve filas que tienen correspondencia en AMBAS tablas.

```sql
SELECT p.id, p.producto, c.nombre
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.id;
```

```
pedidos:                          INNER JOIN:
┌────┬────────┬──────────┐        ┌────┬────────┬────────┐
│ id │producto│cliente_id│        │ id │producto│cliente │
├────┼────────┼──────────┤        ├────┼────────┼────────┤
│ 1  │Laptop  │ 1        │   →    │ 1  │Laptop  │ Ana    │
│ 2  │Mouse   │ 2        │        │ 2  │Mouse   │ Juan   │
│ 3  │Teclado │ 1        │        │ 3  │Teclado │ Ana    │
└────┴────────┴──────────┘        └────┴────────┴────────┘
clientes:
┌────┬───────┬──────────┐
│ id │nombre │ ciudad   │
├────┼───────┼──────────┤
│ 1  │ Ana   │ Madrid   │
│ 2  │ Juan  │Barcelona │
│ 3  │ Maria │ Valencia │
└────┴───────┴──────────┘
Maria no aparece (no tiene pedidos)
```

#### LEFT JOIN

Todas las filas de la tabla IZQUIERDA, NULL si no hay correspondencia.

```sql
SELECT c.nombre, p.producto
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id;
```

```
Resultado:
┌────────┬───────────────┐
│nombre  │ producto      │
├────────┼───────────────┤
│ Ana    │ Laptop        │
│ Ana    │ Teclado       │
│ Juan   │ Mouse         │
│ Maria  │ NULL          │ ← Maria aparece aunque no tenga pedidos
└────────┴───────────────┘
```

#### RIGHT JOIN

Todas las filas de la tabla DERECHA (equivalente a LEFT JOIN invirtiendo el orden).

#### FULL OUTER JOIN

Todas las filas de ambas tablas (SQLite no lo soporta directamente).

### 1.2 Relaciones

| Tipo | Descripcion | Ejemplo |
|------|-------------|---------|
| **1:1** | Un registro en A se relaciona con uno en B | Usuario → Pasaporte |
| **1:N** | Un registro en A se relaciona con muchos en B | Cliente → Pedidos |
| **N:M** | Muchos registros en A se relacionan con muchos en B | Estudiantes ↔ Cursos |

#### Relacion N:M (muchos-a-muchos)

Requiere una **tabla intermedia** (o tabla de union):

```sql
CREATE TABLE inscripciones (
    estudiante_id INTEGER,
    curso_id INTEGER,
    PRIMARY KEY (estudiante_id, curso_id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Consultar muchos-a-muchos (3 JOINs)
SELECT e.nombre, c.nombre
FROM estudiantes e
JOIN inscripciones i ON e.id = i.estudiante_id
JOIN cursos c ON i.curso_id = c.id;
```

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **JOIN** | Operacion que combina filas de dos tablas |
| **INNER JOIN** | Solo filas que coinciden en ambas tablas |
| **LEFT JOIN** | Todas las filas de la izquierda, NULL si no hay match |
| **RIGHT JOIN** | Todas las filas de la derecha (espejo de LEFT) |
| **FOREIGN KEY** | Columna que referencia la PK de otra tabla |
| **Tabla intermedia** | Tabla que resuelve relaciones N:M |
| **Integridad referencial** | Garantiza que FK siempre apunten a un registro existente |
| **ON** | Condicion que determina como se relacionan las tablas |

---

## 3. EJERCICIOS

### 🟢 Ejercicio 1: INNER JOIN

Escribe un INNER JOIN que muestre pedidos con los datos del cliente (nombre y ciudad).

**Ejecuta:** `python scripts/runner.py 4 3 1`

---

### 🟡 Ejercicio 2: LEFT JOIN

Escribe un LEFT JOIN que muestre TODOS los clientes (incluyendo los que no tienen pedidos, que deben mostrar NULL).

**Ejecuta:** `python scripts/runner.py 4 3 2`

---

### 🔴 Ejercicio 3: Relacion muchos-a-muchos

Escribe una consulta con JOIN entre las 3 tablas (estudiantes, inscripciones, cursos) para mostrar que estudiante esta en que curso.

**Ejecuta:** `python scripts/runner.py 4 3 3`
