"""
EJERCICIOS - JSON y XML
Ejecuta desde raiz: python scripts/runner.py 5 3 [ejercicio]
"""
import sys
import json
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Convertir diccionario a JSON con json.dumps()"""
    usuario = {
        "id": 1,
        "nombre": "Ana",
        "email": "ana@ejemplo.com",
        "activo": True,
        "tags": ["admin", "user"]
    }
    # Convierte el dict a string JSON con indentacion
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_2():
    """Parsear string JSON a diccionario con json.loads()"""
    json_str = '{"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com", "activo": true}'
    # Convierte el string JSON a dict e imprime el nombre y email
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_3():
    """Leer JSON de archivo y extraer datos"""
    import os
    ruta = os.path.join(os.path.dirname(__file__), "datos.json")
    # Lee el archivo JSON y muestra todos los usuarios
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
