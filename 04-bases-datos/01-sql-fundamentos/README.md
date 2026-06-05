# SQL Fundamentos

## Contenido
- Creacion de tablas con CREATE TABLE
- Insercion de datos con INSERT INTO
- Consultas con SELECT y WHERE
- Actualizacion con UPDATE y eliminacion con DELETE

## Ejercicios

| #  | Ejercicio                                           |
|----|-----------------------------------------------------|
| 1  | SELECT con WHERE (usuarios mayores de 25)           |
| 2  | INSERT INTO (agregar un nuevo producto)             |
| 3  | UPDATE y DELETE (actualizar precio, eliminar)       |

## Comandos

Ejecutar un ejercicio especifico:

```bash
python scripts/runner.py 4 1 1
python scripts/runner.py 4 1 2
python scripts/runner.py 4 1 3
```

Ejecutar solucion:

```bash
python scripts/runner.py 4 1 1 --solucion
```


## Resumen SQL

```sql
-- Crear tabla
CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER DEFAULT 0
);

-- Insertar datos
INSERT INTO productos VALUES (1, 'Laptop', 999.99, 10);

-- Consultar
SELECT * FROM productos WHERE precio > 100;

-- Actualizar
UPDATE productos SET precio = 30.00 WHERE nombre = 'Mouse';

-- Eliminar
DELETE FROM productos WHERE id = 3;
```
