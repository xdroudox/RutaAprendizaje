# Patrones de Comportamiento

Gestionan algoritmos y responsabilidades entre objetos, definiendo como se comunican.

## Conceptos Basicos

- **Observer**: define una dependencia uno-a-muchos entre objetos, de modo que cuando uno cambia su estado, todos sus dependientes son notificados.
- **Strategy**: define una familia de algoritmos intercambiables en tiempo de ejecucion.
- **Template Method**: define el esqueleto de un algoritmo en un metodo, delegando pasos a subclases.

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Observer** | Patron de suscripcion/notificacion entre objetos |
| **Subject** | Objeto que mantiene la lista de observadores y los notifica |
| **Suscriptor** | Objeto que recibe notificaciones del sujeto |
| **Strategy** | Algoritmo intercambiable encapsulado en una clase |
| **Contexto** | Clase que usa una estrategia sin conocer su implementacion |
| **Template Method** | Metodo plantilla con pasos abstractos |
| **Hook** | Metodo opcional que las subclases pueden sobrescribir |

## Comparativa entre Lenguajes

### Java (Observer)
```java
interface Suscriptor { void notificar(String noticia); }
class Editorial {
    private List<Suscriptor> suscriptores = new ArrayList<>();
    public void suscribir(Suscriptor s) { suscriptores.add(s); }
    public void publicar(String noticia) {
        for (Suscriptor s : suscriptores) s.notificar(noticia);
    }
}
```

### Python (Observer)
```python
class Editorial:
    def __init__(self):
        self._suscriptores = []
    def suscribir(self, s):
        self._suscriptores.append(s)
    def publicar(self, noticia):
        for s in self._suscriptores:
            s.notificar(noticia)
```

### JavaScript (Observer)
```javascript
class Editorial {
    constructor() { this.suscriptores = []; }
    suscribir(s) { this.suscriptores.push(s); }
    publicar(noticia) { this.suscriptores.forEach(s => s.notificar(noticia)); }
}
```

## Ejemplo Guiado: Strategy para ordenamiento

Paso 1: Definir la interfaz de estrategia
```java
interface EstrategiaOrdenamiento {
    void ordenar(int[] arr);
}
```

Paso 2: Implementar estrategias concretas
```java
class BubbleSort implements EstrategiaOrdenamiento {
    public void ordenar(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++)
            for (int j = 0; j < arr.length - i - 1; j++)
                if (arr[j] > arr[j + 1]) {
                    int tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                }
    }
}

class QuickSort implements EstrategiaOrdenamiento {
    public void ordenar(int[] arr) {
        java.util.Arrays.sort(arr);
    }
}
```

Paso 3: Contexto que usa la estrategia
```java
class Contexto {
    private EstrategiaOrdenamiento estrategia;

    public void setEstrategia(EstrategiaOrdenamiento e) {
        this.estrategia = e;
    }

    public void ejecutar(int[] arr) {
        estrategia.ordenar(arr);
    }
}
```

Paso 4: Uso
```java
int[] datos = {5, 2, 8, 1, 9};
Contexto ctx = new Contexto();
ctx.setEstrategia(new BubbleSort());  // Cambia en tiempo real
ctx.ejecutar(datos);
```

## Referencia rapida

| Patron | Problema que resuelve | Estructura clave |
|--------|----------------------|------------------|
| **Observer** | Notificar a multiples objetos cuando algo cambia | Subject mantiene lista de Observers y los notifica |
| **Strategy** | Algoritmos intercambiables en tiempo de ejecucion | Interface comun + Contexto que la usa |
| **Template Method** | Esqueleto de algoritmo con pasos variables | Metodo final + metodos abstractos |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 8 3 [ejercicio] [-p N]`

1. 🟢 **Observer - suscriptores reciben noticias de una Editorial**
2. 🟡 **Strategy - ordenar lista con diferentes estrategias**
3. 🟡 **Template Method - procesar datos con plantilla**
