import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print(">> EJERCICIO 1: Detecta SQL Injection")
    print("")
    print("Dado el siguiente codigo vulnerable, identifica el problema")
    print("y escribe la version corregida usando consultas parametrizadas.")
    print("")
    print("  usuario = input('Usuario: ')")
    print("  query = f'SELECT * FROM usuarios WHERE nombre = \"{usuario}\"'")
    print("")
    print("# --- TU CODIGO AQUI ---")
    pass

def ejercicio_2():
    print(">> EJERCICIO 2: Sanitizar XSS")
    print("")
    print("Escribe una funcion que reciba un texto ingresado por el usuario")
    print("y lo sanitice para evitar XSS, reemplazando < > & \" ' por sus")
    print("entidades HTML.")
    print("")
    print("# --- TU CODIGO AQUI ---")
    pass

def ejercicio_3():
    print(">> EJERCICIO 3: Verificar CSP header")
    print("")
    print("Simula la respuesta HTTP de un servidor y verifica si incluye")
    print("el header Content-Security-Policy. Si no lo incluye, muestra")
    print("una advertencia de seguridad.")
    print("")
    print("PISTA: usa un diccionario para simular los headers")
    print("")
    print("# --- TU CODIGO AQUI ---")
    pass

def menu():
    print("=== Seguridad Web - Ejercicios ===")
    print("1. Detectar SQL Injection")
    print("2. Sanitizar XSS")
    print("3. Verificar CSP header")
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
