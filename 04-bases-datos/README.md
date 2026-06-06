# NIVEL 4: Bases de Datos

```python
print("Bienvenido al Nivel 4, guardian de los datos!")
print("Aqui dominaras el arte de almacenar, consultar y optimizar informacion.")
```

## Que aprenderas en este nivel

Las **bases de datos** son el corazon de cualquier aplicacion. Este nivel cubre desde SQL basico hasta disno relacional, transacciones y bases NoSQL.

Cada tema sigue la misma estructura:

```
📖 TEORIA → Explicacion con ejemplos SQL
📖 GLOSARIO → Terminos del tema definidos
🔄 COMPARATIVA → SQL vs Python vs MongoDB
📝 EJEMPLO GUIADO → Problema resuelto paso a paso
🎯 EJERCICIOS → 3 niveles: 🟢 Basico, 🟡 Intermedio, 🔴 Avanzado
```

## Temas

| # | Tema | Que aprenderas |
|---|------|----------------|
| 1 | **SQL Fundamentos** | CREATE TABLE, INSERT, SELECT, WHERE, UPDATE, DELETE |
| 2 | **Normalizacion** | 1FN, 2FN, 3FN, BCNF, desnormalizacion |
| 3 | **Joins y Relaciones** | INNER JOIN, LEFT/RIGHT JOIN, FOREIGN KEY, relaciones |
| 4 | **Subconsultas y Vistas** | Subqueries, VIEW, CTE (WITH), EXISTS |
| 5 | **Transacciones ACID** | BEGIN, COMMIT, ROLLBACK, propiedades ACID |
| 6 | **Indices y Optimizacion** | CREATE INDEX, EXPLAIN, plan de ejecucion |
| 7 | **NoSQL Intro** | Documentos vs relacional, MongoDB, casos de uso |

## Progresion

```
T1 (SQL Basico) → T2 (Normalizacion) → T3 (Joins) → T4 (Subconsultas)
                                                          │
                                            T5 (ACID) ←──┤
                                                          │
                                            T6 (Indices) ←┘
                                                          │
                                              T7 (NoSQL) ←┘
```

## Requisitos

- Completar Nivel 3 (Estructuras de Datos)
- Python 3.6+ con modulo `sqlite3` (incluido)

## Como empezar

```bash
# Comienza con el primer tema
code 04-bases-datos/01-sql-fundamentos/README.md

# Ejecuta ejercicios
python scripts/runner.py 4 1 1
```
