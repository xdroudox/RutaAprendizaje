"""
EJERCICIOS - API Testing y Documentacion
Ejecuta desde raiz: python scripts/runner.py 5 9 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Construir request GET con http.client"""
    host = "jsonplaceholder.typicode.com"
    ruta = "/posts/1"
    # Crea una conexion HTTPS y haz GET a la ruta
    # Imprime el status code y el body
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_2():
    """Validar status code y body de una response"""
    # Usando la respuesta del ej1, valida que:
    # - status code sea 200
    # - el body tenga los campos "id", "title" y "body"
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_3():
    """Escribir documentacion OpenAPI simple (dict)"""
    # Crea un diccionario con la estructura OpenAPI para:
    # GET /api/usuarios -> lista de usuarios
    # POST /api/usuarios -> crear usuario
    # Incluye: openapi version, info, paths, schemas basicos
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
