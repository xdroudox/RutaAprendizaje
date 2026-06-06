"""
SOLUCIONES - Mocking
Ejecuta desde raiz: python scripts/runner.py 7 4 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Mockear funcion externa con unittest.mock"""
    from unittest.mock import Mock
    def reporte_clima(ciudad):
        temp = obtener_clima(ciudad)
        return f'Temperatura en {ciudad}: {temp}°C'
    mock_clima = Mock()
    mock_clima.side_effect = lambda c: 25 if c == 'Madrid' else 30
    import __main__
    __main__.obtener_clima = mock_clima
    resultado = reporte_clima('Madrid')
    assert resultado == 'Temperatura en Madrid: 25°C'
    print(">> SOLUCION 1: Mockear funcion externa con unittest.mock")
    print("-" * 40)
    print("Mock de funcion externa funciona correctamente.")
    print("reporte_clima('Madrid') =", resultado)

def obtener_clima(ciudad):
    raise NotImplementedError()

def solucion_2():
    """Verificar que mock fue llamado con argumentos correctos"""
    from unittest.mock import patch
    def notificar_usuario(email, nombre):
        enviar_email(email, 'Bienvenido', f'Hola {nombre}')
    with patch('__main__.enviar_email') as mock_email:
        notificar_usuario('test@test.com', 'Ana')
        mock_email.assert_called_once_with('test@test.com', 'Bienvenido', 'Hola Ana')
    print(">> SOLUCION 2: Verificar que mock fue llamado con argumentos correctos")
    print("-" * 40)
    print("Verificacion de argumentos del mock superada.")

def enviar_email(destino, asunto, cuerpo):
    pass

def solucion_3():
    """Mock con side_effect para simular errores"""
    from unittest.mock import patch
    def obtener_usuario(id_usuario):
        conn = conectar_base_datos()
        return conn.query(f'SELECT * FROM usuarios WHERE id = {id_usuario}')
    with patch('__main__.conectar_base_datos') as mock_conn:
        mock_conn.side_effect = ConnectionError('Base de datos no disponible')
        try:
            obtener_usuario(1)
            assert False, "Debio lanzar ConnectionError"
        except ConnectionError as e:
            assert str(e) == 'Base de datos no disponible'
    print(">> SOLUCION 3: Mock con side_effect para simular errores")
    print("-" * 40)
    print("Side effect para simular errores funciona correctamente.")

def conectar_base_datos():
    raise NotImplementedError()

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
