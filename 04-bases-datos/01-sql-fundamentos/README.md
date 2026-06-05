# SQL Fundamentos

## CREATE TABLE

Crea una nueva tabla en la base de datos. Define columnas con sus tipos.

```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER
);
```

Tipos comunes en SQLite: `INTEGER`, `TEXT`, `REAL`, `BLOB`, `NULL`.

## INSERT

Agrega filas a una tabla.

```sql
INSERT INTO usuarios VALUES (1, 'Ana', 25);
INSERT INTO usuarios (nombre, edad) VALUES ('Luis', 35);
```

Multiples filas a la vez:

```sql
INSERT INTO usuarios VALUES
    (1, 'Ana', 25),
    (2, 'Juan', 30),
    (3, 'Maria', 22);
```

## SELECT

Recupera datos de una o mas tablas.

```sql
SELECT nombre, edad FROM usuarios;
SELECT * FROM usuarios;
```

## WHERE

Filtra filas segun una condicion.

```sql
SELECT * FROM usuarios WHERE edad > 25;
SELECT * FROM usuarios WHERE nombre = 'Ana';
```

Operadores: `=`, `<>`, `>`, `<`, `>=`, `<=`, `LIKE`, `IN`, `BETWEEN`, `AND`, `OR`.

## ORDER BY

Ordena los resultados.

```sql
SELECT * FROM usuarios ORDER BY edad ASC;
SELECT * FROM usuarios ORDER BY nombre DESC;
```

## LIMIT

Limita el numero de filas devueltas.

```sql
SELECT * FROM usuarios LIMIT 5;
SELECT * FROM usuarios ORDER BY edad DESC LIMIT 3;
```
