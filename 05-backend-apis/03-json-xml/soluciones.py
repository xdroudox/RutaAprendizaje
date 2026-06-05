"""
SOLUCIONES - JSON y XML
Ejecuta desde raiz: python scripts/runner.py 5 3 1 -s
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
    json_str = json.dumps(usuario, indent=2, ensure_ascii=False)
    print("JSON resultante:")
    print(json_str)

def ejercicio_2():
    """Parsear string JSON a diccionario con json.loads()"""
    json_str = '{"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com", "activo": true}'
    datos = json.loads(json_str)
    print(f"Nombre: {datos['nombre']}")
    print(f"Email: {datos['email']}")
    print(f"Activo: {datos['activo']}")

def ejercicio_3():
    """Leer JSON de archivo y extraer datos"""
    import os
    ruta = os.path.join(os.path.dirname(__file__), "datos.json")
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        print("Contenido del archivo JSON:")
        print(json.dumps(datos, indent=2, ensure_ascii=False))
        if isinstance(datos, list):
            print(f"\nTotal de registros: {len(datos)}")
    else:
        print(f"Archivo no encontrado: {ruta}")
        print("Crea un archivo datos.json en este directorio para probar.")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> SOLUCION {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("SOLUCIONES:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
