"""
EJERCICIOS - Mocking
Ejecuta: python ejercicios.py [numero]

Uso:
  python ejercicios.py      -> Menu
  python ejercicios.py 1    -> Ejercicio 1
  python ejercicios.py -s 1 -> Solucion del ejercicio 1
"""

import sys
from unittest.mock import Mock, patch

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


class ServicioClima:
    def obtener_temperatura(self, ciudad):
        # Simula llamada a API externa
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


def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Mock de API externa")
    print("=" * 50)
    print()
    print("Dada la clase ReporteClima que depende de ServicioClima,")
    print("crea un Mock para ServicioClima.obtener_temperatura.")
    print()
    print("El mock debe retornar 35 cuando se llame con 'Madrid'.")
    print("Luego verifica que generar_reporte devuelva:")
    print("  'Hace calor en Madrid: 35°C'")
    print()
    print("PISTA: mock = Mock(); mock.obtener_temperatura.return_value = 35")
    print()
    print("Edita el archivo:")
    print("def test_reporte_clima_con_mock():")
    print("    # --- TU CODIGO AQUI ---")


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
    print("Verificaciones con Mock:")
    print("  - return_value: valor fijo que retorna el metodo")
    print("  - assert_called_once_with: verifica argumentos de llamada")


def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: patch como context manager")
    print("=" * 50)
    print()
    print("Usa patch de unittest.mock para reemplazar la funcion")
    print("obtener_datos_usuario durante la prueba.")
    print()
    print("  def obtener_datos_usuario(id_usuario):")
    print("      # Simula llamada a API externa")
    print("      return requests.get(f'https://api.ejemplo.com/usuarios/{id_usuario}').json()")
    print()
    print("  def mostrar_nombre_usuario(id_usuario):")
    print("      datos = obtener_datos_usuario(id_usuario)")
    print("      return f'Usuario: {datos[\"nombre\"]}'")
    print()
    print("Crea una prueba que:")
    print("  1. Use patch para mockear obtener_datos_usuario")
    print("  2. Haga que retorne {'nombre': 'Ana'}")
    print("  3. Verifique que mostrar_nombre_usuario(1) == 'Usuario: Ana'")
    print()
    print("PISTA: with patch('__main__.obtener_datos_usuario') as mock:")
    print()
    print("Edita el archivo:")
    print("def test_mostrar_nombre_usuario():")
    print("    # --- TU CODIGO AQUI ---")


def obtener_datos_usuario(id_usuario):
    import requests
    return requests.get(f"https://api.ejemplo.com/usuarios/{id_usuario}").json()


def mostrar_nombre_usuario(id_usuario):
    datos = obtener_datos_usuario(id_usuario)
    return f"Usuario: {datos['nombre']}"


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
    print()
    print("        resultado = mostrar_nombre_usuario(1)")
    print("        assert resultado == 'Usuario: Ana'")
    print("        mock_obtener.assert_called_once_with(1)")
    print("```")
    print()
    print("patch como decorador:")
    print()
    print("```python")
    print("@patch('__main__.obtener_datos_usuario')")
    print("def test_mostrar_nombre_usuario(mock_obtener):")
    print("    mock_obtener.return_value = {'nombre': 'Ana'}")
    print("    resultado = mostrar_nombre_usuario(1)")
    print("    assert resultado == 'Usuario: Ana'")
    print("```")
    print()
    print("patch reemplaza automaticamente el objeto en el modulo")
    print("durante la prueba y lo restaura al finalizar.")


def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Side effects")
    print("=" * 50)
    print()
    print("Usa side_effect de Mock para simular comportamientos:")
    print()
    print("  def procesar_pago(tarjeta, monto):")
    print("      if not validar_tarjeta(tarjeta):")
    print("          raise ValueError('Tarjeta invalida')")
    print("      if monto > 1000:")
    print("          raise ValueError('Monto excede el limite')")
    print("      cobrar(tarjeta, monto)")
    print("      return 'Pago exitoso'")
    print()
    print("Crea pruebas que mockeen validar_tarjeta y cobrar:")
    print("  1. Pago exitoso: validar_tarjeta -> True, cobrar -> None")
    print("  2. Tarjeta invalida: validar_tarjeta -> False")
    print("  3. Error al cobrar: cobrar.side_effect = ConnectionError")
    print()
    print("PISTA: mock.side_effect = Exception('mensaje')")
    print()
    print("Edita el archivo:")
    print("def test_pago_exitoso():")
    print("    # --- TU CODIGO AQUI ---")
    print()
    print("def test_tarjeta_invalida():")
    print("    # --- TU CODIGO AQUI ---")


def validar_tarjeta(tarjeta):
    raise NotImplementedError("Llama a servicio de validacion")


def cobrar(tarjeta, monto):
    raise NotImplementedError("Llama a pasarela de pago")


def procesar_pago(tarjeta, monto):
    if not validar_tarjeta(tarjeta):
        raise ValueError("Tarjeta invalida")
    if monto > 1000:
        raise ValueError("Monto excede el limite")
    cobrar(tarjeta, monto)
    return "Pago exitoso"


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
    print("Side effect puede ser:")
    print("  - Una excepcion: mock.side_effect = ValueError('error')")
    print("  - Una lista: mock.side_effect = [1, 2, 3] (valores en cada llamada)")
    print("  - Una funcion: mock.side_effect = mi_funcion")


def menu():
    while True:
        print()
        print("=" * 50)
        print("MOCKING - EJERCICIOS")
        print("=" * 50)
        print("1. Mock de API externa")
        print("2. patch como context manager")
        print("3. Side effects")
        print("0. Salir")
        print()

        opcion = input("Selecciona un ejercicio: ")

        if opcion == "1":
            ejercicio_1()
            input("Presiona ENTER para continuar...")
        elif opcion == "2":
            ejercicio_2()
            input("Presiona ENTER para continuar...")
        elif opcion == "3":
            ejercicio_3()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue practicando!")
            break
        else:
            print("Opcion invalida")


def main():
    args = sys.argv[1:]

    if not args:
        menu()
        return

    if "-s" in args:
        idx = args.index("-s")
        if idx + 1 < len(args) and args[idx + 1].isdigit():
            num = int(args[idx + 1])
            [solucion_1, solucion_2, solucion_3][num - 1]()
        return

    if args[0].isdigit():
        num = int(args[0])
        [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()


if __name__ == "__main__":
    main()
