# CSS Flexbox y Grid

## Introduccion

CSS Flexbox y CSS Grid son los dos sistemas de layout modernos que reemplazaron a los floats y tablas. Flexbox es unidimensional (fila O columna), Grid es bidimensional (filas Y columnas).

## Flexbox

Flexbox distribuye elementos en una sola direccion (por defecto, fila horizontal).

```
    contenedor (display: flex)
    +--------------------------------------------------+
    |    | item1 |    | item2 |    | item3 |           |
    |    +-------+    +-------+    +-------+           |
    |    justify-content: center (horizontal)          |
    |    align-items: center (vertical)                |
    +--------------------------------------------------+
```

### Propiedades del contenedor

```css
.contenedor {
    display: flex;
    flex-direction: row;       /* row | column | row-reverse | column-reverse */
    justify-content: center;   /* flex-start | flex-end | center | space-between | space-around | space-evenly */
    align-items: center;       /* flex-start | flex-end | center | stretch | baseline */
    flex-wrap: wrap;           /* nowrap | wrap | wrap-reverse */
    gap: 10px;                 /* espacio entre items */
}
```

### Propiedades de los items

```css
.item {
    flex: 1;                   /* shorthand: grow shrink basis */
    flex-grow: 1;              /* cuanto crece respecto a otros */
    flex-shrink: 1;            /* cuanto se encoge */
    flex-basis: auto;          /* tamaño base antes de crecer/encoger */
    align-self: center;        /* alineacion individual (sobrescribe align-items) */
    order: 0;                  /* orden de aparicion (-1 va primero) */
}
```

## CSS Grid

Grid trabaja con filas y columnas simultaneamente.

```
    contenedor (display: grid)
    +---------------+---------------+---------------+
    |    header     |    header     |    header     |
    +---------------+---------------+---------------+
    |    sidebar    |    main       |    aside      |
    +---------------+---------------+---------------+
    |    footer     |    footer     |    footer     |
    +---------------+---------------+---------------+
```

### Propiedades del contenedor

```css
.contenedor {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;   /* 3 columnas: 1 parte, 2 partes, 1 parte */
    grid-template-rows: auto 1fr auto;     /* 3 filas */
    gap: 10px;                              /* espacio entre celdas */
    grid-template-areas:                    /* nombra areas */
        "header  header  header"
        "sidebar main    aside"
        "footer  footer  footer";
}
```

### Asignar items a areas

```css
.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.aside { grid-area: aside; }
.footer { grid-area: footer; }
```

### Propiedades avanzadas de Grid

```css
.item {
    grid-column: 1 / 3;          /* de columna 1 a 3 (span 2) */
    grid-row: 1 / 2;             /* de fila 1 a 2 */
    justify-self: center;        /* alineacion horizontal individual */
    align-self: stretch;         /* alineacion vertical individual */
}
```

## Flexbox vs Grid: Cuando usar cada uno

| Situacion | Recomendado |
|-----------|-------------|
| Barra de navegacion horizontal | Flexbox |
| Centrar un elemento | Flexbox |
| Galeria de imagenes responsiva | Flexbox con wrap |
| Layout completo de pagina | Grid |
| Dashboard con widgets | Grid |
| Formulario con filas y columnas | Grid |

## Media Queries

Combinados con Flexbox/Grid, los media queries crean diseños responsivos:

```css
/* Mobile: una columna */
.contenedor {
    display: grid;
    grid-template-columns: 1fr;
}

/* Tablet: 2 columnas */
@media (min-width: 768px) {
    .contenedor {
        grid-template-columns: 1fr 1fr;
    }
}

/* Desktop: 3 columnas */
@media (min-width: 1024px) {
    .contenedor {
        grid-template-columns: 1fr 2fr 1fr;
    }
}
```

## Ejercicios

### Ejercicio 1: Centrar elemento con Flexbox
Usa display:flex, justify-content:center y align-items:center para centrar un elemento.
**Ejecuta:** `python scripts/runner.py 6 2 1`
**O abre directo:** `06-frontend-web/02-css-flexbox-grid/ejercicios.html`

### Ejercicio 2: Galeria responsiva con Flexbox wrap
Crea una galeria responsiva con flex-wrap y flex-basis que se adapte a diferentes pantallas.
**Ejecuta:** `python scripts/runner.py 6 2 2`
**O abre directo:** `06-frontend-web/02-css-flexbox-grid/ejercicios.html`

### Ejercicio 3: Layout completo con CSS Grid
Crea un layout de pagina completo con grid-template-columns, grid-template-rows y grid-area.
**Ejecuta:** `python scripts/runner.py 6 2 3`
**O abre directo:** `06-frontend-web/02-css-flexbox-grid/ejercicios.html`
