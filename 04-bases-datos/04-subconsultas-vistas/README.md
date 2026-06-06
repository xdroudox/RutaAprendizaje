# Subconsultas y Vistas

Las **subconsultas** son consultas SQL anidadas dentro de otra consulta. Las **vistas (VIEW)** son consultas almacenadas que se comportan como tablas virtuales.

---

## 1. TEORIA

### 1.1 Subconsulta en WHERE

Una consulta dentro de la clausula WHERE de otra consulta.

```sql
-- Empleados con salario mayor al promedio
SELECT * FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);
```

La subconsulta `(SELECT AVG(salario) FROM empleados)` se ejecuta PRIMERO y devuelve un unico valor (56000). Luego la consulta externa lo usa para filtrar.

### 1.2 Subconsulta en FROM

La subconsulta actua como una **tabla temporal** (tabla derivada).

```sql
-- Total vendido por producto (ordenado)
SELECT producto, total_vendido
FROM (
    SELECT producto, SUM(total) AS total_vendido
    FROM ventas
    GROUP BY producto
)
ORDER BY total_vendido DESC;
```

La subconsulta en FROM debe tener un alias (aunque SQLite no lo exija siempre).

### 1.3 Subconsulta en SELECT

Devuelve un valor calculado por fila.

```sql
SELECT nombre,
       (SELECT AVG(salario) FROM empleados) AS promedio,
       salario - (SELECT AVG(salario) FROM empleados) AS diferencia
FROM empleados;
```

### 1.4 Vistas (VIEW)

Una **vista** es una consulta SQL almacenada con un nombre. Se comporta como una tabla virtual.

```sql
-- Crear vista
CREATE VIEW empleados_ti AS
SELECT * FROM empleados
WHERE departamento = 'TI' AND salario >= 55000;

-- Consultar vista (como si fuera una tabla)
SELECT * FROM empleados_ti;

-- Ventajas:
-- 1. Reutilizar consultas complejas
-- 2. Seguridad (mostrar solo columnas necesarias)
-- 3. Abstraccion (ocultar complejidad)
```

### 1.5 CTE (WITH)

Common Table Expression: subconsulta con nombre, mas legible.

```sql
WITH empleados_caros AS (
    SELECT * FROM empleados WHERE salario > 60000
)
SELECT * FROM empleados_caros;
```

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Subconsulta** | Consulta SQL anidada dentro de otra consulta |
| **Subconsulta correlacionada** | Depende de la fila actual de la consulta externa |
| **Tabla derivada** | Subconsulta en la clausula FROM |
| **VIEW** | Consulta almacenada como tabla virtual |
| **CTE** | Common Table Expression (WITH), subconsulta con nombre temporal |
| **EXISTS** | Operador que verifica si una subconsulta devuelve filas |
| **IN / NOT IN** | Operador que verifica si un valor esta en el resultado de una subconsulta |

---

## 3. EJERCICIOS

### 🟢 Ejercicio 1: Subconsulta en WHERE

Muestra los empleados con salario mayor al promedio usando una subconsulta en WHERE.

**Ejecuta:** `python scripts/runner.py 4 4 1`

---

### 🟡 Ejercicio 2: Subconsulta en FROM

Usa una subconsulta en FROM para obtener el total vendido por producto. Ordena de mayor a menor.

**Ejecuta:** `python scripts/runner.py 4 4 2`

---

### 🔴 Ejercicio 3: Crear y consultar una VIEW

Crea una vista `empleados_ti` que muestre solo empleados de TI con salario >= 55000. Luego consultala.

**Ejecuta:** `python scripts/runner.py 4 4 3`
