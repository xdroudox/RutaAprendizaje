# Transacciones ACID

## Contenido
- Transacciones con BEGIN, COMMIT y ROLLBACK
- Propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad)
- Manejo de errores y consistencia de datos

## Ejercicios

| #  | Ejercicio                                                      |
|----|----------------------------------------------------------------|
| 1  | BEGIN, INSERT, COMMIT (transferencia bancaria)                 |
| 2  | ROLLBACK (revertir cambios ante error)                         |
| 3  | Simular fallo y mostrar que ROLLBACK mantiene consistencia     |

## Comandos

```bash
python scripts/runner.py 4 5 1
python scripts/runner.py 4 5 2
python scripts/runner.py 4 5 3
```

## Resumen

```sql
-- Iniciar transaccion
BEGIN;

-- Operaciones
UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 200 WHERE id = 2;

-- Confirmar cambios
COMMIT;

-- Revertir cambios
ROLLBACK;
```

## Propiedades ACID

| Propiedad    | Descripcion                                              |
|-------------|----------------------------------------------------------|
| Atomicidad  | La transaccion se ejecuta completamente o no se ejecuta  |
| Consistencia| Los datos siempre cumplen las reglas de integridad       |
| Aislamiento | Las transacciones concurrentes no interfieren entre si   |
| Durabilidad | Los cambios confirmados persisten incluso tras fallos    |
