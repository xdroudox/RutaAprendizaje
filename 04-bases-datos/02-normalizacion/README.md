# Normalizacion

La **normalizacion** es el proceso de organizar los datos en una BD para reducir redundancia y evitar anomalias. Se aplica en formas progresivas: 1FN, 2FN, 3FN, BCNF.

---

## 1. TEORIA

### 1.1 Primera Forma Normal (1FN)

**Regla:** Cada columna debe contener un solo valor ATOMICO. No arrays, listas ni valores separados por comas.

| ❌ Violacion 1FN | ✅ 1FN |
|------------------|--------|
| `estudiante: "Ana", cursos: "Mate,Historia"` | `estudiante: "Ana", curso: "Mate"` |
| | `estudiante: "Ana", curso: "Historia"` |

```sql
-- ❌ MAL: columna cursos tiene multiples valores
CREATE TABLE estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    cursos TEXT  -- 'Matematicas,Historia'
);

-- ✅ BIEN: tabla intermedia estudiante_curso
CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT);
CREATE TABLE cursos (id INTEGER PRIMARY KEY, nombre TEXT);
CREATE TABLE estudiante_curso (
    estudiante_id INTEGER,
    curso_id INTEGER,
    PRIMARY KEY (estudiante_id, curso_id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);
```

### 1.2 Segunda Forma Normal (2FN)

**Regla:** Cumple 1FN Y cada columna NO clave debe depender de la CLAVE COMPLETA (no solo de parte de ella).

| ❌ Violacion 2FN | Problema |
|------------------|----------|
| `calificaciones(estudiante_id, curso_id)` | `estudiante_nombre` depende solo de `estudiante_id` |
| `estudiante_nombre, curso_nombre, profesor, nota)` | `curso_nombre, profesor` dependen solo de `curso_id` |

```sql
-- ❌ MAL: dependencias parciales
CREATE TABLE calificaciones (
    estudiante_id INTEGER,
    curso_id INTEGER,
    estudiante_nombre TEXT,  -- Solo depende de estudiante_id
    curso_nombre TEXT,       -- Solo depende de curso_id
    profesor TEXT,           -- Solo depende de curso_id
    nota REAL,
    PRIMARY KEY (estudiante_id, curso_id)
);

-- ✅ BIEN: separar en 3 tablas
CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT);
CREATE TABLE cursos (id INTEGER PRIMARY KEY, nombre TEXT, profesor TEXT);
CREATE TABLE calificaciones (
    estudiante_id INTEGER,
    curso_id INTEGER,
    nota REAL,
    PRIMARY KEY (estudiante_id, curso_id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);
```

### 1.3 Tercera Forma Normal (3FN)

**Regla:** Cumple 2FN Y no hay DEPENDENCIAS TRANSITIVAS. Una columna NO clave no debe depender de otra columna NO clave.

| ❌ Violacion 3FN | Problema |
|------------------|----------|
| `pedidos(pedido_id, cliente_id, cliente_nombre, ...)` | `cliente_nombre` depende de `cliente_id` (no de `pedido_id`) |

Dependencia transitiva: `pedido_id → cliente_id → cliente_nombre`

```sql
-- ❌ MAL: dependencia transitiva
CREATE TABLE pedidos (
    pedido_id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    cliente_nombre TEXT,  -- Depende de cliente_id, no de pedido_id
    cliente_ciudad TEXT,  -- Depende de cliente_id, no de pedido_id
    producto TEXT,
    cantidad INTEGER
);

-- ✅ BIEN: separar clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    ciudad TEXT
);
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id),
    producto TEXT,
    cantidad INTEGER
);
```

### 1.4 Resumen

| Forma | Regla | Viola si... |
|-------|-------|-------------|
| **1FN** | Columnas atomicas | Una columna tiene varios valores |
| **2FN** | Dependencia total de la clave | Columna no clave depende solo de parte de la PK compuesta |
| **3FN** | Sin dependencias transitivas | Columna no clave depende de otra columna no clave |
| **BCNF** | Toda dependencia es de una superclave | Caso especial de 3FN |

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Normalizacion** | Proceso de organizar datos para reducir redundancia |
| **Anomalia** | Problema al insertar, actualizar o eliminar datos |
| **Dependencia funcional** | X → Y significa que X determina Y |
| **Dependencia parcial** | Columna depende solo de parte de la PK compuesta |
| **Dependencia transitiva** | X → Y e Y → Z implica X → Z transitiva |
| **Redundancia** | Datos repetidos innecesariamente |
| **Desnormalizacion** | Romper intencionalmente formas normales por rendimiento |
| **FOREIGN KEY** | Columna que referencia la PK de otra tabla |

---

## 3. EJERCICIOS

### 🟢 Ejercicio 1: Identificar 1FN

La tabla `estudiantes` tiene una columna `cursos` con valores separados por comas. Disena el esquema normalizado a 1FN usando tablas separadas.

**Ejecuta:** `python scripts/runner.py 4 2 1`

---

### 🟡 Ejercicio 2: Normalizar a 2FN

La tabla `calificaciones` tiene dependencias parciales. Separa en tablas: `estudiantes`, `cursos`, `calificaciones` (2FN).

**Ejecuta:** `python scripts/runner.py 4 2 2`

---

### 🔴 Ejercicio 3: Normalizar a 3FN

La tabla `pedidos` tiene dependencias transitivas. Separa en `clientes` y `pedidos` (3FN).

**Ejecuta:** `python scripts/runner.py 4 2 3`
