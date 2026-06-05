# Joins y Relaciones

## FOREIGN KEY

Una clave foranea relaciona dos tablas.

```sql
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

## INNER JOIN

Combina filas de dos tablas donde hay coincidencia.

```sql
SELECT c.nombre, p.total
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id;
```

## LEFT JOIN

Devuelve todas las filas de la tabla izquierda, incluso si no hay
coincidencia en la derecha (NULL donde no hay match).

```sql
SELECT c.nombre, p.total
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id;
```

## RIGHT JOIN

Similar a LEFT JOIN pero con la tabla derecha como base.
(SQLite no soporta RIGHT JOIN directamente, se simula con LEFT JOIN
invirtiendo el orden.)

## Relacion Uno a Muchos

Un cliente tiene muchos pedidos. Un pedido pertenece a un cliente.
Se implementa con FK en la tabla muchos (pedidos).

## Relacion Muchos a Muchos

Estudiantes y cursos: un estudiante puede tomar muchos cursos y un curso
tiene muchos estudiantes. Requiere una tabla intermedia (junction table).

```sql
CREATE TABLE estudiante_curso (
    estudiante_id INTEGER,
    curso_id INTEGER,
    PRIMARY KEY (estudiante_id, curso_id)
);
```
