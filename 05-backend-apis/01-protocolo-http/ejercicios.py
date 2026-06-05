import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Estructura de una URL")
    print("=" * 50)
    print()
    url = "https://api.ejemplo.com:8080/usuarios?rol=admin&edad=25#perfil"
    print("URL:", url)
    print()
    print("TAREA: Identifica las partes de la URL asignando cada fragmento")
    print("a su componente: esquema, dominio, puerto, ruta, query, fragmento.")
    print()
    print("Escribe tu codigo para extraer cada parte usando slicing o split.")
    print()
    print("PISTA: Usa .split() con '://', ':', '/', '?', '#' para separar.")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Construir una peticion GET")
    print("=" * 50)
    print()
    print("TAREA: Usando http.client, realiza una peticion GET a")
    print("jsonplaceholder.typicode.com para obtener el post con id=3.")
    print()
    print("Debes imprimir el codigo de estado y el cuerpo de la respuesta.")
    print()
    print("PISTA: HTTPSConnection, conn.request('GET', '/posts/3'), getresponse()")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Headers de request")
    print("=" * 50)
    print()
    print("TAREA: Realiza una peticion GET a https://httpbin.org/headers")
    print("enviando un header personalizado 'X-Mi-Header: HolaMundo'.")
    print()
    print("Imprime la respuesta completa para ver como httpbin refleja")
    print("los headers enviados.")
    print()
    print("PISTA: En el request, pasa un dict como headers: {'X-Mi-Header': 'HolaMundo'}")

pistas = {
    "1": "esquema = url.split('://')[0]; resto = url.split('://')[1]; dominio_puerto = resto.split('/')[0]; dominio = dominio_puerto.split(':')[0]; puerto = dominio_puerto.split(':')[1] if ':' in dominio_puerto else ''; ...",
    "2": "conn = http.client.HTTPSConnection('jsonplaceholder.typicode.com'); conn.request('GET', '/posts/3'); resp = conn.getresponse(); print(resp.status); print(resp.read().decode()); conn.close()",
    "3": "conn = http.client.HTTPSConnection('httpbin.org'); conn.request('GET', '/headers', headers={'X-Mi-Header': 'HolaMundo'}); resp = conn.getresponse(); print(resp.read().decode()); conn.close()"
}

def menu():
    print("=" * 50)
    print("PROTOCOLO HTTP - EJERCICIOS")
    print("=" * 50)
    print("1 - Estructura de una URL")
    print("2 - Construir una peticion GET")
    print("3 - Headers de request")
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
