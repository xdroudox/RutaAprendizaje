# Pruebas de API

Verificar que endpoints HTTP funcionen correctamente.

## requests

```python
import requests

response = requests.get('https://api.ejemplo.com/usuarios')
response = requests.post('https://api.ejemplo.com/usuarios', json={'nombre': 'Ana'})
```

## Validaciones comunes

```python
assert response.status_code == 200
assert 'application/json' in response.headers['Content-Type']
data = response.json()
assert 'id' in data
```

## Ejercicios

1. **Probar GET a JSONPlaceholder**
   **Ejecuta:** `python scripts/runner.py 7 5 1`

2. **Probar POST con datos JSON**
   **Ejecuta:** `python scripts/runner.py 7 5 2`

3. **Validar estructura de response (status, headers, body)**
   **Ejecuta:** `python scripts/runner.py 7 5 3`
