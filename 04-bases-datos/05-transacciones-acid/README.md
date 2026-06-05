# Transacciones ACID

## ACID

- **Atomicity** (Atomicidad): La transaccion se ejecuta completa o no se ejecuta.
- **Consistency** (Consistencia): La base de datos pasa de un estado valido a otro.
- **Isolation** (Aislamiento): Las transacciones concurrentes no interfieren entre si.
- **Durability** (Durabilidad): Una vez confirmada, la transaccion persiste.

## BEGIN

Inicia una transaccion.

```sql
BEGIN;
```

## COMMIT

Confirma los cambios de la transaccion actual.

```sql
COMMIT;
```

## ROLLBACK

Revierte todos los cambios desde el BEGIN.

```sql
ROLLBACK;
```

## Ejemplo tipico (transferencia bancaria)

```sql
BEGIN;
UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
```

Si algo falla, se hace ROLLBACK y ambas cuentas quedan como antes.
