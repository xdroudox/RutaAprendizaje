# JSON y XML

## JSON (JavaScript Object Notation)

Formato ligero de intercambio de datos. Basado en pares clave-valor.

```json
{
    "nombre": "Ana",
    "edad": 30,
    "activo": true,
    "hobbies": ["leer", "correr"],
    "direccion": {
        "ciudad": "Madrid",
        "cp": "28001"
    }
}
```

### Tipos JSON

- String: "texto"
- Number: 42, 3.14
- Boolean: true, false
- Null: null
- Array: [1, 2, 3]
- Object: {"clave": "valor"}

### Modulo json en Python

```python
import json

# Dict a JSON string
datos = {"nombre": "Ana", "edad": 30}
json_str = json.dumps(datos, indent=2)
print(json_str)

# JSON string a dict
datos2 = json.loads(json_str)
print(datos2["nombre"])

# Guardar a archivo
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=2)

# Leer de archivo
with open("datos.json") as f:
    datos3 = json.load(f)
```

## XML (eXtensible Markup Language)

Formato de marcado para datos estructurados.

```xml
<persona>
    <nombre>Ana</nombre>
    <edad>30</edad>
    <activo>true</activo>
    <hobbies>
        <hobbie>leer</hobbie>
        <hobbie>correr</hobbie>
    </hobbies>
    <direccion>
        <ciudad>Madrid</ciudad>
        <cp>28001</cp>
    </direccion>
</persona>
```

### Cuando usar cada uno

| JSON | XML |
|------|-----|
| Ligero y rapido | Mas verboso |
| Ideal para APIs REST | Usado en SOAP, configs |
| Tipos nativos | Todo es texto |
| Sin atributos | Soporta atributos |
| Facil de leer | Mas estructurado |

```python
import json

# Serializar
datos = {"producto": "Laptop", "precio": 1200.50}
print(json.dumps(datos, indent=2))

# Deserializar
json_str = '{"producto": "Laptop", "precio": 1200.50}'
datos = json.loads(json_str)
print(datos["producto"])
```

Ejecuta: python ejercicios.py 1
