# SQL Fundamentos

SQL (Structured Query Language) es el lenguaje estandar para gestionar bases de datos relacionales. Con el se pueden crear tablas, insertar datos, consultarlos, actualizarlos y eliminarlos.

---

## 1. TEORIA

### 1.1 CREATE TABLE — Crear tablas

Define la estructura de una tabla: columnas, tipos de datos y restricciones.

```sql
CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER DEFAULT 0
);
```

| Tipo SQL | Equivalente Python | Descripcion |
|----------|-------------------|-------------|
| INTEGER | int | Numeros enteros |
| REAL | float | Numeros decimales |
| TEXT | str | Cadenas de texto |
| BLOB | bytes | Datos binarios |

| Restriccion | Significado |
|-------------|-------------|
| PRIMARY KEY | Identificador unico (NOT NULL + UNIQUE) |
| NOT NULL | No permite valores nulos |
| DEFAULT valor | Valor por defecto si no se especifica |
| UNIQUE | No permite valores duplicados |

### 1.2 INSERT INTO — Insertar datos

```sql
-- Insertar con valores en orden
INSERT INTO productos VALUES (1, 'Laptop', 999.99, 10);

-- Insertar especificando columnas
INSERT INTO productos (nombre, precio) VALUES ('Mouse', 25.50);
```

### 1.3 SELECT — Consultar datos

```sql
-- Todas las columnas
SELECT * FROM productos;

-- Columnas especificas
SELECT nombre, precio FROM productos;

-- Con filtro WHERE
SELECT * FROM productos WHERE precio > 100;

-- Ordenar
SELECT * FROM productos ORDER BY precio DESC;

-- Limitar resultados
SELECT * FROM productos LIMIT 2;
```

### 1.4 UPDATE — Actualizar datos

```sql
UPDATE productos SET precio = 30.00 WHERE nombre = 'Mouse';
```

**Siempre usa WHERE en UPDATE o cambiarias TODAS las filas.**

### 1.5 DELETE — Eliminar datos

```sql
DELETE FROM productos WHERE id = 3;
```

**Siempre usa WHERE en DELETE.**

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **SQL** | Structured Query Language, lenguaje para BD relacionales |
| **Tabla** | Coleccion de registros organizados en filas y columnas |
| **Columna** | Campo o atributo de una tabla |
| **Fila (registro)** | Una entrada completa en la tabla |
| **Primary Key** | Columna que identifica univocamente cada fila |
| **NOT NULL** | Restriccion que prohibe valores nulos |
| **WHERE** | Clausula que filtra resultados segun una condicion |
| **ORDER BY** | Ordena los resultados (ASC/DESC) |
| **LIMIT** | Restringe el numero de filas devueltas |
| **INSERT** | Comando para agregar nuevas filas |
| **UPDATE** | Comando para modificar filas existentes |
| **DELETE** | Comando para eliminar filas |
| **SQLite** | BD ligera embebida (no requiere servidor) |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Conectar a BD

```python
# PYTHON (SQLite)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
```

```java
// JAVA (JDBC + SQLite)
Connection conn = DriverManager.getConnection("jdbc:sqlite::memory:");
Statement stmt = conn.createStatement();
```

```javascript
// JAVASCRIPT (Node.js + better-sqlite3)
const db = require('better-sqlite3')(':memory:');
```

### SELECT con filtro

```python
# PYTHON
c.execute("SELECT * FROM usuarios WHERE edad > 25")
for row in c.fetchall():
    print(row)
```

```java
// JAVA
ResultSet rs = stmt.executeQuery(
    "SELECT * FROM usuarios WHERE edad > 25");
while (rs.next()) {
    System.out.println(rs.getInt("id") + " " +
                       rs.getString("nombre"));
}
```

```javascript
// JAVASCRIPT
const rows = db.prepare(
    "SELECT * FROM usuarios WHERE edad > 25").all();
```

---

## 4. EJEMPLO GUIADO: Inventario de tienda

**Problema:** Gestionar el inventario de una tienda: agregar productos, consultar stock bajo, actualizar precios.

### Paso 1: Crear la tabla

```sql
CREATE TABLE inventario (
    id INTEGER PRIMARY KEY,
    producto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER DEFAULT 0
);
```

### Paso 2: Insertar datos iniciales

```python
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.executescript("""
    CREATE TABLE inventario (...);
    INSERT INTO inventario VALUES (1, 'Laptop', 'Electronica', 999.99, 10);
    INSERT INTO inventario VALUES (2, 'Mouse', 'Electronica', 25.50, 50);
    INSERT INTO inventario VALUES (3, 'Camiseta', 'Ropa', 19.99, 100);
    INSERT INTO inventario VALUES (4, 'Zapatos', 'Ropa', 59.99, 30);
    INSERT INTO inventario VALUES (5, 'Libro', 'Libros', 14.99, 200);
""")
```

### Paso 3: Consultar productos con poco stock (< 50)

```python
c.execute("SELECT * FROM inventario WHERE stock < 50")
for row in c.fetchall():
    print(f"  {row[1]:10s} | Stock: {row[4]:3d}")
```

Salida:
```
  Laptop     | Stock:  10
  Mouse      | Stock:  50  (no, 50 no < 50)
  Camiseta   | Stock: 100
  Zapatos    | Stock:  30
  Libro      | Stock: 200
```

Espera, `stock < 50` da Laptop(10) y Zapatos(30). Correcto.

### Paso 4: Actualizar stock y consultar

```python
c.execute("UPDATE inventario SET stock = 60 WHERE producto = 'Mouse'")
c.execute("SELECT producto, stock FROM inventario WHERE categoria = 'Electronica'")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1]} unidades")
```

---

## 5. EJERCICIOS

Los ejercicios usan SQLite en memoria. Ya tienen los datos cargados; tu escribes las consultas SQL.

### 🟢 Ejercicio 1: SELECT con WHERE

En la tabla `usuarios` (id, nombre, edad), muestra los usuarios mayores de 25.

**Ejecuta:** `python scripts/runner.py 4 1 1`

---

### 🟡 Ejercicio 2: INSERT INTO

En la tabla `productos` (id, nombre, precio, stock), agrega un nuevo producto: Monitor, precio 299.99, stock 15.

**Ejecuta:** `python scripts/runner.py 4 1 2`

---

### 🔴 Ejercicio 3: UPDATE y DELETE

1. Actualiza el precio del Mouse a 30.00
2. Elimina el producto con id=3 (Teclado)

**Ejecuta:** `python scripts/runner.py 4 1 3`
