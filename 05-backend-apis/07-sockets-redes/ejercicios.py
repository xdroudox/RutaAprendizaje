"""
EJERCICIOS - Sockets y Redes
Ejecuta desde raiz: python scripts/runner.py 5 7 [ejercicio]
"""
import sys
import socket
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Crear socket cliente TCP que se conecte a un host"""
    host = "localhost"
    puerto = 9999
    # Crea un socket TCP, conectate al host:puerto
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_2():
    """Enviar mensaje y recibir respuesta"""
    host = "localhost"
    puerto = 9999
    mensaje = "Hola desde el cliente!"
    # Conectate, envia el mensaje codificado, recibe respuesta, cierra
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_3():
    """Servidor echo simple"""
    host = "localhost"
    puerto = 9999
    # Crea un servidor TCP que reciba datos y los devuelva (echo)
    # Debe ejecutarse en un hilo separado o como demostracion
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
