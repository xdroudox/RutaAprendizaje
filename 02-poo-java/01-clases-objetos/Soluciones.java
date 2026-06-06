/**
 * SOLUCIONES - Clases y Objetos (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 1 [ejercicio] -s
 */
public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0 && !args[0].startsWith("-")) {
            int num;
            try {
                num = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Solucion no encontrada");
                return;
            }
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Ejercicio no encontrado. Valores: 1-3");
            }
        } else {
            System.out.println("SOLUCIONES:");
            System.out.println("  🟢 1. Persona con mostrarDatos()");
            System.out.println("  🟡 2. Rectangulo con area()");
            System.out.println("  🔴 3. Libro con esLargo()");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: Clase Persona");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Persona {
    String nombre;
    int edad;

    Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
    }
}

public class Main {
    public static void main(String[] args) {
        Persona p1 = new Persona("Ana", 25);
        Persona p2 = new Persona("Luis", 30);

        p1.mostrarDatos();
        p2.mostrarDatos();
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `class Persona { ... }` — Define la clase. Es el molde para crear personas.

2. `String nombre; int edad;` — Atributos: toda Persona tendra nombre y edad.
   Son variables de INSTANCIA: cada objeto tiene su propia copia.

3. `Persona(String nombre, int edad)` — CONSTRUCTOR: se ejecuta al hacer new.
   - Los parametros tienen el MISMO nombre que los atributos
   - `this.nombre = nombre` diferencia el atributo (`this.nombre`) del parametro (`nombre`)
   - Sin el constructor, hariamos: p.nombre = "Ana" DESPUES de crear el objeto

4. `void mostrarDatos()` — Metodo que USA los atributos del objeto.
   - `nombre` se refiere al atributo del objeto que llamo al metodo
   - Si p1.mostrarDatos(), nombre es "Ana"
   - Si p2.mostrarDatos(), nombre es "Luis"

5. `Persona p1 = new Persona("Ana", 25);` — Crea el objeto en UNA linea.
   - `Persona p1`: declara variable de tipo Persona
   - `new Persona(...)`: reserva memoria, ejecuta el constructor, devuelve referencia
   - `p1` guarda la direccion de memoria del objeto creado
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: Clase Rectangulo");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Rectangulo {
    double base;
    double altura;

    Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    double area() {
        return base * altura;
    }
}

public class Main {
    public static void main(String[] args) {
        Rectangulo r = new Rectangulo(5, 3);
        System.out.println("Area: " + r.area());
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `double area()` — El metodo RETORNA un valor (no es void).
   - `double` indica el tipo de dato que devuelve
   - `return base * altura;` calcula y devuelve el resultado

2. `rectangulo.area()` — Ejecuta el metodo area() en ese objeto.
   - Usa los atributos base(=5) y altura(=3) de ESE objeto
   - Devuelve 15.0 (double)

3. `System.out.println("Area: " + r.area())` — Concatena texto con el resultado.
   - r.area() se evalua PRIMERO, devuelve 15.0
   - Luego se concatena: "Area: " + "15.0" = "Area: 15.0"
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: Clase Libro");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Libro {
    String titulo;
    String autor;
    int paginas;

    Libro(String titulo, String autor, int paginas) {
        this.titulo = titulo;
        this.autor = autor;
        this.paginas = paginas;
    }

    boolean esLargo() {
        return paginas > 300;
    }
}

public class Main {
    public static void main(String[] args) {
        Libro l1 = new Libro("Don Quijote", "Cervantes", 500);
        Libro l2 = new Libro("Platero", "Jimenez", 150);

        System.out.println(l1.titulo + " es largo? " + l1.esLargo());
        System.out.println(l2.titulo + " es largo? " + l2.esLargo());
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `boolean esLargo()` — Retorna true o false.
   - `paginas > 300` es una expresion BOOLEANA
   - Si paginas=500: 500 > 300 = true
   - Si paginas=150: 150 > 300 = false

2. TRES atributos en el constructor:
   - `Libro(... titulo, ... autor, ... paginas)` — orden de parametros IMPORTANTE
   - Debe coincidir con `new Libro("Don Quijote", "Cervantes", 500)`

3. `System.out.println(l1.titulo + " es largo? " + l1.esLargo())`:
   - l1.titulo accede al ATRIBUTO de l1 (Don Quijote)
   - l1.esLargo() ejecuta el METODO de l1 (true)
   - Resultado: "Don Quijote es largo? true"
""");
    }
}
