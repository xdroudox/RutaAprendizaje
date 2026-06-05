import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import hashlib

def ejercicio_1():
    print(">> EJERCICIO 1: Hashing SHA-256")
    print("")
    print("Solicita al usuario un texto por consola y muestra su hash SHA-256.")
    print("")
    print("# --- TU CODIGO AQUI ---")
    pass

def ejercicio_2():
    print(">> EJERCICIO 2: Verificar contrasena con hashlib")
    print("")
    print("Almacena el hash SHA-256 de la contrasena 'secreta'. Luego pide")
    print("al usuario una contrasena, calcula su hash y comprueba si coincide.")
    print("")
    print("# --- TU CODIGO AQUI ---")
    pass

def ejercicio_3():
    print(">> EJERCICIO 3: Cifrado simetrico simple")
    print("")
    print("Usa la libreria cryptography (o implementa tu propio cifrado simple)")
    print("para cifrar y descifrar un mensaje con una clave fija.")
    print("Muestra el mensaje original, el cifrado y el descifrado.")
    print("")
    print("PISTA: from cryptography.fernet import Fernet")
    print("")
    print("# --- TU CODIGO AQUI ---")
    pass

def menu():
    print("=== Cifrado y Hashing - Ejercicios ===")
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
