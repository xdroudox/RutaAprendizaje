# Mocking

## Que es mocking

Mocking es la tecnica de reemplazar objetos reales por objetos simulados (mocks) para aislar la unidad bajo prueba.

## Cuando mockear vs usar objetos reales

Mockear cuando:
- El objeto real hace llamadas a redes/API
- El objeto real accede a bases de datos
- El objeto real es lento o costoso
- El objeto real es dificil de configurar
- Se quiere probar comportamiento especifico (errores, timeouts)

Usar objetos reales cuando:
- El objeto es simple y rapido
- Se quiere probar la integracion real
- El mock daria una falsa sensacion de seguridad

## unittest.mock

Python incluye el modulo `unittest.mock` con la clase `Mock` y la funcion `patch`.

### Mock basico

```python
from unittest.mock import Mock

m = Mock()
m.retornar_dato.return_value = 42
print(m.retornar_dato())  # 42

m.hacer_algo.side_effect = Exception("Error simulado")
m.hacer_algo()  # Lanza Exception
```

### patch

`patch` reemplaza un objeto en un modulo durante una prueba:

```python
from unittest.mock import patch

@patch("modulo.externo.obtener_datos")
def test_con_patch(mock_obtener_datos):
    mock_obtener_datos.return_value = {"id": 1, "nombre": "Mock"}
    resultado = mi_funcion()
    assert resultado["nombre"] == "Mock"
```

### patch como context manager

```python
def test_con_context_manager():
    with patch("modulo.externo.obtener_datos") as mock_obtener_datos:
        mock_obtener_datos.return_value = {"id": 1}
        resultado = mi_funcion()
        assert resultado["id"] == 1
```

## Side effects

Los side effects permiten simular comportamientos complejos:

```python
mock.obtener.return_value = "valor_fijo"

# Diferentes valores en cada llamada
mock.obtener.side_effect = [1, 2, 3]

# Llamar una funcion real
mock.obtener.side_effect = mi_funcion_real

# Lanzar excepcion
mock.obtener.side_effect = ConnectionError("Timeout")
```

## Verificar llamadas

```python
mock = Mock()
mock.hacer_algo(1, 2, clave="valor")

mock.hacer_algo.assert_called_once()
mock.hacer_algo.assert_called_with(1, 2, clave="valor")
mock.hacer_algo.assert_called_once_with(1, 2, clave="valor")
```
