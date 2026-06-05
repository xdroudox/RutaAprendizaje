import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import hashlib

def ejercicio_1():
    print(">> SOLUCION EJERCICIO 1: Hashing SHA-256")
    texto = input("Ingresa un texto: ")
    hash_obj = hashlib.sha256(texto.encode('utf-8'))
    print(f"Hash SHA-256: {hash_obj.hexdigest()}")

def ejercicio_2():
    print(">> SOLUCION EJERCICIO 2: Verificar contrasena")
    password_original = "secreta"
    hash_original = hashlib.sha256(password_original.encode()).hexdigest()
    intento = input("Ingresa la contrasena: ")
    hash_intento = hashlib.sha256(intento.encode()).hexdigest()
    if hash_intento == hash_original:
        print("Contrasena correcta")
    else:
        print("Contrasena incorrecta")

def ejercicio_3():
    print(">> SOLUCION EJERCICIO 3: Cifrado simetrico con Fernet")
    from cryptography.fernet import Fernet
    clave = Fernet.generate_key()
    cipher = Fernet(clave)
    mensaje = b"Mensaje secreto"
    cifrado = cipher.encrypt(mensaje)
    descifrado = cipher.decrypt(cifrado)
    print(f"Original: {mensaje}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")

def menu():
    print("=== Cifrado y Hashing - Soluciones ===")
    print("1. Hashing SHA-256")
    print("2. Verificar contrasena")
    print("3. Cifrado simetrico")
    print("0. Salir")
    return input("Selecciona un ejercicio: ")

def main():
    while True:
        opcion = menu()
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida")
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
