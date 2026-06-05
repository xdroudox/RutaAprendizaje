# NoSQL - Introduccion

## Documentos vs Relacional

| Relacional (SQL) | Documentos (NoSQL)  |
|------------------|----------------------|
| Tablas           | Colecciones          |
| Filas            | Documentos (JSON)    |
| Columnas         | Campos               |
| Esquema fijo     | Esquema flexible     |
| JOINs            | Embedding / Referencias |

## MongoDB conceptos

Un documento en MongoDB es similar a un diccionario Python:

```python
{
    "_id": 1,
    "nombre": "Ana",
    "direccion": {
        "ciudad": "Madrid",
        "calle": "Calle Mayor 10"
    },
    "intereses": ["lectura", "deporte"]
}
```

## Cuando usar NoSQL

- Esquema de datos que cambia frecuentemente
- Datos jerarquicos o anidados
- Alta escalabilidad horizontal
- Prototipos rapidos sin esquema fijo
- Cuando la consistencia inmediata no es critica

## Cuando usar SQL

- Relaciones complejas entre entidades
- Consultas ad-hoc y analiticas
- ACID es requisito
- Datos altamente estructurados
- Reportes con agregaciones complejas
