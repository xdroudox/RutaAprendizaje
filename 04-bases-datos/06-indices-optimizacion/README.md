# Indices y Optimizacion

## CREATE INDEX

Los indices aceleran las busquedas en columnas especificas.

```sql
CREATE INDEX idx_empleados_nombre ON empleados(nombre);
CREATE INDEX idx_orden_fecha ON ordenes(fecha DESC);
```

Indice unico (no permite duplicados):

```sql
CREATE UNIQUE INDEX idx_email ON usuarios(email);
```

## EXPLAIN QUERY PLAN

Muestra como SQLite ejecutara una consulta. Ayuda a detectar
carencia de indices.

```sql
EXPLAIN QUERY PLAN SELECT * FROM empleados WHERE nombre = 'Ana';
```

## Cuando indexar

- Columnas usadas frecuentemente en WHERE
- Columnas usadas en JOIN (FOREIGN KEY)
- Columnas usadas en ORDER BY

## Cuando NO indexar

- Tablas pequenas
- Columnas con pocos valores distintos (ej. booleanos)
- Columnas que se actualizan muy frecuentemente
- El indice tiene costo en INSERTS, UPDATES, DELETES

## Indices compuestos

```sql
CREATE INDEX idx_depto_salario ON empleados(departamento, salario);
```
