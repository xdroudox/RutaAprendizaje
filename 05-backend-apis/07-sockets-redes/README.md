# Sockets y Redes

## Contenido
- Modelo Cliente-Servidor TCP
- Creacion de sockets (cliente y servidor)
- Envio y recepcion de datos
- Servidor echo

---

## 1. Que es un Socket?

Un socket es un punto final de comunicacion entre dos programas a traves de una red. Es el mecanismo fundamental de internet.

### Modelo Cliente-Servidor TCP

```
Servidor:                         Cliente:
socket() ← crear socket          socket() ← crear socket
bind()   ← asignar IP:puerto     |
listen() ← escuchar conexiones   |
accept() ← aceptar cliente       connect() ← conectar al servidor
recv()   ← recibir datos <------ send() ← enviar datos
send()   ← enviar datos -------> recv() ← recibir datos
close()  ← cerrar conexion       close() ← cerrar conexion
```

---

## 2. Funciones principales

| Funcion      | Descripcion |
|-------------|-------------|
| `socket()`  | Crea un socket (AF_INET=IPv4, SOCK_STREAM=TCP) |
| `bind()`    | Asigna direccion IP y puerto al socket |
| `listen()`  | Pone el socket en modo escucha |
| `accept()`  | Acepta una conexion entrante (bloqueante) |
| `connect()` | Conecta a un servidor remoto |
| `send()`    | Envia datos |
| `recv()`    | Recibe datos (buffer size en bytes) |
| `close()`   | Cierra el socket |

---

## 3. Glosario

| Termino      | Definicion |
|-------------|-----------|
| **Socket**  | Canal de comunicacion bidireccional entre procesos |
| **TCP**     | Transmission Control Protocol - protocolo orientado a conexion |
| **IP**      | Internet Protocol - direccion del dispositivo |
| **Puerto**  | Numero que identifica el servicio (16 bits, 0-65535) |
| **Cliente** | Inicia la conexion |
| **Servidor** | Escucha y acepta conexiones |
| **Echo**    | Servidor que devuelve exactamente lo que recibe |

---

## 4. Comparativa entre lenguajes

### Python
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))
sock.send(b"Hola")
resp = sock.recv(1024)
sock.close()
```

### JavaScript (Node.js)
```javascript
const net = require('net');
const client = net.createConnection({port: 9999}, () => {
    client.write('Hola');
});
client.on('data', (data) => console.log(data.toString()));
```

### Java
```java
Socket socket = new Socket("localhost", 9999);
PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
out.println("Hola");
System.out.println(in.readLine());
socket.close();
```

---

## 5. Ejemplo guiado paso a paso

**Problema:** Cliente envia "Hola servidor!" y servidor responde con echo.

**Servidor:**
1. `socket()` → `bind(("localhost", 9999))` → `listen(1)`
2. `accept()` → espera cliente
3. `recv(1024)` → recibe datos
4. `send(datos)` → devuelve los mismos datos (echo)
5. `close()`

**Cliente:**
1. `socket()` → `connect(("localhost", 9999))`
2. `send(b"Hola servidor!")` → envia datos
3. `recv(1024)` → recibe respuesta
4. `close()`

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Crear socket cliente TCP | 🟢 |
| 2  | Enviar mensaje y recibir respuesta | 🟡 |
| 3  | Servidor echo simple (con hilo) | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 7 1
python scripts/runner.py 5 7 2
python scripts/runner.py 5 7 3
python scripts/runner.py 5 7 1 -p 1
python scripts/runner.py 5 7 3 -s
```
