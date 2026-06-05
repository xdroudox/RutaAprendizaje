# JSON y XML

JSON (JavaScript Object Notation) y XML (eXtensible Markup Language) son formatos de intercambio de datos.

## JSON
- Ligero y legible
- `json.dumps()`: dict/lista a string JSON
- `json.loads()`: string JSON a dict/lista
- `json.dump()`: escribe JSON a archivo
- `json.load()`: lee JSON desde archivo

## XML
- Mas verboso, con etiquetas
- Usa `xml.etree.ElementTree`
- Soporta atributos y namespaces

## Ejercicios

1. **Convertir dict a JSON** - Usar json.dumps() para serializar un diccionario.
   **Ejecuta:** `python scripts/runner.py 5 3 1`

2. **Parsear JSON a dict** - Usar json.loads() para deserializar un string JSON.
   **Ejecuta:** `python scripts/runner.py 5 3 2`

3. **Leer JSON de archivo** - Usar json.load() para leer datos desde un archivo JSON.
   **Ejecuta:** `python scripts/runner.py 5 3 3`
