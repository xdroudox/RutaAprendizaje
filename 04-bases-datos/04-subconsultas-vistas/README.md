# Subconsultas y Vistas

## Contenido
- Subconsultas en WHERE (comparacion con subresultado)
- Subconsultas en FROM (tabla derivada)
- Subconsultas en SELECT
- Vistas (CREATE VIEW)
- CTE con WITH

## Ejercicios

| #  | Ejercicio                                                          |
|----|--------------------------------------------------------------------|
| 1  | Subconsulta en WHERE (empleados con salario > promedio)            |
| 2  | Subconsulta en FROM (usar subconsulta como tabla temporal)         |
| 3  | Crear y consultar una VIEW                                         |

## Comandos

```bash
python scripts/runner.py 4 4 1
python scripts/runner.py 4 4 2
python scripts/runner.py 4 4 3
```

## Resumen

```sql
-- Subconsulta en WHERE
SELECT * FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- Subconsulta en FROM
SELECT producto, total_vendido
FROM (SELECT producto, SUM(total) as total_vendido FROM ventas GROUP BY producto)
ORDER BY total_vendido DESC;

-- Crear vista
CREATE VIEW empleados_ti AS
SELECT * FROM empleados WHERE departamento = 'TI' AND salario >= 55000;

-- Consultar vista
SELECT * FROM empleados_ti;
```
