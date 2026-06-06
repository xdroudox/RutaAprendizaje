"""
SOLUCIONES - NoSQL Introduccion
Ejecuta: python scripts/runner.py 4 7 [ejercicio] -s
"""

import sys
import json

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Modelar documento MongoDB (dict anidado)")
    print("=" * 50)

    print("--- CODIGO ---")
    print("usuario = {")
    print('    "nombre": "Ana Garcia",')
    print('    "email": "ana@email.com",')
    print('    "direccion": {')
    print('        "calle": "Calle Mayor 10",')
    print('        "ciudad": "Madrid",')
    print('        "pais": "Espana"')
    print("    },")
    print('    "intereses": ["lectura", "viajes", "fotografia"]')
    print("}")
    print('print(json.dumps(usuario, indent=2, ensure_ascii=False))')
    print()

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
    print("--- RESULTADO ---")
    print(json.dumps(usuario, indent=2, ensure_ascii=False))

    print()
    print("--- EXPLICACION ---")
    print("""
Este documento NoSQL equivale a multiples tablas SQL:
  - Una tabla 'usuarios' con nombre y email
  - Una tabla 'direcciones' con FK a usuarios
  - Una tabla 'intereses' con FK a usuarios

Ventaja: Para obtener el perfil completo del usuario solo
necesitamos UNA consulta (lectura del documento), no 3 JOINs.

Los documentos anidados son ideales cuando:
  - Los datos se acceden JUNTOS (perfil de usuario)
  - La estructura es jerarquica (1 usuario → N direcciones)
  - No necesitas consultar los sub-datos por separado
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Convertir SQL normalizado a NoSQL")
    print("=" * 50)

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

    documentos = []
    for c in datos_sql["clientes"]:
        pedidos_cliente = [
            {"producto": p["producto"], "total": p["total"]}
            for p in datos_sql["pedidos"]
            if p["cliente_id"] == c["id"]
        ]
        documentos.append({
            "cliente": {"nombre": c["nombre"], "ciudad": c["ciudad"]},
            "pedidos": pedidos_cliente
        })

    print("--- CODIGO ---")
    print("documentos = []")
    print("for c in datos_sql['clientes']:")
    print("    pedidos_cliente = [")
    print("        {'producto': p['producto'], 'total': p['total']}")
    print("        for p in datos_sql['pedidos']")
    print("        if p['cliente_id'] == c['id']")
    print("    ]")
    print("    documentos.append({")
    print("        'cliente': {'nombre': c['nombre'], 'ciudad': c['ciudad']},")
    print("        'pedidos': pedidos_cliente")
    print("    })")
    print()

    print("--- RESULTADO ---")
    print(json.dumps(documentos, indent=2, ensure_ascii=False))

    print()
    print("--- EXPLICACION ---")
    print("""
SQL normalizado (tablas separadas con FK):
  clientes: id, nombre, ciudad
  pedidos:  id, cliente_id, producto, total
  Consulta: SELECT * FROM clientes JOIN pedidos ON ...

NoSQL desnormalizado (datos anidados en un solo documento):
  Un documento por cliente que INCLUYE sus pedidos

Trade-offs:
  SQL:
    ✅ Sin duplicacion de datos
    ✅ Facil de actualizar (un solo lugar)
    ❌ JOIN necesario para leer datos relacionados

  NoSQL:
    ✅ Lectura rapida (1 consulta)
    ✅ Datos relacionados almacenados juntos
    ❌ Duplicacion si el cliente aparece en varios documentos
    ❌ Actualizacion mas compleja (multiples documentos)
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Clasificar casos de uso SQL vs NoSQL")
    print("=" * 50)

    print("--- ANALISIS ---")
    casos = [
        (1, "Sistema bancario con transferencias entre cuentas",
         "SQL",   "Requiere ACID, consistencia fuerte, transacciones atomicas"),
        (2, "Catalogo de productos con estructura variable",
         "NoSQL", "Cada producto puede tener atributos distintos (schema flexible)"),
        (3, "Red social con posts, likes y comentarios",
         "NoSQL", "Datos semi-estructurados, alta escalabilidad horizontal"),
        (4, "Sistema de facturacion con totales exactos",
         "SQL",   "Requiere consistencia fuerte, calculos exactos, integridad"),
        (5, "Blog con articulos y multiples autores",
         "SQL",   "Relaciones muchos-a-muchos (autor-articulo), integridad referencial"),
        (6, "Analitica en tiempo real de eventos de usuario",
         "NoSQL", "Alto volumen de escritura, esquema simple, baja latencia"),
        (7, "Sistema de reservas de vuelos con integridad estricta",
         "SQL",   "Consistencia estricta, sin sobregiro de reservas"),
        (8, "Almacenamiento de sesiones de usuario con TTL",
         "NoSQL", "TTL nativo (MongoDB), datos temporales, esquema simple")
    ]

    for num, desc, tipo, razon in casos:
        print(f"  {num}. [{tipo:6s}] {desc}")
        print(f"       {razon}")
        print()

    print("--- CONCLUSION ---")
    print("""
Regla practica: Preguntate 3 cosas:

1. ¿Necesito ACID?
   Si → SQL (bancos, facturacion, reservas)
   No → Considera NoSQL

2. ¿La estructura de datos es fija y predecible?
   Si → SQL (esquema definido de antemano)
   No → NoSQL (schema flexible)

3. ¿Voy a escalar a millones de usuarios?
   Si → Considera NoSQL (escalabilidad horizontal nativa)
   No → SQL es suficiente y mas maduro

La mayoria de aplicaciones reales usan AMBOS:
  - SQL para datos criticos (usuarios, pagos, facturas)
  - NoSQL para datos de alta carga (logs, sesiones, analytics)
  Esto se llama "persistencia poliglota".
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
