# Normalizacion

La normalizacion es el proceso de organizar datos para reducir redundancia
y evitar anomalias.

## Primera Forma Normal (1NF)

- Cada celda contiene un solo valor (atomo)
- No hay grupos repetitivos
- Cada fila es unica

Antes (no 1NF):
| id | nombre | telefonos          |
|----|--------|--------------------|
| 1  | Ana    | 123, 456           |

Despues (1NF):
| id | nombre | telefono |
|----|--------|----------|
| 1  | Ana    | 123      |
| 1  | Ana    | 456      |

## Segunda Forma Normal (2NF)

- Esta en 1NF
- Todos los atributos no clave dependen de la clave completa
- (Aplica solo en tablas con clave compuesta)

## Tercera Forma Normal (3NF)

- Esta en 2NF
- No hay dependencias transitivas (atributos no clave que dependen
  de otros atributos no clave)

Antes (no 3NF):
| empleado_id | departamento | ciudad_departamento |

La ciudad depende del departamento, no del empleado.

Despues (3NF):
| empleado_id | departamento |
| departamento | ciudad_departamento |

## BCNF (Boyce-Codd Normal Form)

- Version mas estricta de 3NF
- Cada determinante debe ser clave candidata

## Desnormalizacion

A veces se desnormaliza intencionalmente para mejorar rendimiento en
lecturas, aceptando redundancia controlada.
