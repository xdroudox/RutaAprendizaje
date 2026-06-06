# JSON y XML

## Contenido
- JSON: formato, serializacion (dumps/loads), archivos
- XML: estructura con etiquetas
- Comparativa JSON vs XML

---

## 1. JSON (JavaScript Object Notation)

Formato ligero de intercambio de datos, basado en la sintaxis de objetos de JavaScript. Es el formato mas usado en APIs REST.

### Tipos de datos JSON

| JSON          | Python          | Ejemplo |
|--------------|----------------|---------|
| string       | str            | `"nombre"` |
| number       | int / float    | `25`, `3.14` |
| boolean      | bool           | `true` / `false` |
| null         | None           | `null` |
| array        | list           | `[1, 2, 3]` |
| object       | dict           | `{"clave": "valor"}` |

### Funciones principales de `json`

| Funcion        | Description |
|---------------|-------------|
| `json.dumps(obj)` | Convierte Python dict/list a string JSON |
| `json.loads(str)` | Convierte string JSON a Python dict/list |
| `json.dump(obj, f)` | Escribe JSON a archivo |
| `json.load(f)` | Lee JSON desde archivo |

---

## 2. XML (eXtensible Markup Language)

Formato mas verboso que JSON, usa etiquetas de apertura y cierre.

```xml
<usuario>
    <id>1</id>
    <nombre>Ana</nombre>
    <email>ana@ejemplo.com</email>
    <activo>true</activo>
</usuario>
```

Equivalente JSON:
```json
{
    "id": 1,
    "nombre": "Ana",
    "email": "ana@ejemplo.com",
    "activo": true
}
```

---

## 3. JSON vs XML

| Aspecto         | JSON | XML |
|----------------|------|-----|
| Legibilidad    | Alta | Media |
| Verbosidad     | Baja | Alta |
| Tipos de datos | Nativos (string, number, boolean, null, array, object) | Solo texto (todo es string) |
| Arrays         | `[...]` nativo | No tiene array nativo |
| Atributos      | No soporta | Soporta `<tag attr="val">` |
| Namespaces     | No soporta | Soporta |
| Velocidad parseo | Rapido | Lento |
| Uso tipico     | APIs REST, configuraciones | Documentos, SOAP, configuraciones legacy |

---

## 4. Glosario

| Termino          | Definicion |
|-----------------|-----------|
| **JSON**        | JavaScript Object Notation - formato ligero de intercambio de datos |
| **XML**         | eXtensible Markup Language - formato de marcado para documentos |
| **Serializar**  | Convertir un objeto en memoria a un formato almacenable (JSON string) |
| **Deserializar** | Convertir un formato almacenable (JSON string) a un objeto en memoria |
| **dump**        | Escribir JSON a un archivo |
| **load**        | Leer JSON desde un archivo |
| **dumps**       | Convertir objeto a string JSON (serializar) |
| **loads**       | Convertir string JSON a objeto (deserializar) |

---

## 5. Comparativa entre lenguajes

### Python
```python
import json
datos = {"nombre": "Ana", "edad": 30}
json_str = json.dumps(datos, indent=2)
datos2 = json.loads(json_str)
```

### JavaScript
```javascript
const datos = { nombre: "Ana", edad: 30 };
const jsonStr = JSON.stringify(datos, null, 2);
const datos2 = JSON.parse(jsonStr);
```

### Java (Jackson)
```java
ObjectMapper mapper = new ObjectMapper();
String json = mapper.writeValueAsString(datos);
User user = mapper.readValue(json, User.class);
```

---

## 6. Ejemplo guiado paso a paso

**Problema:** Tienes datos de un usuario en un diccionario. Quieres enviarlos por HTTP.

1. Partimos del diccionario:
   ```python
   usuario = {"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com"}
   ```

2. Serializamos a JSON string:
   ```python
   json_str = json.dumps(usuario)
   # '{"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com"}'
   ```

3. Enviamos por HTTP (body del request)

4. El servidor recibe y deserializa:
   ```python
   datos = json.loads(json_str)
   nombre = datos["nombre"]  # "Ana"
   ```

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Convertir dict a JSON con json.dumps() | 🟢 |
| 2  | Parsear JSON a dict con json.loads() | 🟡 |
| 3  | Leer JSON de archivo y extraer datos | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 3 1
python scripts/runner.py 5 3 2
python scripts/runner.py 5 3 3
python scripts/runner.py 5 3 1 -p 1
python scripts/runner.py 5 3 3 -s
```
