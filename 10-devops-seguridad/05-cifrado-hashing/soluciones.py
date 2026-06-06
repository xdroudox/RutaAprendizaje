"""
SOLUCIONES - Cifrado y Hashing
Ejecuta desde raiz: python scripts/runner.py 10 05 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    """Hashear un string con SHA-256 usando hashlib"""
    import hashlib
    texto = "Hola Mundo"
    texto_bytes = texto.encode('utf-8')
    hash_obj = hashlib.sha256(texto_bytes)
    hash_hex = hash_obj.hexdigest()
    assert len(hash_hex) == 64
    assert isinstance(hash_hex, str)
    print(">> SOLUCION 1: Hashear un string con SHA-256")
    print("-" * 40)
    print("import hashlib")
    print("texto = 'Hola Mundo'")
    print("texto_bytes = texto.encode('utf-8')")
    print("hash_obj = hashlib.sha256(texto_bytes)")
    print("hash_hex = hash_obj.hexdigest()")
    print(f"print(hash_hex)  # {hash_hex}")
    print()
    print(f"Texto original: {texto}")
    print(f"Hash SHA-256:   {hash_hex}")
    print()
    print("Explicacion:")
    print("  El texto se convierte a bytes, se pasa a hashlib.sha256(),")
    print("  y .hexdigest() retorna el hash como string hexadecimal de 64 caracteres.")


def solucion_2():
    """Verificar una contrasena comparando hashes"""
    import hashlib
    password_original = "secreta"
    hash_original = hashlib.sha256(password_original.encode()).hexdigest()
    intento = "secreta"
    hash_intento = hashlib.sha256(intento.encode()).hexdigest()
    assert hash_intento == hash_original
    print(">> SOLUCION 2: Verificar una contrasena comparando hashes")
    print("-" * 40)
    print("import hashlib")
    print()
    print("# Almacenar hash de la contrasena original")
    print("password_original = 'secreta'")
    print("hash_original = hashlib.sha256(password_original.encode()).hexdigest()")
    print()
    print("# Comparar con el intento")
    print("intento = 'secreta'")
    print("hash_intento = hashlib.sha256(intento.encode()).hexdigest()")
    print("if hash_intento == hash_original:")
    print("    print('Contrasena correcta')")
    print("else:")
    print("    print('Contrasena incorrecta')")
    print()
    print(f"Hash original: {hash_original}")
    print(f"Hash intento:  {hash_intento}")
    print(f"Resultado: {'Contrasena correcta' if hash_intento == hash_original else 'Contrasena incorrecta'}")
    print()
    print("Explicacion:")
    print("  Se compara el hash del intento contra el hash almacenado.")
    print("  Si coinciden, la contrasena es correcta. Nunca se guarda la contrasena original.")


def solucion_3():
    """Codificar y decodificar un string en base64"""
    import base64
    texto = "Hola Mundo"
    codificado = base64.b64encode(texto.encode('utf-8'))
    decodificado = base64.b64decode(codificado).decode('utf-8')
    assert decodificado == texto
    print(">> SOLUCION 3: Codificar y decodificar en base64")
    print("-" * 40)
    print("import base64")
    print("texto = 'Hola Mundo'")
    print("codificado = base64.b64encode(texto.encode('utf-8'))")
    print("decodificado = base64.b64decode(codificado).decode('utf-8')")
    print()
    print(f"Original:    {texto}")
    print(f"Codificado:  {codificado.decode('utf-8')}")
    print(f"Decodificado: {decodificado}")
    print()
    print("Explicacion:")
    print("  base64 convierte datos binarios a texto usando 64 caracteres seguros.")
    print("  Se usa para transmitir datos en URLs, JSON, o emails.")
    print("  No es cifrado: cualquiera puede decodificarlo sin clave.")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
