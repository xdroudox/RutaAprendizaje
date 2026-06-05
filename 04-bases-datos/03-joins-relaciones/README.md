# Joins y Relaciones

## Contenido
- INNER JOIN: registros que coinciden en ambas tablas
- LEFT / RIGHT JOIN: todos los registros de una tabla con datos de la otra
- Relaciones uno-a-muchos y muchos-a-muchos
- FOREIGN KEY e integridad referencial

## Ejercicios

| #  | Ejercicio                                                      |
|----|----------------------------------------------------------------|
| 1  | INNER JOIN (pedidos + clientes)                                |
| 2  | LEFT JOIN (todos los clientes aunque no tengan pedidos)        |
| 3  | Relacion muchos-a-muchos (estudiantes-cursos con tabla intermedia) |

## Comandos

```bash
python scripts/runner.py 4 3 1
python scripts/runner.py 4 3 2
python scripts/runner.py 4 3 3
```

## Resumen Joins

```sql
-- Solo registros con correspondencia en ambas tablas
SELECT * FROM pedidos INNER JOIN clientes ON pedidos.cliente_id = clientes.id;

-- Todos los de la izquierda, NULL si no hay correspondencia
SELECT * FROM clientes LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;

-- Muchos-a-muchos con tabla intermedia
SELECT * FROM estudiantes e
JOIN inscripciones i ON e.id = i.estudiante_id
JOIN cursos c ON i.curso_id = c.id;
```
