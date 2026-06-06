"""
EJERCICIOS - Pruebas de API
Ejecuta desde raiz: python scripts/runner.py 7 5 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Probar GET a JSONPlaceholder"""
    print(">> EJERCICIO 1: Probar GET a JSONPlaceholder")
    print("-" * 40)
    print("Usando la libreria requests, haz una peticion GET a:")
    print("https://jsonplaceholder.typicode.com/posts/1")
    print()
    print("Verifica:")
    print("- status_code == 200")
    print("- La respuesta contiene 'title'")
    print("- El campo 'id' es 1")
    print()
    print("import requests")
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  import requests")
        print("  response = requests.get('https://jsonplaceholder.typicode.com/posts/1')")
        print("  assert response.status_code == 200")
        print("  data = response.json()  # Convierte JSON a dict")
        print("  assert 'title' in data")
        print("  assert data['id'] == 1")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  import requests")
        print("  response = requests.get('https://jsonplaceholder.typicode.com/posts/1')")
        print("  assert response.status_code == 200, f'Status: {response.status_code}'")
        print("  data = response.json()")
        print("  assert 'title' in data, 'Falta campo title'")
        print("  assert data['id'] == 1, f'ID esperado 1, obtenido {data[\"id\"]}'")
        print("  print(f'GET exitoso. Post 1: {data[\"title\"]}')")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  import requests")
        print("  response = requests.get('https://jsonplaceholder.typicode.com/posts/1')")
        print("  assert response.status_code == 200")
        print("  data = response.json()")
        print("  assert 'title' in data")
        print("  assert data['id'] == 1")
        print("  print(f'GET exitoso. Post 1: {data[\"title\"]}')")

def ejercicio_2(pista=0):
    """Probar POST con datos JSON"""
    print(">> EJERCICIO 2: Probar POST con datos JSON")
    print("-" * 40)
    print("Haz una peticion POST a:")
    print("https://jsonplaceholder.typicode.com/posts")
    print()
    print("Envia JSON: {'title': 'foo', 'body': 'bar', 'userId': 1}")
    print()
    print("Verifica:")
    print("- status_code == 201")
    print("- La respuesta contiene 'id'")
    print()
    print("import requests")
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  import requests")
        print("  payload = {'title': 'foo', 'body': 'bar', 'userId': 1}")
        print("  response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)")
        print("  assert response.status_code == 201")
        print("  data = response.json()")
        print("  assert 'id' in data")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  import requests")
        print("  payload = {'title': 'foo', 'body': 'bar', 'userId': 1}")
        print("  response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)")
        print("  assert response.status_code == 201, f'Status: {response.status_code}'")
        print("  data = response.json()")
        print("  assert 'id' in data, 'Respuesta no contiene id'")
        print("  print(f'POST exitoso. Creado con ID: {data[\"id\"]}')")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  import requests")
        print("  payload = {'title': 'foo', 'body': 'bar', 'userId': 1}")
        print("  response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)")
        print("  assert response.status_code == 201")
        print("  data = response.json()")
        print("  assert 'id' in data")
        print("  print(f'POST exitoso. Creado con ID: {data[\"id\"]}')")

def ejercicio_3(pista=0):
    """Validar estructura de response (status, headers, body)"""
    print(">> EJERCICIO 3: Validar estructura de response (status, headers, body)")
    print("-" * 40)
    print("Haz GET a https://jsonplaceholder.typicode.com/users")
    print()
    print("Verifica:")
    print("- status_code == 200")
    print("- Content-Type contiene 'application/json'")
    print("- La respuesta es una lista")
    print("- Cada usuario tiene: id, name, email")
    print()
    print("import requests")
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  import requests")
        print("  response = requests.get('https://jsonplaceholder.typicode.com/users')")
        print("  assert response.status_code == 200")
        print("  assert 'application/json' in response.headers.get('Content-Type', '')")
        print("  usuarios = response.json()")
        print("  assert isinstance(usuarios, list)")
        print("  for u in usuarios:")
        print("      assert 'id' in u")
        print("      assert 'name' in u")
        print("      assert 'email' in u")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  import requests")
        print("  response = requests.get('https://jsonplaceholder.typicode.com/users')")
        print("  assert response.status_code == 200")
        print("  assert 'application/json' in response.headers.get('Content-Type', '')")
        print("  usuarios = response.json()")
        print("  assert isinstance(usuarios, list) and len(usuarios) > 0")
        print("  for u in usuarios:")
        print("      assert 'id' in u and 'name' in u and 'email' in u")
        print("  print(f'GET /users exitoso. {len(usuarios)} usuarios validados.')")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  import requests")
        print("  response = requests.get('https://jsonplaceholder.typicode.com/users')")
        print("  assert response.status_code == 200")
        print("  assert 'application/json' in response.headers.get('Content-Type', '')")
        print("  usuarios = response.json()")
        print("  assert isinstance(usuarios, list)")
        print("  for u in usuarios:")
        print("      assert 'id' in u")
        print("      assert 'name' in u")
        print("      assert 'email' in u")
        print("  print(f'GET /users exitoso. {len(usuarios)} usuarios validados.')")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    pista_level = 0
    if "-p" in sys.argv:
        idx = sys.argv.index("-p")
        if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
            pista_level = int(sys.argv[idx + 1])
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num](pista=pista_level)
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
