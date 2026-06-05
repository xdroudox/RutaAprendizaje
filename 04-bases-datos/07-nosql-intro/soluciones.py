"""
SOLUCIONES - NoSQL Intro
Ejecuta desde raiz: python scripts/runner.py 4 7 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Modela un documento MongoDB para un usuario usando un dict anidado"""
    import json
    print(">>> Documento MongoDB para usuario:")
    usuario = {
        "nombre": "Ana Garcia",
        "email": "ana@email.com",
        "direccion": {
            "calle": "Calle Mayor 10",
            "ciudad": "Madrid",
            "pais": "Espana"
        },
        "intereses": ["lectura", "viajes", "fotografia"]
    }
    print(json.dumps(usuario, indent=2, ensure_ascii=False))

def ejercicio_2():
    """Convierte un esquema SQL normalizado a un documento NoSQL (dict)"""
    import json
    print(">>> Documento NoSQL con pedidos anidados:")
    documentos = [
        {
            "cliente": {"nombre": "Ana", "ciudad": "Madrid"},
            "pedidos": [
                {"producto": "Laptop", "total": 999.99},
                {"producto": "Mouse", "total": 25.50}
            ]
        },
        {
            "cliente": {"nombre": "Juan", "ciudad": "Barcelona"},
            "pedidos": [
                {"producto": "Teclado", "total": 45.00}
            ]
        }
    ]
    print(json.dumps(documentos, indent=2, ensure_ascii=False))

def ejercicio_3():
    """Compara casos de uso: cuando usar SQL vs NoSQL"""
    print(">>> Analisis de casos:")
    casos = [
        (1, "SQL",    "Requiere ACID, integridad referencial y consistencia fuerte"),
        (2, "NoSQL",  "Estructura de producto variable, esquema flexible"),
        (3, "NoSQL",  "Datos semi-estructurados, alta escalabilidad, grafos de relaciones"),
        (4, "SQL",    "Requiere transacciones atomicas, totales exactos"),
        (5, "SQL",    "Relaciones muchos-a-muchos, integridad referencial"),
        (6, "NoSQL",  "Alto volumen de escritura, esquema simple, baja latencia"),
        (7, "SQL",    "Consistencia estricta, reservas sin sobregiro"),
        (8, "NoSQL",  "TTL nativo, datos temporales, esquema simple")
    ]
    for num, tipo, razon in casos:
        print(f"  {num}. {tipo:6s} - {razon}")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
