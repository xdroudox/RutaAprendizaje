# HTML Semantico

## Que es HTML semantico?

HTML semantico significa usar etiquetas que describen el significado del contenido, no solo como se ve. En lugar de usar `<div>` para todo, usamos etiquetas como `<header>`, `<nav>`, `<main>`, `<article>`, etc.

## Etiquetas semanticas principales

```
+--------------------------------------------------+
|  <header>                                         |
|  +------------------------------------------+    |
|  |  <nav>   Home | Blog | Contacto          |    |
|  +------------------------------------------+    |
+--------------------------------------------------+

+--------------------------------------------------+
|  <main>                                           |
|  +--------+  +--------------------------------+  |
|  |<aside> |  | <section>                      |  |
|  | Menu   |  |  <article>                     |  |
|  | lateral|  |   - Titulo                     |  |
|  |        |  |   - Contenido                  |  |
|  +--------+  +--------------------------------+  |
+--------------------------------------------------+

+--------------------------------------------------+
|  <footer>                                         |
|  Copyright 2025 - Todos los derechos reservados   |
+--------------------------------------------------+
```

### Etiquetas y su proposito

| Etiqueta | Proposito |
|----------|-----------|
| `<header>` | Encabezado de pagina o seccion (logo, titulo, intro) |
| `<nav>` | Navegacion principal (menus, enlaces) |
| `<main>` | Contenido principal unico de la pagina |
| `<section>` | Agrupacion tematica de contenido |
| `<article>` | Contenido independiente (blog post, noticia) |
| `<aside>` | Contenido complementario (sidebar, anuncios) |
| `<footer>` | Pie de pagina (copyright, enlaces legales) |
| `<figure>` | Contenido visual con `<figcaption>` |
| `<time>` | Fechas y horas legibles por maquina |

## Por que es importante?

1. **Accesibilidad**: Los lectores de pantalla usan la semantica para navegar
2. **SEO**: Los motores de busqueda entienden mejor la estructura
3. **Mantenibilidad**: El codigo es mas legible para otros desarrolladores
4. **Estandar**: Sigue las especificaciones del W3C

## Ejemplo basico

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Mi Blog</title>
</head>
<body>
  <header>
    <h1>Mi Blog de Tecnologia</h1>
    <nav>
      <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/contacto">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article>
      <header>
        <h2>Aprendiendo HTML Semantico</h2>
        <time datetime="2025-01-15">15 Enero 2025</time>
      </header>
      <p>El HTML semantico mejora la accesibilidad...</p>
    </article>

    <aside>
      <h3>Articulos Recientes</h3>
      <ul>
        <li><a href="#">CSS Grid vs Flexbox</a></li>
        <li><a href="#">JavaScript Moderno</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2025 Mi Blog. Todos los derechos reservados.</p>
  </footer>
</body>
</html>
```

## Accesibilidad basica

- Usa `<h1>` a `<h6>` jerarquicamente (un solo `<h1>` por pagina)
- Los `<button>` deben etiquetarse (nunca `<div>` clickeables sin rol)
- Usa `alt` en todas las `<img>`
- Usa `label` asociado a los inputs de formularios
- Atributo `lang` en `<html>` correcto

## Ejercicios

Abre `ejercicios.html` en tu navegador y completa los 3 ejercicios.
