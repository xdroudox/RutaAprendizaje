# Patrones Estructurales

Definen relaciones entre objetos y clases.

## Adapter

Convierte una interfaz en otra que el cliente espera.

```java
interface EnchufeAmericano { void plugIn(); }
class Adaptador implements EnchufeAmericano {
    private EnchufeEuropeo e;
    public void plugIn() { e.conectar(); }
}
```

## Decorator

Anade responsabilidades a objetos dinamicamente.

```java
Bebida cafe = new Leche(new Azucar(new CafeSimple()));
```

## Proxy

Controla el acceso a un objeto.

```java
class ProxyDocumento implements Documento {
    public void mostrar() {
        if ("admin".equals(rol)) doc.mostrar();
        else System.out.println("Acceso denegado");
    }
}
```

## Ejercicios

1. **Adapter - convertir interfaz EnchufeEuropeo a EnchufeAmericano**
   **Ejecuta:** `python scripts/runner.py 8 2 1`

2. **Decorator - agregar extras a Cafe (Leche, Azucar)**
   **Ejecuta:** `python scripts/runner.py 8 2 2`

3. **Proxy - control de acceso a Documento**
   **Ejecuta:** `python scripts/runner.py 8 2 3`
