"""
EJERCICIOS - Mocking
Ejecuta desde raiz: python scripts/runner.py 7 4 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Mockear funcion externa con unittest.mock"""
    print("Dada una funcion que llama a una API externa:")
    print()
    print("def obtener_clima(ciudad):")
    print("    # Llama a API externa (no implementada)")
    print("    raise NotImplementedError()")
    print()
    print("def reporte_clima(ciudad):")
    print("    temp = obtener_clima(ciudad)")
    print("    return f'Temperatura en {ciudad}: {temp}°C'")
    print()
    print("Usa unittest.mock.Mock para simular obtener_clima")
    print("y probar reporte_clima sin llamar a la API real.")
    print()
    print("from unittest.mock import Mock")
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")

def ejercicio_2():
    """Verificar que mock fue llamado con argumentos correctos"""
    print("Usa patch para mockear una funcion y verifica que")
    print("fue llamada con los argumentos esperados.")
    print()
    print("def enviar_email(destino, asunto, cuerpo):")
    print("    # Envia email real")
    print("    pass")
    print()
    print("def notificar_usuario(email, nombre):")
    print("    enviar_email(email, 'Bienvenido', f'Hola {nombre}')")
    print()
    print("from unittest.mock import patch")
    print("# ==== ESCRIBE TU PRUEBA AQUI ====")
    print("# Verifica que enviar_email fue llamada con los argumentos correctos")

def ejercicio_3():
    """Mock con side_effect para simular errores"""
    print("Usa side_effect en un mock para simular diferentes")
    print("comportamientos en cada llamada o lanzar excepciones.")
    print()
    print("def conectar_base_datos():")
    print("    # Conexion real a BD")
    print("    pass")
    print()
    print("def obtener_usuario(id_usuario):")
    print("    conn = conectar_base_datos()")
    print("    return conn.query(f'SELECT * FROM usuarios WHERE id = {id_usuario}')")
    print()
    print("from unittest.mock import patch")
    print("# ==== ESCRIBE TU PRUEBA AQUI ====")
    print("# side_effect para simular error de conexion")

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
