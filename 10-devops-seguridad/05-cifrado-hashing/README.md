# 05 - Cifrado y Hashing

## Glosario

- **Cifrado**: proceso que convierte datos legibles en ilegibles usando un algoritmo y una clave. Se puede revertir (descifrar) si se tiene la clave correcta.
- **Hashing**: funcion unidireccional que produce una cadena de longitud fija (hash) a partir de cualquier entrada. No se puede revertir.
- **Cifrado simetrico**: usa la misma clave para cifrar y descifrar (AES, DES).
- **Cifrado asimetrico**: usa un par de claves (publica para cifrar, privada para descifrar).
- **Salt**: valor aleatorio que se anade a una contrasena antes de hashearla para evitar rainbow tables.
- **Base64**: codificacion que convierte datos binarios en texto usando 64 caracteres seguros para transporte (no es cifrado).
- **SHA-256**: algoritmo de hash de 256 bits perteneciente a la familia SHA-2. Ampliamente usado para verificar integridad.
- **bcrypt**: algoritmo de hashing de contrasenas que incorpora automaticamente un salt y es deliberadamente lento para resistir ataques de fuerza bruta.
- **AES**: estandar de cifrado simetrico con claves de 128, 192 o 256 bits.
- **RSA**: algoritmo de cifrado asimetrico basado en la dificultad de factorizar numeros primos grandes.

## Conceptos clave

- **Hash vs Cifrado**: el hash es unidireccional (no se puede obtener el original), el cifrado es bidireccional (se puede descifrar con la clave). Para almacenar contrasenas se usa hash, no cifrado.
- **Integridad**: el hash permite verificar que un dato no ha sido modificado. Si el hash coincide, el dato original no cambio.
- **Confidencialidad**: el cifrado protege la informacion para que solo quien tiene la clave pueda leerla.
- **Autenticidad**: firmas digitales y MACs verifican que un mensaje viene de una fuente confiable.
- **Salt unico**: cada contrasena debe tener un salt diferente. Asi dos usuarios con la misma contrasena tendran distintos hashes.
- **Codificacion vs Cifrado**: base64 solo transforma la representacion de los datos, no los protege. Cualquiera puede decodificar base64 sin clave.

## Comparativa

| Operacion | Python | Java | JavaScript |
|-----------|--------|------|------------|
| Hash SHA-256 | `hashlib.sha256(dato.encode()).hexdigest()` | `MessageDigest.getInstance("SHA-256")` | `crypto.subtle.digest("SHA-256", data)` |
| Hash con bcrypt | `bcrypt.hashpw(passw, bcrypt.gensalt())` | `BCrypt.hashpw(password, BCrypt.gensalt())` | `bcrypt.hashSync(password, salt)` |
| Codificar base64 | `base64.b64encode(dato.encode())` | `Base64.getEncoder().encodeToString()` | `btoa(dato)` |
| Decodificar base64 | `base64.b64decode(dato).decode()` | `Base64.getDecoder().decode()` | `atob(dato)` |
| Cifrado AES | `Crypto.Cipher.AES` (pycryptodome) | `javax.crypto.Cipher` | `crypto.subtle.encrypt("AES-GCM", ...)` |

## Ejemplo guiado

**Problema**: Queremos almacenar una contrasena de forma segura usando hashing.

**Paso 1**: Hashear con SHA-256 (basico, sin salt).

```python
import hashlib
contrasena = "MiClaveSegura2024"
hash_resultado = hashlib.sha256(contrasena.encode()).hexdigest()
print(hash_resultado)
```

**Paso 2**: Verificar comparando hashes.

```python
hash_almacenado = hashlib.sha256("MiClaveSegura2024".encode()).hexdigest()
intento = "MiClaveSegura2024"
hash_intento = hashlib.sha256(intento.encode()).hexdigest()
if hash_intento == hash_almacenado:
    print("Contrasena correcta")
else:
    print("Contrasena incorrecta")
```

**Paso 3**: Codificar y decodificar con base64 para transmitir datos.

```python
import base64
texto = "datos sensibles"
codificado = base64.b64encode(texto.encode())
decodificado = base64.b64decode(codificado).decode()
print(f"Original: {texto}")
print(f"Codificado: {codificado.decode()}")
print(f"Decodificado: {decodificado}")
```

**Nota**: En produccion usa bcrypt (con salt incorporado) en lugar de SHA-256 para contrasenas.

## Referencia

| Funcion / Comando | Descripcion |
|-------------------|-------------|
| `hashlib.sha256(dato).hexdigest()` | Calcula hash SHA-256 y lo retorna como hexadecimal |
| `hashlib.sha256(dato).digest()` | Calcula hash SHA-256 y lo retorna como bytes |
| `base64.b64encode(dato)` | Codifica bytes a base64 |
| `base64.b64decode(dato)` | Decodifica base64 a bytes |
| `bcrypt.hashpw(passw, salt)` | Hashea contrasena con bcrypt (requiere pip install bcrypt) |
| `bcrypt.checkpw(passw, hash)` | Verifica contrasena contra hash bcrypt |
| `os.urandom(n)` | Genera n bytes aleatorios seguros (para crear salts) |

## Ejercicios

1. **SHA-256** - Hashea un string usando hashlib y muestra el resultado hexadecimal.
2. **Verificar contrasena** - Compara el hash de un intento contra el hash de una contrasena almacenada.
3. **Base64** - Codifica un string a base64 y luego decodificalo de vuelta.

**Ejecuta:** `python scripts/runner.py 10 05 [N]`
