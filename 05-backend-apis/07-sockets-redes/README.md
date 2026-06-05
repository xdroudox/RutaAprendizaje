# Sockets y Redes

## Pila TCP/IP

Capa | Protocolo | Funcion
-----|-----------|--------
Aplicacion | HTTP, FTP, SMTP | Datos de aplicacion
Transporte | TCP, UDP | Comunicacion extremo a extremo
Red | IP | Enrutamiento entre redes
Enlace | Ethernet, WiFi | Transferencia en el medio fisico

## TCP vs UDP

| Caracteristica | TCP | UDP |
|----------------|-----|-----|
| Conexion | Orientada a conexion | Sin conexion |
| Confiabilidad | Garantiza entrega | No garantiza |
| Orden | Mantiene orden | No garantiza orden |
| Velocidad | Mas lento | Mas rapido |
| Uso | HTTP, WebSockets | DNS, streaming |

## Sockets en Python

Un socket es un punto final de comunicacion entre dos procesos.

### Servidor TCP

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(1)
print("Servidor escuchando en puerto 9999...")

conn, addr = server.accept()
print(f"Conectado: {addr}")
data = conn.recv(1024)
print(f"Recibido: {data.decode()}")
conn.send(b"Hola desde el servidor!")
conn.close()
```

### Cliente TCP

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
client.send(b"Hola desde el cliente!")
resp = client.recv(1024)
print(f"Respuesta: {resp.decode()}")
client.close()
```

## IP y Puertos

- IP: identifica un dispositivo en la red (192.168.1.1)
- Puerto: identifica un proceso en el dispositivo (80, 443, 8080)
- Localhost: 127.0.0.1 (tu propia maquina)

## Procesos vs Hilos

| Aspecto | Proceso | Hilo |
|---------|---------|------|
| Memoria | Compartida separada | Compartida |
| Creacion | Costosa | Ligera |
| Paralelismo | Real (multi-CPU) | Concurrencia |
| Aislamiento | Total | Comparten memoria |

```python
import socket

# Cliente simple
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
resp = sock.recv(4096)
print(resp.decode())
sock.close()
```

Ejecuta: python ejercicios.py 1
