"""
SOLUCIONES - Sockets y Redes
Ejecuta: python scripts/runner.py 5 7 [ejercicio] -s
"""

import sys
import socket
import threading
import time

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Crear socket cliente TCP")
    print("=" * 50)

    host = "localhost"
    puerto = 9999

    print("--- CODIGO ---")
    print("try:")
    print("    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
    print("    sock.settimeout(3)")
    print("    sock.connect((host, puerto))")
    print("    print(f'Conectado a {host}:{puerto}')")
    print("    sock.close()")
    print("except ConnectionRefusedError:")
    print("    print('El servidor no esta corriendo')")
    print()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, puerto))
        print(f"  Conectado a {host}:{puerto}")
        sock.close()
    except ConnectionRefusedError:
        print(f"  No se pudo conectar a {host}:{puerto}. El servidor no esta corriendo.")

    print()
    print("--- EXPLICACION ---")
    print("""
Creacion de un socket TCP:

  AF_INET     → IPv4
  SOCK_STREAM → TCP (orientado a conexion)
  settimeout  → tiempo maximo de espera

El error ConnectionRefusedError ocurre cuando no hay
ningun servidor escuchando en ese puerto. Siempre
debemos manejar esta excepcion.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Enviar y recibir datos")
    print("=" * 50)

    host = "localhost"
    puerto = 9999
    mensaje = "Hola desde el cliente!"

    print("--- CODIGO ---")
    print("sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
    print("sock.settimeout(3)")
    print("sock.connect((host, puerto))")
    print("sock.send(mensaje.encode())")
    print("respuesta = sock.recv(1024)")
    print("print(f'Recibido: {respuesta.decode()}')")
    print("sock.close()")
    print()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, puerto))
        sock.send(mensaje.encode())
        respuesta = sock.recv(1024)
        print(f"  Enviado: {mensaje}")
        print(f"  Recibido: {respuesta.decode()}")
        sock.close()
    except ConnectionRefusedError:
        print(f"  No se pudo conectar. Inicia el servidor primero.")

    print()
    print("--- EXPLICACION ---")
    print("""
Los sockets trabajan con bytes, no strings:

  mensaje.encode()  → 'Hola' → b'Hola'  (str a bytes)
  respuesta.decode() → b'Hola' → 'Hola'  (bytes a str)

  recv(1024) recibe hasta 1024 bytes.
  Si el mensaje es mayor, se necesitan multiples recv().

  send() no garantiza enviar todos los datos de una vez.
  Para mensajes grandes usa sendall().
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Servidor echo simple")
    print("=" * 50)

    host = "localhost"
    puerto = 9999

    def echo_server():
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((host, puerto))
        servidor.listen(1)
        conn, addr = servidor.accept()
        datos = conn.recv(1024)
        conn.send(datos)
        conn.close()
        servidor.close()

    print("--- CODIGO ---")
    print("def echo_server():")
    print("    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
    print("    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)")
    print("    servidor.bind((host, puerto))")
    print("    servidor.listen(1)")
    print("    conn, addr = servidor.accept()")
    print("    datos = conn.recv(1024)")
    print("    conn.send(datos)  # echo")
    print("    conn.close()")
    print()
    print("hilo = threading.Thread(target=echo_server, daemon=True)")
    print("hilo.start()")
    print("time.sleep(0.5)")
    print("sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
    print("sock.connect((host, puerto))")
    print("sock.send(b'Hola servidor!')")
    print("resp = sock.recv(1024)")
    print("print(f'Cliente recibio: {resp.decode()}')")
    print()

    hilo = threading.Thread(target=echo_server, daemon=True)
    hilo.start()
    time.sleep(0.5)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    sock.connect((host, puerto))
    sock.send(b"Hola servidor!")
    resp = sock.recv(1024)
    print(f"  Cliente recibio: {resp.decode()}")
    sock.close()
    hilo.join(timeout=1)

    print()
    print("--- EXPLICACION ---")
    print("""
El servidor echo:

  1. bind()   → asigna IP:puerto
  2. listen() → se pone en modo escucha
  3. accept() → bloquea hasta que llegue un cliente
  4. recv()   → recibe datos
  5. send()   → devuelve los mismos datos (echo)
  6. close()  → cierra la conexion

SO_REUSEADDR permite reusar el puerto inmediatamente
despues de cerrar (evita 'Address already in use').

En produccion:
  - Usa servidores asincronos (asyncio) en lugar de hilos
  - Implementa manejo de multiples clientes simultaneos
  - Usa protocolos de aplicacion (HTTP) sobre TCP
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
