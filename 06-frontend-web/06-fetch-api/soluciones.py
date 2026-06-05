"""
SOLUCIONES - Fetch API
Ejecuta desde raiz: python scripts/runner.py 6 6 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """GET request con fetch"""
    print(">> SOLUCION 1: GET request con fetch")
    print("-" * 40)
    print("function ejercicio1() {")
    print("    var resultado = document.getElementById('resultado-ej1');")
    print("    resultado.textContent = 'Cargando...';")
    print("    fetch(API_URL + '/posts')")
    print("        .then(function(respuesta) { return respuesta.json(); })")
    print("        .then(function(data) {")
    print("            var posts = data.slice(0, 5);")
    print("            resultado.innerHTML = '';")
    print("            posts.forEach(function(post) {")
    print("                var card = document.createElement('div');")
    print("                card.className = 'card';")
    print("                card.innerHTML = '<h3>' + post.title + '</h3><p>' + post.body + '</p>';")
    print("                resultado.appendChild(card);")
    print("            });")
    print("        })")
    print("        .catch(function(error) {")
    print("            resultado.textContent = 'Error: ' + error.message;")
    print("        });")
    print("}")
    print()
    print("Abre soluciones.html en el navegador para verlo en accion.")

def ejercicio_2():
    """POST request con JSON body"""
    print(">> SOLUCION 2: POST request con JSON body")
    print("-" * 40)
    print("function ejercicio2() {")
    print("    fetch(API_URL + '/posts', {")
    print("        method: 'POST',")
    print("        headers: { 'Content-Type': 'application/json' },")
    print("        body: JSON.stringify({ title: title, body: body, userId: 1 })")
    print("    })")
    print("    .then(function(r) { return r.json(); })")
    print("    .then(function(data) {")
    print("        resultado.textContent = JSON.stringify(data, null, 2);")
    print("    })")
    print("    .catch(function(error) {")
    print("        resultado.textContent = 'Error: ' + error.message;")
    print("    });")
    print("}")

def ejercicio_3():
    """Manejar errores de fetch con catch"""
    print(">> SOLUCION 3: Manejar errores de fetch con catch")
    print("-" * 40)
    print("async function ejercicio3() {")
    print("    try {")
    print("        var respuesta = await fetch(API_URL + '/posts/' + postId);")
    print("        if (!respuesta.ok) {")
    print("            throw new Error('HTTP ' + respuesta.status);")
    print("        }")
    print("        var post = await respuesta.json();")
    print("        resultado.textContent = JSON.stringify(post, null, 2);")
    print("    } catch (error) {")
    print("        resultado.textContent = 'Error: ' + error.message;")
    print("    }")
    print("}")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
