# NoSQL Introduccion

## Contenido
- Documentos vs modelo relacional
- Conceptos de MongoDB (colecciones, documentos, schemas flexibles)
- Modelado de datos anidados
- Cuando usar SQL vs NoSQL

## Ejercicios

| #  | Ejercicio                                                      |
|----|----------------------------------------------------------------|
| 1  | Modelar documento MongoDB para usuario (dict anidado)           |
| 2  | Convertir esquema SQL normalizado a documento NoSQL             |
| 3  | Comparar: cuando usar SQL vs NoSQL (casos practicos)            |

## Comandos

```bash
python scripts/runner.py 4 7 1
python scripts/runner.py 4 7 2
python scripts/runner.py 4 7 3
```

## Resumen

```python
# Documento NoSQL (MongoDB-like)
usuario = {
    "nombre": "Ana Garcia",
    "email": "ana@email.com",
    "direccion": {
        "calle": "Calle Mayor 10",
        "ciudad": "Madrid",
        "pais": "Espana"
    },
    "intereses": ["lectura", "viajes", "fotografia"]
}
```

## SQL vs NoSQL

| Caracteristica       | SQL                        | NoSQL                          |
|---------------------|----------------------------|--------------------------------|
| Esquema             | Fijo (tablas, columnas)    | Flexible (documentos)          |
| Relaciones         | Joins, FK                  | Anidacion, referencias         |
| Escalabilidad      | Vertical                   | Horizontal                     |
| Consistencia       | Fuerte (ACID)              | Eventual (BASE)                |
| Casos tipicos      | Bancos, facturacion        | Redes sociales, analytics      |
