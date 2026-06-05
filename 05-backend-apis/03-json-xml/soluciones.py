import sys, json, os

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Serializar un diccionario a JSON")
    print("=" * 50)
    producto = {
        "id": 101,
        "nombre": "Teclado mecanico",
        "precio": 89.99,
        "disponible": True,
        "colores": ["negro", "blanco", "rojo"]
    }
    json_str = json.dumps(producto, indent=2)
    print("JSON generado:")
    print(json_str)

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Deserializar JSON a diccionario")
    print("=" * 50)
    json_str = '{"usuarios": [{"id": 1, "nombre": "Ana"}, {"id": 2, "nombre": "Luis"}, {"id": 3, "nombre": "Maria"}]}'
    datos = json.loads(json_str)
    print("Diccionario completo:")
    print(datos)
    print()
    print("Nombre del usuario con id=2:", datos["usuarios"][1]["nombre"])

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Guardar y leer JSON de archivo")
    print("=" * 50)
    tareas = [
        {"id": 1, "titulo": "Estudiar Python", "completada": False},
        {"id": 2, "titulo": "Hacer ejercicios", "completada": True},
        {"id": 3, "titulo": "Leer documentacion", "completada": False}
    ]
    archivo = "tareas.json"
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=2)
    print("JSON guardado en", archivo)
    print()
    with open(archivo, "r", encoding="utf-8") as f:
        datos_leidos = json.load(f)
    print("Datos leidos del archivo:")
    for t in datos_leidos:
        estado = "Completada" if t["completada"] else "Pendiente"
        print(f"  [{t['id']}] {t['titulo']} - {estado}")
    os.remove(archivo)

def menu():
    print("SOLUCIONES - JSON Y XML")
    print("1 - Serializar un diccionario a JSON")
    print("2 - Deserializar JSON a diccionario")
    print("3 - Guardar y leer JSON de archivo")

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
