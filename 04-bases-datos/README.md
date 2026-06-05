# Nivel 4: Bases de Datos

Bienvenido al nivel de Bases de Datos. Aqui aprenderas los fundamentos de SQL,
diseno relacional, optimizacion y conceptos de bases NoSQL.

## Modulos

### 1. SQL Fundamentos (01-sql-fundamentos)
Creacion de tablas, insercion de datos, consultas SELECT, clausulas WHERE,
ORDER BY y LIMIT.

### 2. Normalizacion (02-normalizacion)
Primera, segunda y tercera forma normal, BCNF, cuando desnormalizar.

### 3. Joins y Relaciones (03-joins-relaciones)
INNER JOIN, LEFT/RIGHT JOIN, FOREIGN KEY, relaciones uno-a-muchos y
muchos-a-muchos.

### 4. Subconsultas y Vistas (04-subconsultas-vistas)
Subconsultas en WHERE/FROM/SELECT, VIEW, CTE con WITH.

### 5. Transacciones ACID (05-transacciones-acid)
BEGIN, COMMIT, ROLLBACK, propiedades ACID.

### 6. Indices y Optimizacion (06-indices-optimizacion)
CREATE INDEX, EXPLAIN, planificacion de consultas, cuando indexar.

### 7. NoSQL Intro (07-nosql-intro)
Documentos vs relacional, conceptos MongoDB, cuando usar NoSQL.

## Como usar

Cada modulo contiene:

- `README.md` -- Explicacion teorica del tema
- `ejercicios.py` -- Ejercicios practicos con SQLite en memoria
- `soluciones.py` -- Soluciones a los ejercicios

Ejecutar un ejercicio:

    python ejercicios.py 1
    python ejercicios.py 1 -p   (con pista)
    python soluciones.py 1

## Requisitos

- Python 3.6+
- Solo modulo `sqlite3` (incluido en la biblioteca estandar)
