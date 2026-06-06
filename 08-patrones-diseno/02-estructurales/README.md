# Patrones Estructurales

Definen relaciones entre objetos y clases, facilitando que las entidades trabajen juntas.

## Conceptos Basicos

- **Adapter**: convierte la interfaz de una clase en otra interfaz que el cliente espera. Permite que clases incompatibles trabajen juntas.
- **Decorator**: anade responsabilidades a objetos de forma dinamica, sin modificar su codigo.
- **Proxy**: proporciona un sustituto o representante de otro objeto para controlar el acceso a el.

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Adapter** | Traduce una interfaz a otra que el cliente espera |
| **Target** | Interfaz que el cliente espera usar |
| **Adaptee** | Clase existente con interfaz incompatible |
| **Decorator** | Envuelve un objeto para anadirle comportamiento |
| **Wrapper** | Objeto que envuelve a otro para extenderlo |
| **Proxy** | Intermediario que controla el acceso al objeto real |
| **Delegacion** | Pasar la responsabilidad a otro objeto |

## Comparativa entre Lenguajes

### Java (Decorator)
```java
interface Bebida { double costo(); String descripcion(); }
class CafeSimple implements Bebida {
    public double costo() { return 2.0; }
    public String descripcion() { return "Cafe simple"; }
}
abstract class BebidaDecorator implements Bebida {
    protected Bebida bebida;
    public BebidaDecorator(Bebida b) { this.bebida = b; }
}
```

### Python (Decorator)
```python
class CafeSimple:
    def costo(self): return 2.0
    def descripcion(self): return "Cafe simple"

class Leche:
    def __init__(self, bebida): self._bebida = bebida
    def costo(self): return self._bebida.costo() + 0.5
    def descripcion(self): return self._bebida.descripcion() + ", leche"
```

### JavaScript (Decorator)
```javascript
class CafeSimple {
    costo() { return 2.0; }
    descripcion() { return "Cafe simple"; }
}
class Leche {
    constructor(bebida) { this.bebida = bebida; }
    costo() { return this.bebida.costo() + 0.5; }
    descripcion() { return this.bebida.descripcion() + ", leche"; }
}
```

## Ejemplo Guiado: Proxy de control de acceso

Paso 1: Interfaz comun
```java
interface Documento {
    void mostrar();
}
```

Paso 2: Objeto real
```java
class DocumentoReal implements Documento {
    private String contenido;
    public DocumentoReal(String c) { this.contenido = c; }
    public void mostrar() {
        System.out.println("Contenido: " + contenido);
    }
}
```

Paso 3: Proxy que controla acceso
```java
class ProxyDocumento implements Documento {
    private DocumentoReal doc;
    private String usuario;
    private String rol;

    public ProxyDocumento(String contenido, String usuario, String rol) {
        this.doc = new DocumentoReal(contenido);
        this.usuario = usuario;
        this.rol = rol;
    }

    public void mostrar() {
        if ("admin".equalsIgnoreCase(rol)) {
            System.out.println("Acceso concedido a " + usuario);
            doc.mostrar();
        } else {
            System.out.println("Acceso DENEGADO para " + usuario);
        }
    }
}
```

Paso 4: Uso
```java
new ProxyDocumento("Secreto", "Juan", "admin").mostrar();    // OK
new ProxyDocumento("Secreto", "Pedro", "invitado").mostrar(); // DENEGADO
```

## Referencia rapida

| Patron | Problema que resuelve | Estructura clave |
|--------|----------------------|------------------|
| **Adapter** | Interfaz incompatible entre clases | Envuelve el Adaptee implementando la interfaz Target |
| **Decorator** | Anadir funcionalidad dinamicamente | Envuelve el objeto original, anadiendo comportamiento |
| **Proxy** | Controlar acceso a un objeto | Implementa la misma interfaz y delega al objeto real |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 8 2 [ejercicio] [-p N]`

1. 🟢 **Adapter - convertir interfaz EnchufeEuropeo a EnchufeAmericano**
2. 🟡 **Decorator - agregar extras a Cafe (Leche, Azucar)**
3. 🟡 **Proxy - control de acceso a Documento**
