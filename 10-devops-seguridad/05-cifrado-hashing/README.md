# 05 - Cifrado y Hashing

## Conceptos clave

- **Hash**: funcion unidireccional. No se puede revertir.
- **Cifrado simetrico**: misma clave para cifrar y descifrar (AES).
- **Cifrado asimetrico**: clave publica para cifrar, privada para descifrar (RSA).
- **JWT**: JSON Web Token, firma digital basada en HMAC o RSA.
- **Salt**: valor aleatorio anadido al hash para evitar rainbow tables.

## Algoritmos

| Algoritmo | Tipo | Uso |
|-----------|------|-----|
| SHA-256 | Hash | Integridad de datos |
| bcrypt | Hash | Contrasenas |
| AES-256 | Simetrico | Cifrado de datos |
| RSA | Asimetrico | Intercambio de claves |
| HMAC | Hash con clave | Firmas |
