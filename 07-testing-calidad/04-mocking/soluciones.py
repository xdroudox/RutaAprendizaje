"""
SOLUCIONES - Mocking
Ejecuta desde raiz: python scripts/runner.py 7 4 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Solucion: mockear funcion externa"""
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
    print("Mock de funcion externa funciona correctamente.")
    print("reporte_clima('Madrid') =", resultado)

def obtener_clima(ciudad):
    raise NotImplementedError()

def ejercicio_2():
    """Solucion: verificar argumentos del mock"""
    from unittest.mock import patch
    def notificar_usuario(email, nombre):
        enviar_email(email, 'Bienvenido', f'Hola {nombre}')
    with patch('__main__.enviar_email') as mock_email:
        notificar_usuario('test@test.com', 'Ana')
        mock_email.assert_called_once_with('test@test.com', 'Bienvenido', 'Hola Ana')
    print("Verificacion de argumentos del mock superada.")

def enviar_email(destino, asunto, cuerpo):
    pass

def ejercicio_3():
    """Solucion: side_effect para errores"""
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
    print("Side effect para simular errores funciona correctamente.")

def conectar_base_datos():
    raise NotImplementedError()

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
