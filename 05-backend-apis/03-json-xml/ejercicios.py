import sys, json

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Serializar un diccionario a JSON")
    print("=" * 50)
    producto = {
        "id": 101,
        "nombre": "Teclado mecanico",
        "precio": 89.99,
        "disponible": True,
        "colores": ["negro", "blanco", "rojo"]
    }
    print("Diccionario original:")
    print(producto)
    print()
    print("TAREA: Usa json.dumps() para convertir el diccionario a")
    print("una cadena JSON con indentacion de 2 espacios.")
    print()
    print("PISTA: json.dumps(producto, indent=2)")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Deserializar JSON a diccionario")
    print("=" * 50)
    json_str = '{"usuarios": [{"id": 1, "nombre": "Ana"}, {"id": 2, "nombre": "Luis"}, {"id": 3, "nombre": "Maria"}]}'
    print("Cadena JSON:")
    print(json_str)
    print()
    print("TAREA: Usa json.loads() para convertir la cadena a un")
    print("diccionario Python. Luego imprime el nombre del usuario con id=2.")
    print()
    print("PISTA: datos = json.loads(json_str); datos['usuarios'][1]['nombre']")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Guardar y leer JSON de archivo")
    print("=" * 50)
    print()
    print("TAREA: Crea una lista de tareas (tareas) donde cada tarea")
    print("tiene: id, titulo, completada (bool). Guardala como JSON")
    print("en un archivo 'tareas.json' y luego leela de vuelta.")
    print()
    print("Agrega al menos 3 tareas, una de ellas completada.")
    print()
    print("PISTA: json.dump(lista, archivo) para escribir.")
    print("       json.load(archivo) para leer.")

pistas = {
    "1": "json.dumps(producto, indent=2)",
    "2": "datos = json.loads(json_str); print(datos['usuarios'][1]['nombre'])",
    "3": "tareas = [{'id': 1, 'titulo': 'Estudiar Python', 'completada': False}, {'id': 2, 'titulo': 'Hacer ejercicios', 'completada': True}, {'id': 3, 'titulo': 'Leer documentacion', 'completada': False}]; with open('tareas.json', 'w') as f: json.dump(tareas, f, indent=2); with open('tareas.json') as f: datos = json.load(f); print(datos)"
}

def menu():
    print("=" * 50)
    print("JSON Y XML - EJERCICIOS")
    print("=" * 50)
    print("1 - Serializar un diccionario a JSON")
    print("2 - Deserializar JSON a diccionario")
    print("3 - Guardar y leer JSON de archivo")
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
