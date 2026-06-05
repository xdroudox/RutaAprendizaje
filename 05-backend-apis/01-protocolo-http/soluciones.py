import sys
import http.client

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Estructura de una URL")
    print("=" * 50)
    url = "https://api.ejemplo.com:8080/usuarios?rol=admin&edad=25#perfil"
    print("URL:", url)
    print()

    esquema = url.split("://")[0]
    resto = url.split("://")[1]
    if "#" in resto:
        dominio_ruta_query, fragmento = resto.split("#")
    else:
        dominio_ruta_query = resto
        fragmento = ""
    if "?" in dominio_ruta_query:
        dominio_ruta, query = dominio_ruta_query.split("?")
    else:
        dominio_ruta = dominio_ruta_query
        query = ""
    if ":" in dominio_ruta.split("/")[0]:
        dominio, puerto = dominio_ruta.split("/")[0].split(":")
    else:
        dominio = dominio_ruta.split("/")[0]
        puerto = ""
    ruta = "/" + "/".join(dominio_ruta.split("/")[1:]) if "/" in dominio_ruta else ""

    print(f"Esquema:  {esquema}")
    print(f"Dominio:  {dominio}")
    print(f"Puerto:   {puerto if puerto else '(default)'}")
    print(f"Ruta:     {ruta if ruta else '/'}")
    print(f"Query:    {query if query else '(ninguna)'}")
    print(f"Fragmento: {fragmento if fragmento else '(ninguno)'}")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Construir una peticion GET")
    print("=" * 50)
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("GET", "/posts/3")
    resp = conn.getresponse()
    print("Codigo de estado:", resp.status, resp.reason)
    print()
    print("Cuerpo de la respuesta:")
    print(resp.read().decode())
    conn.close()

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Headers de request")
    print("=" * 50)
    conn = http.client.HTTPSConnection("httpbin.org")
    conn.request("GET", "/headers", headers={"X-Mi-Header": "HolaMundo"})
    resp = conn.getresponse()
    print("Codigo:", resp.status)
    print()
    print("Respuesta:")
    print(resp.read().decode())
    conn.close()

def menu():
    print("SOLUCIONES - PROTOCOLO HTTP")
    print("1 - Estructura de una URL")
    print("2 - Construir una peticion GET")
    print("3 - Headers de request")

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
