"""
EJERCICIOS - Mocking
Ejecuta desde raiz: python scripts/runner.py 7 4 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Mockear funcion externa con unittest.mock"""
    print(">> EJERCICIO 1: Mockear funcion externa con unittest.mock")
    print("-" * 40)
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
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  from unittest.mock import Mock")
        print("  Crea un Mock: mock_clima = Mock()")
        print("  Asigna side_effect: mock_clima.side_effect = lambda c: 25")
        print("  Reemplaza la funcion: __main__.obtener_clima = mock_clima")
        print("  Llama a reporte_clima() y verifica el resultado.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  from unittest.mock import Mock")
        print("  mock_clima = Mock()")
        print("  mock_clima.side_effect = lambda c: 25 if c == 'Madrid' else 30")
        print("  import __main__")
        print("  __main__.obtener_clima = mock_clima")
        print("  resultado = reporte_clima('Madrid')")
        print("  assert resultado == 'Temperatura en Madrid: 25°C'")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  from unittest.mock import Mock")
        print("  def reporte_clima(ciudad):")
        print("      temp = obtener_clima(ciudad)")
        print("      return f'Temperatura en {ciudad}: {temp}°C'")
        print("  mock_clima = Mock()")
        print("  mock_clima.side_effect = lambda c: 25 if c == 'Madrid' else 30")
        print("  import __main__")
        print("  __main__.obtener_clima = mock_clima")
        print("  resultado = reporte_clima('Madrid')")
        print("  assert resultado == 'Temperatura en Madrid: 25°C'")
        print("  print('Mock de funcion externa funciona correctamente')")

def ejercicio_2(pista=0):
    """Verificar que mock fue llamado con argumentos correctos"""
    print(">> EJERCICIO 2: Verificar que mock fue llamado con argumentos correctos")
    print("-" * 40)
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
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Usa with patch('__main__.enviar_email') as mock_email:")
        print("  Dentro del bloque, llama a notificar_usuario()")
        print("  Luego verifica: mock_email.assert_called_once_with(...)")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  from unittest.mock import patch")
        print("  with patch('__main__.enviar_email') as mock_email:")
        print("      notificar_usuario('test@test.com', 'Ana')")
        print("      mock_email.assert_called_once_with(")
        print("          'test@test.com', 'Bienvenido', 'Hola Ana'")
        print("      )")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  from unittest.mock import patch")
        print("  def notificar_usuario(email, nombre):")
        print("      enviar_email(email, 'Bienvenido', f'Hola {nombre}')")
        print("  with patch('__main__.enviar_email') as mock_email:")
        print("      notificar_usuario('test@test.com', 'Ana')")
        print("      mock_email.assert_called_once_with(")
        print("          'test@test.com', 'Bienvenido', 'Hola Ana'")
        print("      )")
        print("  print('Verificacion de argumentos superada')")

def ejercicio_3(pista=0):
    """Mock con side_effect para simular errores"""
    print(">> EJERCICIO 3: Mock con side_effect para simular errores")
    print("-" * 40)
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
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Usa patch('__main__.conectar_base_datos') as mock_conn")
        print("  Asigna mock_conn.side_effect = ConnectionError('mensaje')")
        print("  Llama a obtener_usuario() dentro de try/except")
        print("  Verifica que se lance ConnectionError")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  from unittest.mock import patch")
        print("  with patch('__main__.conectar_base_datos') as mock_conn:")
        print("      mock_conn.side_effect = ConnectionError('Base de datos no disponible')")
        print("      try:")
        print("          obtener_usuario(1)")
        print("          assert False, 'Debio lanzar ConnectionError'")
        print("      except ConnectionError as e:")
        print("          assert str(e) == 'Base de datos no disponible'")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  from unittest.mock import patch")
        print("  with patch('__main__.conectar_base_datos') as mock_conn:")
        print("      mock_conn.side_effect = ConnectionError('Base de datos no disponible')")
        print("      try:")
        print("          obtener_usuario(1)")
        print("          assert False, 'Debio lanzar ConnectionError'")
        print("      except ConnectionError as e:")
        print("          assert str(e) == 'Base de datos no disponible'")
        print("  print('Side effect para simular errores funciona')")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    pista_level = 0
    if "-p" in sys.argv:
        idx = sys.argv.index("-p")
        if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
            pista_level = int(sys.argv[idx + 1])
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num](pista=pista_level)
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
