"""
SOLUCIONES - Pruebas de API
Ejecuta desde raiz: python scripts/runner.py 7 5 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Solucion: GET a JSONPlaceholder"""
    import requests
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    data = response.json()
    assert 'title' in data
    assert data['id'] == 1
    print(f"GET exitoso. Post 1: {data['title']}")

def ejercicio_2():
    """Solucion: POST con datos JSON"""
    import requests
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data
    print(f"POST exitoso. Creado con ID: {data['id']}")

def ejercicio_3():
    """Solucion: validar estructura de response"""
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
    print(f"GET /users exitoso. {len(usuarios)} usuarios validados.")

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
