import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Cliente socket basico")
    print("=" * 50)
    print()
    print("TAREA: Crea un socket cliente que se conecte a")
    print("example.com en el puerto 80 y envie una peticion HTTP GET")
    print("para obtener la pagina principal.")
    print()
    print("Pasos:")
    print("  1. Crear socket (AF_INET, SOCK_STREAM)")
    print("  2. Conectar a ('example.com', 80)")
    print("  3. Enviar: b'GET / HTTP/1.1\\r\\nHost: example.com\\r\\n\\r\\n'")
    print("  4. Recibir respuesta con recv(4096)")
    print("  5. Imprimir y cerrar")
    print()
    print("PISTA: socket.socket(), .connect(), .send(), .recv(), .close()")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Servidor eco simple")
    print("=" * 50)
    print()
    print("TAREA: Escribe un servidor socket que:")
    print("  1. Escuche en localhost puerto 8888")
    print("  2. Acepte una conexion")
    print("  3. Reciba un mensaje")
    print("  4. Envie el mismo mensaje de vuelta (eco)")
    print("  5. Cierre la conexion")
    print()
    print("NOTA: Este ejercicio es solo para escribir el codigo.")
    print("No se ejecutara el servidor aqui para no bloquear.")
    print()
    print("PISTA: server = socket.socket(); server.bind(('localhost', 8888)); server.listen(1); conn, addr = server.accept(); data = conn.recv(1024); conn.send(data); conn.close()")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Identificar capas TCP/IP")
    print("=" * 50)
    print()
    print("TAREA: Asigna cada protocolo a su capa en el modelo TCP/IP.")
    print()
    protocolos = ["HTTP", "TCP", "IP", "Ethernet", "UDP", "FTP"]
    capas = ["Aplicacion", "Transporte", "Red", "Enlace"]
    print("Protocolos:", protocolos)
    print("Capas:", capas)
    print()
    print("PISTA: HTTP y FTP son de Aplicacion, TCP y UDP de Transporte,")
    print("IP es de Red, Ethernet es de Enlace.")

pistas = {
    "1": "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(('example.com', 80)); s.send(b'GET / HTTP/1.1\\r\\nHost: example.com\\r\\n\\r\\n'); print(s.recv(4096).decode()); s.close()",
    "2": "import socket; s = socket.socket(); s.bind(('localhost', 8888)); s.listen(1); print('Esperando...'); conn, addr = s.accept(); print('Conectado:', addr); data = conn.recv(1024); conn.send(data); conn.close(); s.close()",
    "3": "HTTP -> Aplicacion, FTP -> Aplicacion, TCP -> Transporte, UDP -> Transporte, IP -> Red, Ethernet -> Enlace"
}

def menu():
    print("=" * 50)
    print("SOCKETS Y REDES - EJERCICIOS")
    print("=" * 50)
    print("1 - Cliente socket basico")
    print("2 - Servidor eco simple")
    print("3 - Identificar capas TCP/IP")
    print()
    print("Usa: python ejercicios.py <numero>")
    print("     python ejercicios.py <numero> -p  (pista)")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    mostrar_pista = "-p" in args
    if mostrar_pista and num in pistas:
        print("=== PISTA ===")
        print(pistas[num])
        print()
    if num == "1":
        ejercicio_1()
    elif num == "2":
        ejercicio_2()
    elif num == "3":
        ejercicio_3()
    else:
        print("Ejercicio no valido. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
