"""
SOLUCIONES - Cifrado y Hashing
Ejecuta desde raiz: python scripts/runner.py 10 05 [ejercicio] solucion
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Hashea un string con hashlib usando SHA-256"""
    import hashlib
    texto = input("Ingresa un texto: ")
    hash_obj = hashlib.sha256(texto.encode('utf-8'))
    print(f"Hash SHA-256: {hash_obj.hexdigest()}")

def solucion_2():
    """Verifica una contrasena comparando su hash"""
    import hashlib
    password_original = "secreta"
    hash_original = hashlib.sha256(password_original.encode()).hexdigest()
    intento = input("Ingresa la contrasena: ")
    hash_intento = hashlib.sha256(intento.encode()).hexdigest()
    if hash_intento == hash_original:
        print("Contrasena correcta")
    else:
        print("Contrasena incorrecta")

def solucion_3():
    """Codifica y decodifica un string en base64"""
    import base64
    texto = input("Ingresa un texto: ")
    codificado = base64.b64encode(texto.encode('utf-8'))
    decodificado = base64.b64decode(codificado).decode('utf-8')
    print(f"Original: {texto}")
    print(f"Codificado (base64): {codificado.decode('utf-8')}")
    print(f"Decodificado: {decodificado}")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            print(f">> SOLUCION {num + 1}: {soluciones[num].__doc__}")
            print("-" * 40)
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
