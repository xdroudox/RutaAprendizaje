# Patrones Estructurales

Los patrones estructurales explican como ensamblar objetos y clases en estructuras mas grandes, manteniendo flexibilidad y eficiencia.

## Adapter

**Intencion:** Convertir la interfaz de una clase en otra interfaz que el cliente espera. Permite que clases con interfaces incompatibles trabajen juntas.

**Problema:** Tienes una clase existente con una interfaz que no coincide con la que necesita tu sistema.

**Estructura:**
- Target (interfaz que el cliente espera)
- Adaptee (clase existente con interfaz incompatible)
- Adapter (convierte la interfaz del Adaptee al Target)

**Cuando usar:**
- Cuando quieres usar una clase existente pero su interfaz no es compatible
- Cuando quieres crear una clase reutilizable que coopere con clases no relacionadas

**Ejemplo:**
```java
interface ConectorEU { void conectar(); }
class EnchufeEU implements ConectorEU {
    public void conectar() { System.out.println("Conectado a 220V"); }
}
interface ConectorUS { void plugIn(); }
class AdaptadorEUaUS implements ConectorUS {
    private ConectorEU enchufe;
    public AdaptadorEUaUS(ConectorEU e) { this.enchufe = e; }
    public void plugIn() { enchufe.conectar(); }
}
```

## Decorator

**Intencion:** Anadir responsabilidades adicionales a un objeto de forma dinamica. Proporciona una alternativa flexible a la herencia para extender funcionalidad.

**Problema:** Necesitas anadir funcionalidad a objetos individuales, no a toda la clase.

**Estructura:**
- Component (interfaz base)
- ConcreteComponent (objeto base al que anadir funcionalidad)
- Decorator (mantiene referencia al Component y anade comportamiento)
- ConcreteDecorators (implementaciones especificas)

**Cuando usar:**
- Para anadir responsabilidades a objetos individualmente sin afectar a otros
- Cuando la herencia no es practica por la cantidad de combinaciones

**Ejemplo:**
```java
interface Cafe { double costo(); String descripcion(); }
class CafeSimple implements Cafe {
    public double costo() { return 2.0; }
    public String descripcion() { return "Cafe simple"; }
}
abstract class CafeDecorator implements Cafe {
    protected Cafe cafe;
    public CafeDecorator(Cafe c) { this.cafe = c; }
}
class Leche extends CafeDecorator {
    public Leche(Cafe c) { super(c); }
    public double costo() { return cafe.costo() + 0.5; }
    public String descripcion() { return cafe.descripcion() + ", leche"; }
}
```

## Proxy

**Intencion:** Proporcionar un sustituto o representante de otro objeto para controlar el acceso a el.

**Problema:** Necesitas controlar el acceso a un objeto, ya sea por seguridad, pereza (lazy loading), o logging.

**Estructura:**
- Subject (interfaz comun)
- RealSubject (objeto real)
- Proxy (controla el acceso al RealSubject)

**Cuando usar:**
- Control de acceso a recursos sensibles
- Inicializacion perezosa de objetos pesados
- Logging o auditoria de operaciones

**Ejemplo:**
```java
interface Acceso { void acceder(String usuario); }
class AccesoReal implements Acceso {
    public void acceder(String u) { System.out.println(u + " accedio"); }
}
class ProxyAcceso implements Acceso {
    private AccesoReal real = new AccesoReal();
    public void acceder(String usuario) {
        if (usuario.equals("admin")) {
            real.acceder(usuario);
        } else {
            System.out.println("Acceso denegado a " + usuario);
        }
    }
}
```

## Facade

**Intencion:** Proporcionar una interfaz simplificada a un conjunto de interfaces de un subsistema.

**Problema:** Un sistema complejo con muchas clases dificiles de usar requiere una interfaz sencilla.

**Cuando usar:**
- Cuando quieres proporcionar una interfaz simple a un subsistema complejo
- Cuando quieres desacoplar el cliente del subsistema

## Ejecuta

```
javac Ejercicios.java && java Ejercicios 1
javac Ejercicios.java && java Ejercicios 1 -p
javac Ejercicios.java && java Ejercicios -s 1
```
