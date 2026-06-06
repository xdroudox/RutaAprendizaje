# Patrones Creacionales

Controlan el proceso de creacion de objetos, haciendo el sistema independiente de como se crean, componen y representan.

## Conceptos Basicos

- **Singleton**: garantiza que una clase tenga una unica instancia y proporciona un punto de acceso global.
- **Factory Method**: define una interfaz para crear objetos, pero permite que las subclases decidan que clase instanciar.
- **Builder**: separa la construccion de un objeto complejo de su representacion, permitiendo crear diferentes representaciones con el mismo proceso.

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Singleton** | Patron que restringe la creacion de objetos a una unica instancia |
| **Factory** | Metodo o clase que crea objetos sin exponer la logica de creacion |
| **Builder** | Patron que construye objetos complejos paso a paso |
| **Instancia** | Objeto concreto creado a partir de una clase |
| **Constructor privado** | Constructor que solo puede ser llamado desde la misma clase |
| **Fluent Interface** | Estilo que permite encadenar llamadas (`.masa().salsa().build()`) |
| **Inmutabilidad** | Estado que no puede cambiar despues de la creacion del objeto |

## Comparativa entre Lenguajes

### Java (Singleton)
```java
public class Configuracion {
    private static Configuracion instancia;
    private Configuracion() {}
    public static Configuracion getInstance() {
        if (instancia == null) instancia = new Configuracion();
        return instancia;
    }
}
```

### Python (Singleton)
```python
class Configuracion:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
```

### JavaScript (Singleton)
```javascript
class Configuracion {
    static instancia;
    constructor() {
        if (Configuracion.instancia) return Configuracion.instancia;
        Configuracion.instancia = this;
    }
}
```

## Ejemplo Guiado: Factory de Figuras

Paso 1: Definir la interfaz comun
```java
interface Figura {
    void dibujar();
}
```

Paso 2: Implementar las clases concretas
```java
class Circulo implements Figura {
    public void dibujar() {
        System.out.println("Dibujando Circulo");
    }
}

class Cuadrado implements Figura {
    public void dibujar() {
        System.out.println("Dibujando Cuadrado");
    }
}
```

Paso 3: Crear la Factory
```java
class FiguraFactory {
    public static Figura crearFigura(String tipo) {
        if (tipo.equalsIgnoreCase("circulo")) return new Circulo();
        if (tipo.equalsIgnoreCase("cuadrado")) return new Cuadrado();
        throw new IllegalArgumentException("Figura desconocida: " + tipo);
    }
}
```

Paso 4: Usar la Factory
```java
Figura f1 = FiguraFactory.crearFigura("circulo");
Figura f2 = FiguraFactory.crearFigura("cuadrado");
f1.dibujar();  // "Dibujando Circulo"
f2.dibujar();  // "Dibujando Cuadrado"
```

## Referencia rapida

| Patron | Problema que resuelve | Estructura clave |
|--------|----------------------|------------------|
| **Singleton** | Una unica instancia global | Constructor privado + getInstance() estatico |
| **Factory** | Crear objetos sin saber su clase concreta | Metodo estatico que retorna la interfaz |
| **Builder** | Construir objetos con muchos atributos opcionales | Clase interna Builder con metodos fluent + build() |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 8 1 [ejercicio] [-p N]`

1. 🟢 **Singleton - clase Configuracion con instancia unica**
2. 🟡 **Factory - crear figuras (Circulo, Cuadrado) segun tipo**
3. 🟡 **Builder - construir Pizza con pasos (masa, salsa, ingredientes)**
