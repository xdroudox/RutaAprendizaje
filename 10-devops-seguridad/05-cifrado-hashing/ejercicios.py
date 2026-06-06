"""
EJERCICIOS - Cifrado y Hashing
Ejecuta desde raiz: python scripts/runner.py 10 05 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """Hashear un string con SHA-256 usando hashlib"""
    import hashlib
    print(">> EJERCICIO 1: Hashear un string con SHA-256")
    print("-" * 40)
    texto = "Hola Mundo"
    print(f"Texto a hashear: '{texto}'")
    print()
    print("Instrucciones:")
    print("  1. Codifica el texto a bytes con .encode('utf-8')")
    print("  2. Llama a hashlib.sha256() con los bytes")
    print("  3. Convierte el hash a hexadecimal con .hexdigest()")
    print("  4. Imprime el resultado")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("hash_resultado = hashlib.sha256(...)")
    print("print(hash_resultado)")
    if pista:
        print("\n" + "=" * 40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  .encode() convierte un string a bytes.")
        print("  Ejemplo: texto.encode('utf-8')")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  hash_object = hashlib.sha256(texto.encode('utf-8'))")
        print("  hash_hex = hash_object.hexdigest()")
        print("  print('Hash SHA-256:', hash_hex)")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  texto_bytes = texto.encode('utf-8')")
        print("  hash_obj = hashlib.sha256(texto_bytes)")
        print("  hash_hex = hash_obj.hexdigest()")
        print("  print(f'Hash SHA-256: {hash_hex}')")


def ejercicio_2(pista=0):
    """Verificar una contrasena comparando hashes"""
    import hashlib
    print(">> EJERCICIO 2: Verificar una contrasena comparando hashes")
    print("-" * 40)
    password_original = "secreta"
    hash_original = hashlib.sha256(password_original.encode()).hexdigest()
    intento = "secreta"
    print(f"Password original: '{password_original}'")
    print(f"Intento: '{intento}'")
    print()
    print("Instrucciones:")
    print("  1. Hashea el intento con SHA-256")
    print("  2. Compara el hash resultante con hash_original")
    print("  3. Si coinciden, imprime 'Contrasena correcta'")
    print("  4. Si no, imprime 'Contrasena incorrecta'")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("hash_intento = ...")
    print("if ... :")
    print("    print('Contrasena correcta')")
    print("else:")
    print("    print('Contrasena incorrecta')")
    if pista:
        print("\n" + "=" * 40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Usa el mismo proceso que en el ejercicio 1 para hashear.")
        print("  Compara con el operador == entre dos strings.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  hash_intento = hashlib.sha256(intento.encode()).hexdigest()")
        print("  if hash_intento == hash_original:")
        print("      print('Contrasena correcta')")
        print("  else:")
        print("      print('Contrasena incorrecta')")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  hash_intento = hashlib.sha256(intento.encode()).hexdigest()")
        print("  if hash_intento == hash_original:")
        print("      print('Acceso concedido. Contrasena correcta')")
        print("  else:")
        print("      print('Acceso denegado. Contrasena incorrecta')")


def ejercicio_3(pista=0):
    """Codificar y decodificar un string en base64"""
    import base64
    print(">> EJERCICIO 3: Codificar y decodificar en base64")
    print("-" * 40)
    texto = "Hola Mundo"
    print(f"Texto a codificar: '{texto}'")
    print()
    print("Instrucciones:")
    print("  1. Codifica el texto a bytes con .encode()")
    print("  2. Llama a base64.b64encode() para codificar")
    print("  3. Decodifica el resultado con base64.b64decode()")
    print("  4. Convierte los bytes de vuelta a string con .decode()")
    print("  5. Imprime el original, codificado y decodificado")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("codificado = base64.b64encode(...)")
    print("decodificado = base64.b64decode(...)")
    if pista:
        print("\n" + "=" * 40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  base64.b64encode() recibe bytes y retorna bytes.")
        print("  base64.b64decode() recibe bytes y retorna bytes.")
        print("  Usa .decode() para convertir bytes a string.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  texto_bytes = texto.encode('utf-8')")
        print("  codificado = base64.b64encode(texto_bytes)")
        print("  decodificado_bytes = base64.b64decode(codificado)")
        print("  decodificado = decodificado_bytes.decode('utf-8')")
        print("  print(f'Original: {texto}')")
        print("  print(f'Codificado: {codificado.decode()}')")
        print("  print(f'Decodificado: {decodificado}')")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  codificado = base64.b64encode(texto.encode('utf-8'))")
        print("  decodificado = base64.b64decode(codificado).decode('utf-8')")
        print("  print(f'Original:    {texto}')")
        print("  print(f'Codificado:  {codificado.decode(\"utf-8\")}')")
        print("  print(f'Decodificado: {decodificado}')")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    pista_level = 0
    if "-p" in sys.argv:
        idx = sys.argv.index("-p")
        if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
            pista_level = int(sys.argv[idx + 1])
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num](pista=pista_level)
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
