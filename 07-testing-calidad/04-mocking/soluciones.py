"""
SOLUCIONES - Mocking
Ejecuta: python soluciones.py [numero]

Uso:
  python soluciones.py    -> Menu
  python soluciones.py 1  -> Solucion del ejercicio 1
"""

import sys
from unittest.mock import Mock, patch

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


class ServicioClima:
    def obtener_temperatura(self, ciudad):
        raise NotImplementedError("Llama a API real")


class ReporteClima:
    def __init__(self, servicio):
        self.servicio = servicio

    def generar_reporte(self, ciudad):
        temp = self.servicio.obtener_temperatura(ciudad)
        if temp > 30:
            return f"Hace calor en {ciudad}: {temp}°C"
        elif temp < 10:
            return f"Hace frio en {ciudad}: {temp}°C"
        else:
            return f"Clima templado en {ciudad}: {temp}°C"


def validar_tarjeta(tarjeta):
    raise NotImplementedError


def cobrar(tarjeta, monto):
    raise NotImplementedError


def procesar_pago(tarjeta, monto):
    if not validar_tarjeta(tarjeta):
        raise ValueError("Tarjeta invalida")
    if monto > 1000:
        raise ValueError("Monto excede el limite")
    cobrar(tarjeta, monto)
    return "Pago exitoso"


def obtener_datos_usuario(id_usuario):
    import requests
    return requests.get(f"https://api.ejemplo.com/usuarios/{id_usuario}").json()


def mostrar_nombre_usuario(id_usuario):
    datos = obtener_datos_usuario(id_usuario)
    return f"Usuario: {datos['nombre']}"


def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Mock de API externa")
    print("=" * 50)
    print()
    print("```python")
    print("from unittest.mock import Mock")
    print()
    print("def test_reporte_clima_con_mock():")
    print("    mock_servicio = Mock()")
    print("    mock_servicio.obtener_temperatura.return_value = 35")
    print()
    print("    reporte = ReporteClima(mock_servicio)")
    print("    resultado = reporte.generar_reporte('Madrid')")
    print()
    print("    assert resultado == 'Hace calor en Madrid: 35°C'")
    print("    mock_servicio.obtener_temperatura.assert_called_once_with('Madrid')")
    print("```")
    print()
    print("Ejecucion del test:")
    print()

    mock_servicio = Mock()
    mock_servicio.obtener_temperatura.return_value = 35
    reporte = ReporteClima(mock_servicio)
    resultado = reporte.generar_reporte("Madrid")
    assert resultado == "Hace calor en Madrid: 35°C"
    mock_servicio.obtener_temperatura.assert_called_once_with("Madrid")
    print("  Resultado:", resultado)
    print("  assert_called_once_with('Madrid') -> OK")
    print()
    print("Ventajas del mock:")
    print("- No necesitas conexion a internet")
    print("- La prueba es rapida y determinista")
    print("- Puedes simular errores facilmente")


def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: patch como context manager")
    print("=" * 50)
    print()
    print("```python")
    print("from unittest.mock import patch")
    print()
    print("def test_mostrar_nombre_usuario():")
    print("    with patch('__main__.obtener_datos_usuario') as mock_obtener:")
    print("        mock_obtener.return_value = {'nombre': 'Ana'}")
    print("        resultado = mostrar_nombre_usuario(1)")
    print("        assert resultado == 'Usuario: Ana'")
    print("        mock_obtener.assert_called_once_with(1)")
    print("```")
    print()
    print("Como decorador:")
    print()
    print("```python")
    print("@patch('__main__.obtener_datos_usuario')")
    print("def test_mostrar_nombre_usuario(mock_obtener):")
    print("    mock_obtener.return_value = {'nombre': 'Ana'}")
    print("    resultado = mostrar_nombre_usuario(1)")
    print("    assert resultado == 'Usuario: Ana'")
    print("```")
    print()
    print("Diferencia entre context manager y decorador:")
    print("  - Context manager: patch solo dura durante el with")
    print("  - Decorador: patch dura toda la funcion")
    print("  - El orden de los decoradores importa (de abajo hacia arriba)")


def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Side effects")
    print("=" * 50)
    print()
    print("```python")
    print("from unittest.mock import patch")
    print("import pytest")
    print()
    print("@patch('__main__.validar_tarjeta')")
    print("@patch('__main__.cobrar')")
    print("def test_pago_exitoso(mock_cobrar, mock_validar):")
    print("    mock_validar.return_value = True")
    print("    resultado = procesar_pago('1234', 500)")
    print("    assert resultado == 'Pago exitoso'")
    print("    mock_cobrar.assert_called_once_with('1234', 500)")
    print()
    print("@patch('__main__.validar_tarjeta')")
    print("def test_tarjeta_invalida(mock_validar):")
    print("    mock_validar.return_value = False")
    print("    with pytest.raises(ValueError, match='Tarjeta invalida'):")
    print("        procesar_pago('0000', 100)")
    print()
    print("@patch('__main__.validar_tarjeta')")
    print("@patch('__main__.cobrar')")
    print("def test_error_conexion(mock_cobrar, mock_validar):")
    print("    mock_validar.return_value = True")
    print("    mock_cobrar.side_effect = ConnectionError('Sin conexion')")
    print("    with pytest.raises(ConnectionError):")
    print("        procesar_pago('1234', 500)")
    print("```")
    print()
    print("Ejemplos de side_effect:")
    print()
    print("  # Retornar diferentes valores en cada llamada")
    print("  mock.side_effect = [10, 20, 30]")
    print("  # Llamar una funcion real")
    print("  mock.side_effect = lambda x: x * 2")
    print("  # Lanzar excepcion")
    print("  mock.side_effect = RuntimeError('fallo')")
    print()
    print("Buenas practicas:")
    print("- Mockea solo lo que no es tuyo (API externas, DB, etc.)")
    print("- No mockees lo que estas probando")
    print("- Prefiere patch sobre Mock directo cuando sea posible")
    print("- Verifica que las llamadas ocurrieron con assert_called_*")


def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Mocking")
        print("=" * 50)
        print("1. Mock de API externa")
        print("2. patch como context manager")
        print("3. Side effects")
        print("0. Salir")
        print()

        opcion = input("Ver solucion: ")

        soluciones = {"1": solucion_1, "2": solucion_2, "3": solucion_3}

        if opcion in soluciones:
            soluciones[opcion]()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue asi!")
            break
        else:
            print("Opcion invalida")


def main():
    args = sys.argv[1:]
    if args and args[0].isdigit():
        [solucion_1, solucion_2, solucion_3][int(args[0]) - 1]()
    else:
        menu()


if __name__ == "__main__":
    main()
