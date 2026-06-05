# Subconsultas y Vistas

## Subconsulta en WHERE

Una consulta dentro de otra, usada para filtrar resultados.

```sql
SELECT nombre FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);
```

## Subconsulta en FROM

Trata el resultado de una subconsulta como una tabla temporal.

```sql
SELECT AVG(total) FROM (
    SELECT cliente_id, SUM(total) AS total
    FROM pedidos GROUP BY cliente_id
);
```

## Subconsulta en SELECT

Subconsulta como columna calculada.

```sql
SELECT nombre,
    (SELECT COUNT(*) FROM pedidos WHERE pedidos.cliente_id = clientes.id) AS num_pedidos
FROM clientes;
```

## VIEW

Una vista es una consulta almacenada que se comporta como una tabla virtual.

```sql
CREATE VIEW empleados_caros AS
SELECT * FROM empleados WHERE salario > 50000;

SELECT * FROM empleados_caros;
```

## CTE (WITH)

Common Table Expression: consulta temporal con nombre, util para consultas
recursivas o para simplificar subconsultas complejas.

```sql
WITH empleados_caros AS (
    SELECT * FROM empleados WHERE salario > 50000
)
SELECT * FROM empleados_caros;
```
