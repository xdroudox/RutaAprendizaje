# Mocking

Reemplazar objetos reales por simulados para aislar la unidad bajo prueba.

## unittest.mock

```python
from unittest.mock import Mock, patch

# Mock directo
mock = Mock()
mock.metodo.return_value = 42

# patch como decorador
@patch('modulo.funcion')
def test_algo(mock_funcion):
    mock_funcion.return_value = 'mockeado'

# side_effect
mock.metodo.side_effect = ValueError('Error simulado')
```

## Ejercicios

1. **Mockear funcion externa con unittest.mock**
   **Ejecuta:** `python scripts/runner.py 7 4 1`

2. **Verificar que mock fue llamado con argumentos correctos**
   **Ejecuta:** `python scripts/runner.py 7 4 2`

3. **Mock con side_effect para simular errores**
   **Ejecuta:** `python scripts/runner.py 7 4 3`
