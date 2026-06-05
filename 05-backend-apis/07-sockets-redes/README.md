# Sockets y Redes

Un socket es un punto final de comunicacion entre dos programas a traves de una red. TCP/IP es el protocolo mas usado.

## Conceptos clave
- **Socket:** canal de comunicacion bidireccional
- **Cliente:** inicia la conexion
- **Servidor:** escucha y acepta conexiones
- **Puerto:** identifica el servicio (ej: 80 HTTP, 443 HTTPS)

## Modelo Cliente-Servidor
1. Servidor crea socket, lo asigna a IP:puerto y escucha
2. Cliente crea socket y se conecta al servidor
3. Ambos intercambian datos
4. Cierran la conexion

## Ejercicios

1. **Socket cliente TCP** - Crear un socket que se conecte a un host y puerto.
   **Ejecuta:** `python scripts/runner.py 5 7 1`

2. **Enviar y recibir datos** - Conectarse a localhost, enviar mensaje y recibir respuesta.
   **Ejecuta:** `python scripts/runner.py 5 7 2`

3. **Servidor echo simple** - Crear un servidor que devuelva lo que recibe.
   **Ejecuta:** `python scripts/runner.py 5 7 3`
