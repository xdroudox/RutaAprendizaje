"""
SOLUCIONES - Pruebas de API
Ejecuta desde raiz: python scripts/runner.py 7 5 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Probar GET a JSONPlaceholder"""
    import requests
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    data = response.json()
    assert 'title' in data
    assert data['id'] == 1
    print(">> SOLUCION 1: Probar GET a JSONPlaceholder")
    print("-" * 40)
    print(f"GET exitoso. Post 1: {data['title']}")

def solucion_2():
    """Probar POST con datos JSON"""
    import requests
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data
    print(">> SOLUCION 2: Probar POST con datos JSON")
    print("-" * 40)
    print(f"POST exitoso. Creado con ID: {data['id']}")

def solucion_3():
    """Validar estructura de response (status, headers, body)"""
    import requests
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    assert response.status_code == 200
    assert 'application/json' in response.headers.get('Content-Type', '')
    usuarios = response.json()
    assert isinstance(usuarios, list)
    for u in usuarios:
        assert 'id' in u
        assert 'name' in u
        assert 'email' in u
    print(">> SOLUCION 3: Validar estructura de response")
    print("-" * 40)
    print(f"GET /users exitoso. {len(usuarios)} usuarios validados.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
