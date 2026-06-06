"""
EJERCICIOS - Fetch API
Ejecuta desde raiz: python scripts/runner.py 6 6 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """GET request con fetch"""
    print(">> EJERCICIO 1: GET request con fetch")
    print("-" * 40)
    print("Este ejercicio es en HTML/JS.")
    print("Abre el archivo en tu navegador:")
    print("  06-frontend-web/06-fetch-api/ejercicios.html")
    print()
    print("Usa fetch() para obtener los primeros 5 posts de")
    print("JSONPlaceholder y muestralos en pantalla.")
    print("Endpoint: https://jsonplaceholder.typicode.com/posts")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  fetch(API_URL + '/posts')")
        print("    .then(function(respuesta) { return respuesta.json(); })")
        print("    .then(function(data) {")
        print("      // data es un array de 100 posts")
        print("      // Usa .slice(0, 5) para obtener los primeros 5")
        print("    })")
        print("    .catch(function(error) { console.error(error); });")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  fetch(API_URL + '/posts')")
        print("    .then(function(respuesta) { return respuesta.json(); })")
        print("    .then(function(data) {")
        print("        var posts = data.slice(0, 5);")
        print("        resultado.innerHTML = '';")
        print("        posts.forEach(function(post) {")
        print("            var card = document.createElement('div');")
        print("            card.className = 'card';")
        print("            card.innerHTML = '<h3>' + post.title + '</h3><p>' + post.body + '</p>';")
        print("            resultado.appendChild(card);")
        print("        });")
        print("    })")
        print("    .catch(function(error) {")
        print("        resultado.textContent = 'Error: ' + error.message;")
        print("    });")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  var resultado = document.getElementById('resultado-ej1');")
        print("  resultado.textContent = 'Cargando...';")
        print("  fetch(API_URL + '/posts')")
        print("    .then(function(r) { return r.json(); })")
        print("    .then(function(data) {")
        print("        resultado.innerHTML = '';")
        print("        data.slice(0, 5).forEach(function(post) {")
        print("            var card = document.createElement('div');")
        print("            card.className = 'card';")
        print("            card.innerHTML = '<h3>' + post.title + '</h3><p>' + post.body + '</p>';")
        print("            resultado.appendChild(card);")
        print("        });")
        print("    })")
        print("    .catch(function(error) { resultado.textContent = 'Error: ' + error.message; });")

def ejercicio_2(pista=0):
    """POST request con JSON body"""
    print(">> EJERCICIO 2: POST request con JSON body")
    print("-" * 40)
    print("Abre: 06-frontend-web/06-fetch-api/ejercicios.html")
    print()
    print("Envia un POST con method, headers y body.")
    print("Incluye Content-Type: application/json")
    print("Muestra la respuesta del servidor.")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  fetch(API_URL + '/posts', {")
        print("      method: 'POST',")
        print("      headers: { 'Content-Type': 'application/json' },")
        print("      body: JSON.stringify({ title: titulo, body: cuerpo, userId: 1 })")
        print("  })")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  fetch(API_URL + '/posts', {")
        print("      method: 'POST',")
        print("      headers: { 'Content-Type': 'application/json' },")
        print("      body: JSON.stringify({ title: title, body: body, userId: 1 })")
        print("  })")
        print("  .then(function(r) { return r.json(); })")
        print("  .then(function(data) {")
        print("      resultado.textContent = JSON.stringify(data, null, 2);")
        print("  })")
        print("  .catch(function(error) { resultado.textContent = 'Error: ' + error.message; });")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  var title = document.getElementById('titulo-post').value;")
        print("  var body = document.getElementById('cuerpo-post').value;")
        print("  fetch(API_URL + '/posts', {")
        print("      method: 'POST',")
        print("      headers: { 'Content-Type': 'application/json' },")
        print("      body: JSON.stringify({ title: title, body: body, userId: 1 })")
        print("  })")
        print("  .then(function(r) { return r.json(); })")
        print("  .then(function(data) { resultado.textContent = JSON.stringify(data, null, 2); })")
        print("  .catch(function(error) { resultado.textContent = 'Error: ' + error.message; });")

def ejercicio_3(pista=0):
    """Manejar errores de fetch con catch"""
    print(">> EJERCICIO 3: Manejar errores de fetch con catch")
    print("-" * 40)
    print("Abre: 06-frontend-web/06-fetch-api/ejercicios.html")
    print()
    print("Usa async/await con try/catch.")
    print("Verifica respuesta.ok, lanza error si !ok.")
    print("Muestra mensaje de error si falla la peticion.")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  async function ejercicio3() {")
        print("      try {")
        print("          var respuesta = await fetch(url);")
        print("          if (!respuesta.ok) {")
        print("              throw new Error('HTTP ' + respuesta.status);")
        print("          }")
        print("          var data = await respuesta.json();")
        print("          // mostrar data")
        print("      } catch (error) {")
        print("          // mostrar error")
        print("      }")
        print("  }")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  async function ejercicio3() {")
        print("      try {")
        print("          var respuesta = await fetch(API_URL + '/posts/' + postId);")
        print("          if (!respuesta.ok) {")
        print("              throw new Error('HTTP ' + respuesta.status);")
        print("          }")
        print("          var post = await respuesta.json();")
        print("          resultado.textContent = JSON.stringify(post, null, 2);")
        print("      } catch (error) {")
        print("          resultado.textContent = 'Error: ' + error.message;")
        print("      }")
        print("  }")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  async function ejercicio3() {")
        print("      var postId = document.getElementById('post-id').value || 1;")
        print("      try {")
        print("          var respuesta = await fetch(API_URL + '/posts/' + postId);")
        print("          if (!respuesta.ok) {")
        print("              throw new Error('HTTP ' + respuesta.status + ' ' + respuesta.statusText);")
        print("          }")
        print("          var post = await respuesta.json();")
        print("          resultado.innerHTML = '<h3>' + post.title + '</h3><p>' + post.body + '</p>';")
        print("      } catch (error) {")
        print("          resultado.textContent = 'Error: ' + error.message;")
        print("      }")
        print("  }")

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
