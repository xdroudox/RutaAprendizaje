# Indices y Optimizacion

## Contenido
- CREATE INDEX para acelerar busquedas
- EXPLAIN QUERY PLAN para analizar el plan de ejecucion
- Comparacion de rendimiento con y sin indices
- Cuando indexar (y cuando no)

## Ejercicios

| #  | Ejercicio                                                      |
|----|----------------------------------------------------------------|
| 1  | Crear indice y medir velocidad con EXPLAIN                     |
| 2  | Comparar query CON y SIN indice (con time)                     |
| 3  | Identificar queries lentas y proponer indices                  |

## Comandos

```bash
python scripts/runner.py 4 6 1
python scripts/runner.py 4 6 2
python scripts/runner.py 4 6 3
```

## Resumen

```sql
-- Crear indice
CREATE INDEX idx_categoria ON productos(categoria);

-- Analizar plan de ejecucion
EXPLAIN QUERY PLAN SELECT * FROM productos WHERE categoria = 'Electronica';

-- Buenas practicas
-- Indexar columnas usadas en WHERE, JOIN y ORDER BY
-- No indexar columnas con baja cardinalidad (ej. booleanos)
-- Los indices aceleran lecturas pero ralentizan escrituras
```
