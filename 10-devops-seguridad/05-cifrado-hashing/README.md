# 05 - Cifrado y Hashing

## Conceptos clave

- **Hash**: funcion unidireccional. No se puede revertir.
- **Cifrado simetrico**: misma clave para cifrar y descifrar (AES).
- **Cifrado asimetrico**: clave publica para cifrar, privada para descifrar (RSA).
- **Salt**: valor aleatorio anadido al hash para evitar rainbow tables.

## Algoritmos

| Algoritmo | Tipo | Uso |
|-----------|------|-----|
| SHA-256 | Hash | Integridad de datos |
| bcrypt | Hash | Contrasenas |
| AES-256 | Simetrico | Cifrado de datos |
| base64 | Codificacion | Transferencia de datos |

## Ejercicios

1. **SHA-256** - Hashea un string con hashlib.
2. **Verificar contrasena** - Compara hashes para validar.
3. **Base64** - Codifica y decodifica con base64.

**Ejecuta:** `python scripts/runner.py 10 05 [ejercicio]`
