# Normalizacion

## Contenido
- Primera Forma Normal (1NF): atomicidad de columnas
- Segunda Forma Normal (2NF): eliminar dependencias parciales
- Tercera Forma Normal (3NF): eliminar dependencias transitivas
- BCNF y desnormalizacion

## Ejercicios

| #  | Ejercicio                                                       |
|----|-----------------------------------------------------------------|
| 1  | Identificar violacion 1NF (columna con multiples valores)       |
| 2  | Normalizar a 2NF (eliminar dependencias parciales)              |
| 3  | Normalizar a 3NF (eliminar dependencias transitivas)            |

## Comandos

```bash
python scripts/runner.py 4 2 1
python scripts/runner.py 4 2 2
python scripts/runner.py 4 2 3
```

## Resumen Formas Normales

| Forma | Regla                                              |
|-------|----------------------------------------------------|
| 1NF   | Cada columna debe contener un solo valor atomico   |
| 2NF   | Cumple 1NF y cada columna no clave depende de la clave completa |
| 3NF   | Cumple 2NF y no hay dependencias transitivas       |
