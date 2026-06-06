# Mocking

Reemplazar objetos reales por simulados para aislar la unidad bajo prueba.

## Conceptos Basicos

- **Mock**: objeto simulado que imita el comportamiento de un objeto real.
- **Stub**: objeto que retorna valores fijos predefinidos.
- **Spy**: mock que registra como fue llamado (con que argumentos, cuantas veces).
- **Patch**: mecanismo para reemplazar temporalmente una funcion/clase por un mock.
- **Side effect**: comportamiento alternativo que ejecuta el mock (lanzar error, retornar valores distintos).

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Mock** | Objeto simulado que puede retornar valores y verificar llamadas |
| **Stub** | Objeto que solo retorna valores predefinidos (no verifica) |
| **Spy** | Mock que registra interacciones para verificacion posterior |
| **Patch** | Decorador/contexto que reemplaza un objeto real por un mock |
| **Side Effect** | Funcion o excepcion que se ejecuta cuando se llama al mock |
| **return_value** | Valor fijo que retorna el mock al ser llamado |
| **assert_called_once_with** | Verifica que el mock fue llamado con argumentos especificos |
| **call_count** | Numero de veces que se invoco el mock |

## Comparativa entre Lenguajes

### Python (unittest.mock)
```python
from unittest.mock import Mock, patch

# Mock directo
mock_api = Mock()
mock_api.return_value = {"temperatura": 25}

# Patch como context manager
with patch('modulo.obtener_clima') as mock_clima:
    mock_clima.return_value = 25
    resultado = reporte_clima('Madrid')
    assert resultado == 'Temperatura en Madrid: 25°C'
```

### Java (Mockito)
```java
import static org.mockito.Mockito.*;

// Mock directo
ApiService mockApi = mock(ApiService.class);
when(mockApi.obtenerClima("Madrid")).thenReturn(25);

// Verificar llamada
verify(mockApi).obtenerClima("Madrid");
```

### JavaScript (Jest)
```javascript
// Mock directo
const mockApi = jest.fn();
mockApi.mockReturnValue(25);

// Spy
const utils = { obtenerClima: () => 25 };
jest.spyOn(utils, 'obtenerClima');
expect(utils.obtenerClima).toHaveBeenCalledWith('Madrid');
```

## unittest.mock en detalle

### Mock basico
```python
from unittest.mock import Mock

mock = Mock()
mock.return_value = 42  # Siempre retorna 42
print(mock())  # 42

mock.side_effect = [10, 20, 30]  # Retorna diferente en cada llamada
print(mock())  # 10
print(mock())  # 20
print(mock())  # 30
```

### Verificaciones
```python
mock = Mock()
mock('Hola', clave='valor')

mock.assert_called()                    # Fue llamado al menos una vez
mock.assert_called_once()               # Fue llamado exactamente una vez
mock.assert_called_with('Hola', clave='valor')  # Con argumentos exactos
mock.assert_called_once_with('Hola', clave='valor')  # Una vez con esos args
print(mock.call_count)                  # Numero de llamadas
print(mock.call_args)                   # Ultimos argumentos recibidos
```

### Patch

Reemplaza temporalmente un objeto durante la prueba:

```python
from unittest.mock import patch

# Como decorador
@patch('modulo.funcion_externa')
def test_algo(mock_funcion):
    mock_funcion.return_value = 'mockeado'
    # Dentro de la prueba, modulo.funcion_externa es un mock
    resultado = modulo.mi_funcion()
    assert resultado == 'mockeado'

# Como context manager
def test_algo():
    with patch('modulo.funcion_externa') as mock_funcion:
        mock_funcion.return_value = 'mockeado'
        resultado = modulo.mi_funcion()
        assert resultado == 'mockeado'
```

### Side effect para simular errores

```python
from unittest.mock import Mock

mock = Mock()
mock.side_effect = ValueError('Error simulado')

try:
    mock()
except ValueError as e:
    print(e)  # 'Error simulado'
```

## Ejemplo Guiado: Mockear API externa

Paso 1: Funcion original que llama a API
```python
def obtener_clima(ciudad):
    # Llama a API real (no implementada en pruebas)
    raise NotImplementedError()

def reporte_clima(ciudad):
    temp = obtener_clima(ciudad)
    return f'Temperatura en {ciudad}: {temp}°C'
```

Paso 2: Prueba con mock
```python
from unittest.mock import Mock

def test_reporte_clima():
    # Creamos el mock
    mock_clima = Mock()
    mock_clima.side_effect = lambda c: 25 if c == 'Madrid' else 30

    # Reemplazamos la funcion real por el mock
    import __main__
    __main__.obtener_clima = mock_clima

    # Probamos sin llamar a la API real
    resultado = reporte_clima('Madrid')
    assert resultado == 'Temperatura en Madrid: 25°C'
```

## Referencia rapida

| Funcion/Clase | Descripcion |
|---------------|-------------|
| `Mock()` | Crea un objeto mock generico |
| `mock.return_value = X` | Valor fijo que retorna el mock |
| `mock.side_effect = [a,b,c]` | Valores diferentes en cada llamada |
| `mock.side_effect = Exception` | Lanza excepcion al ser llamado |
| `patch('ruta.modulo.funcion')` | Reemplaza funcion por mock |
| `mock.assert_called_once_with(X)` | Verifica argumentos de la llamada |
| `mock.call_count` | Cuantas veces fue llamado |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 7 4 [ejercicio] [-p N]`

1. 🟢 **Mockear funcion externa con unittest.mock**
2. 🟡 **Verificar que mock fue llamado con argumentos correctos**
3. 🟡 **Mock con side_effect para simular errores**
