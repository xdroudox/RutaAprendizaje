"""
SOLUCIONES - Sockets y Redes
Ejecuta desde raiz: python scripts/runner.py 5 7 1 -s
"""
import sys
import socket
import threading
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Crear socket cliente TCP que se conecte a un host"""
    host = "localhost"
    puerto = 9999
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, puerto))
        print(f"Conectado a {host}:{puerto}")
        sock.close()
    except ConnectionRefusedError:
        print(f"No se pudo conectar a {host}:{puerto}. El servidor no esta corriendo.")
    except Exception as e:
        print(f"Error: {e}")

def ejercicio_2():
    """Enviar mensaje y recibir respuesta"""
    host = "localhost"
    puerto = 9999
    mensaje = "Hola desde el cliente!"
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, puerto))
        sock.send(mensaje.encode())
        respuesta = sock.recv(1024)
        print(f"Enviado: {mensaje}")
        print(f"Recibido: {respuesta.decode()}")
        sock.close()
    except ConnectionRefusedError:
        print(f"No se pudo conectar a {host}:{puerto}. Inicia el servidor primero.")

def ejercicio_3():
    """Servidor echo simple"""
    host = "localhost"
    puerto = 9999
    def echo_server():
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((host, puerto))
        servidor.listen(1)
        print(f"Servidor escuchando en {host}:{puerto}")
        conn, addr = servidor.accept()
        print(f"Cliente conectado: {addr}")
        datos = conn.recv(1024)
        print(f"Recibido: {datos.decode()}")
        conn.send(datos)
        print(f"Echo enviado")
        conn.close()
        servidor.close()
    hilo = threading.Thread(target=echo_server, daemon=True)
    hilo.start()
    import time
    time.sleep(0.5)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    sock.connect((host, puerto))
    sock.send(b"Hola servidor!")
    resp = sock.recv(1024)
    print(f"Cliente recibio: {resp.decode()}")
    sock.close()
    hilo.join(timeout=1)
    print("Demo de servidor echo completada.")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> SOLUCION {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("SOLUCIONES:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
