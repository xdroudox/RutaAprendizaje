import sys
import socket

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Cliente socket basico")
    print("=" * 50)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect(("example.com", 80))
        sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        respuesta = sock.recv(4096)
        print("Respuesta del servidor:")
        print(respuesta.decode(errors="replace")[:500])
    except Exception as e:
        print("Error:", e)
    finally:
        sock.close()

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Servidor eco simple")
    print("=" * 50)
    codigo = '''
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8888))
server.listen(1)
print("Servidor escuchando en puerto 8888...")

conn, addr = server.accept()
print(f"Conectado: {addr}")
data = conn.recv(1024)
print(f"Recibido: {data.decode()}")
conn.send(data)  # Eco
conn.close()
server.close()
'''
    print("Codigo del servidor eco:")
    print(codigo)
    print()
    print("Para probarlo, ejecuta este codigo en una terminal y")
    print("en otra terminal conectate con: telnet localhost 8888")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Identificar capas TCP/IP")
    print("=" * 50)
    print("Distribucion de protocolos por capa:")
    print()
    tabla = [
        ("Aplicacion", "HTTP, FTP, SMTP, DNS"),
        ("Transporte", "TCP, UDP"),
        ("Red", "IP"),
        ("Enlace", "Ethernet, WiFi"),
    ]
    for capa, protocolos in tabla:
        print(f"  {capa:12s} -> {protocolos}")
    print()
    print("Asignacion:")
    print("  HTTP y FTP -> Capa de Aplicacion")
    print("  TCP y UDP  -> Capa de Transporte")
    print("  IP         -> Capa de Red")
    print("  Ethernet   -> Capa de Enlace")

def menu():
    print("SOLUCIONES - SOCKETS Y REDES")
    print("1 - Cliente socket basico")
    print("2 - Servidor eco simple")
    print("3 - Identificar capas TCP/IP")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    if num == "1":
        solucion_1()
    elif num == "2":
        solucion_2()
    elif num == "3":
        solucion_3()
    else:
        print("Solucion no valida. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
