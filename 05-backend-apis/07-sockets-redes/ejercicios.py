"""
EJERCICIOS - Sockets y Redes
Ejecuta desde raiz: python scripts/runner.py 5 7 [ejercicio]

Niveles:
  🟢 Ej 1: Crear socket cliente TCP
  🟡 Ej 2: Enviar mensaje y recibir respuesta
  🔴 Ej 3: Servidor echo simple (con hilo)

Pistas: python scripts/runner.py 5 7 N -p [1|2|3]
"""

import sys
import socket

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Crear socket cliente TCP"""
    print(">> 🟢 EJERCICIO 1: Crear socket cliente TCP")
    print("-" * 50)

    host = "localhost"
    puerto = 9999

    print(f"Conectarse a {host}:{puerto}")

    if pista == 1:
        print("\n💡 Pista 1: Crear socket e intentar conectar:")
        print("  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
        print("  sock.settimeout(3)")
        print("  sock.connect((host, puerto))")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Maneja errores con try/except:")
        print("  try:")
        print("      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
        print("      sock.settimeout(3)")
        print("      sock.connect((host, puerto))")
        print("      print(f'Conectado a {host}:{puerto}')")
        print("      sock.close()")
        print("  except ConnectionRefusedError:")
        print("      print('El servidor no esta corriendo')")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Si no hay servidor, la solucion demuestra")
        print("  que el codigo maneja correctamente el error")
        print("  ConnectionRefusedError sin crashear.")
        return

    print("\nCrea un socket TCP, configuralo con timeout de 3 segundos")
    print("e intenta conectarte a localhost:9999.")
    print("Maneja la excepcion si el servidor no esta corriendo.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Enviar mensaje y recibir respuesta"""
    print(">> 🟡 EJERCICIO 2: Enviar y recibir datos")
    print("-" * 50)

    host = "localhost"
    puerto = 9999
    mensaje = "Hola desde el cliente!"

    print(f"Mensaje a enviar: '{mensaje}'")

    if pista == 1:
        print("\n💡 Pista 1: Secuencia completa:")
        print("  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
        print("  sock.settimeout(3)")
        print("  sock.connect((host, puerto))")
        print("  sock.send(mensaje.encode())")
        print("  respuesta = sock.recv(1024)")
        print("  print(f'Recibido: {respuesta.decode()}')")
        print("  sock.close()")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Usa encode()/decode() para strings:")
        print("  Los sockets trabajan con bytes, no strings:")
        print("    mensaje.encode() → str a bytes")
        print("    respuesta.decode() → bytes a str")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Necesitas un servidor corriendo")
        print("  Puedes usar netcat: nc -l -p 9999")
        print("  O ejecutar el ej 3 (servidor echo) en otra terminal")
        return

    print("\nConectate a localhost:9999, envia el mensaje,")
    print("recibe la respuesta y cierra la conexion.")
    print("Usa encode() para enviar y decode() para recibir.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Servidor echo simple (con hilo)"""
    print(">> 🔴 EJERCICIO 3: Servidor echo simple")
    print("-" * 50)

    host = "localhost"
    puerto = 9999

    if pista == 1:
        print("\n💡 Pista 1: Funcion del servidor:")
        print("  def echo_server():")
        print("      servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
        print("      servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)")
        print("      servidor.bind((host, puerto))")
        print("      servidor.listen(1)")
        print("      conn, addr = servidor.accept()")
        print("      datos = conn.recv(1024)")
        print("      conn.send(datos)  # echo")
        print("      conn.close()")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Ejecuta el servidor en un hilo:")
        print("  import threading")
        print("  hilo = threading.Thread(target=echo_server, daemon=True)")
        print("  hilo.start()")
        print("  time.sleep(0.5)  # espera a que el servidor este listo")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Desde el hilo principal, actua como cliente:")
        print("  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
        print("  sock.settimeout(3)")
        print("  sock.connect((host, puerto))")
        print("  sock.send(b'Hola servidor!')")
        print("  resp = sock.recv(1024)")
        print("  print(f'Cliente recibio: {resp.decode()}')")
        return

    print("\nCrea un servidor TCP que reciba datos y los devuelva (echo).")
    print("Ejecutalo en un hilo separado y desde el hilo principal")
    print("actua como cliente para probarlo.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            pista = 0
            if "-p" in sys.argv:
                idx = sys.argv.index("-p")
                if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                    pista = int(sys.argv[idx + 1])
            ejercicios[num](pista)
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__ or ""
            print(f"  {i}. {doc}")
