"""
EJERCICIOS - NoSQL Introduccion
Ejecuta desde raiz: python scripts/runner.py 4 7 [ejercicio]

Niveles:
  🟢 Ej 1: Modelar documento MongoDB (dict anidado)
  🟡 Ej 2: Convertir esquema SQL normalizado a NoSQL
  🔴 Ej 3: Clasificar casos de uso SQL vs NoSQL

Pistas: python scripts/runner.py 4 7 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Modelar documento MongoDB (dict anidado)"""
    print(">> 🟢 EJERCICIO 1: Modelar documento MongoDB para usuario")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1: Estructura basica del documento:")
        print("  usuario = {")
        print('      "nombre": "Ana",')
        print('      "email": "ana@email.com",')
        print("      ...")
        print("  }")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Incluye datos anidados:")
        print('  "direccion": {')
        print('      "calle": "Calle Mayor 10",')
        print('      "ciudad": "Madrid",')
        print('      "pais": "Espana"')
        print("  },")
        print('  "intereses": ["lectura", "viajes", "fotografia"]')
        return
    elif pista == 3:
        print("\n💡 Pista 3: Para imprimir con formato:")
        print("  import json")
        print('  print(json.dumps(usuario, indent=2, ensure_ascii=False))')
        return

    print("Crea un diccionario que represente un documento MongoDB")
    print("para un usuario. Debe incluir:")
    print("  - nombre (string)")
    print("  - email (string)")
    print("  - direccion (dict anidado: calle, ciudad, pais)")
    print("  - intereses (lista de strings)")
    print()
    print("Luego imprimelo con json.dumps(indent=2)")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Convertir esquema SQL normalizado a NoSQL"""
    print(">> 🟡 EJERCICIO 2: SQL normalizado → Documento NoSQL")
    print("-" * 50)

    datos_sql = {
        "clientes": [
            {"id": 1, "nombre": "Ana", "ciudad": "Madrid"},
            {"id": 2, "nombre": "Juan", "ciudad": "Barcelona"}
        ],
        "pedidos": [
            {"id": 1, "cliente_id": 1, "producto": "Laptop", "total": 999.99},
            {"id": 2, "cliente_id": 1, "producto": "Mouse", "total": 25.50},
            {"id": 3, "cliente_id": 2, "producto": "Teclado", "total": 45.00}
        ]
    }

    print("=== Esquema SQL normalizado ===")
    print("clientes:")
    for c in datos_sql["clientes"]:
        print(f"  {c}")
    print("pedidos:")
    for p in datos_sql["pedidos"]:
        print(f"  {p}")

    if pista == 1:
        print("\n💡 Pista 1: Cada cliente debe tener un array 'pedidos':")
        print("  documento = [")
        print("      {")
        print('          "cliente": {"nombre": "...", "ciudad": "..."},')
        print('          "pedidos": [')
        print('              {"producto": "...", "total": ... }')
        print("          ]")
        print("      },")
        print("      ...")
        print("  ]")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  Recorre los clientes, filtra sus pedidos por cliente_id")
        print("  y anidalos dentro de cada cliente:")
        print("  for c in datos_sql['clientes']:")
        print("      pedidos_cliente = [p for p in datos_sql['pedidos']")
        print("                        if p['cliente_id'] == c['id']]")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  Ana (Madrid): Laptop $999.99, Mouse $25.50")
        print("  Juan (Barcelona): Teclado $45.00")
        print("  En NoSQL, los datos relacionados se ANIDAN en lugar de usar JOINs")
        print("  Esto evita la necesidad de JOINs en lecturas frecuentes")
        return

    print()
    print("Convierte este esquema SQL normalizado a documentos NoSQL")
    print("donde cada cliente incluya sus pedidos como array anidado.")
    print()
    print("Crea una lista de documentos como:")
    print("  [")
    print("    { 'cliente': { 'nombre': 'Ana', 'ciudad': 'Madrid' },")
    print("      'pedidos': [ { 'producto': 'Laptop', 'total': 999.99 }, ... ] },")
    print("    ...")
    print("  ]")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Clasificar casos de uso SQL vs NoSQL"""
    print(">> 🔴 EJERCICIO 3: Clasificar casos de uso SQL vs NoSQL")
    print("-" * 50)

    casos = [
        "Sistema bancario con transferencias entre cuentas",
        "Catalogo de productos con estructura variable",
        "Red social con posts, likes y comentarios",
        "Sistema de facturacion con totales exactos",
        "Blog con articulos y multiples autores",
        "Analitica en tiempo real de eventos de usuario",
        "Sistema de reservas de vuelos con integridad estricta",
        "Almacenamiento de sesiones de usuario con TTL"
    ]

    print("Clasifica cada caso como SQL o NoSQL y explica por que:")
    print()
    for i, caso in enumerate(casos, 1):
        print(f"  {i}. {caso}")

    if pista == 1:
        print("\n💡 Pista 1: Piensa en estas preguntas para cada caso:")
        print("  - ¿Necesita transacciones ACID?           → SQL")
        print("  - ¿La estructura de datos es fija?         → SQL")
        print("  - ¿Necesita alta escalabilidad?             → NoSQL")
        print("  - ¿La estructura puede variar?             → NoSQL")
        print("  - ¿Requiere joins o relaciones complejas?   → SQL")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Clasificacion esperada:")
        print("  SQL:   1, 4, 5, 7  (ACID, relaciones, consistencia fuerte)")
        print("  NoSQL: 2, 3, 6, 8  (estructura variable, escalabilidad, TTL)")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Explicaciones:")
        print("  1. SQL   → ACID necesario para transferencias exactas")
        print("  2. NoSQL → Cada producto puede tener atributos distintos")
        print("  3. NoSQL → Datos semi-estructurados, alta escalabilidad")
        print("  4. SQL   → Totales exactos requieren consistencia fuerte")
        print("  5. SQL   → Relaciones muchos-a-muchos (articulo-autor)")
        print("  6. NoSQL → Alto volumen de escritura, esquema simple")
        print("  7. SQL   → Consistencia estricta, sin sobregiro")
        print("  8. NoSQL → TTL nativo en MongoDB, datos temporales")
        return

    print("\nPara cada caso, asigna 'SQL' o 'NoSQL' con una breve explicacion.")
    print("Usa un diccionario con tu analisis.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            pista = 0
            if "-p" in sys.argv:
                idx = sys.argv.index("-p")
                if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                    pista = int(sys.argv[idx + 1])
            ejercicios[num](pista)
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__ or ""
            print(f"  {i}. {doc}")
