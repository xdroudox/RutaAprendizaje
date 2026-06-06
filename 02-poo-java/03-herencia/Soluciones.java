/**
 * SOLUCIONES - Herencia (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 3 [ejercicio] -s
 */
public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Ejercicio no encontrado");
            }
        } else {
            System.out.println("SOLUCIONES:");
            System.out.println("  🟢 1. Animal, Perro y Gato");
            System.out.println("  🟡 2. Vehiculo, Coche y Bicicleta");
            System.out.println("  🔴 3. Empleado, Gerente y Vendedor");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: Animal, Perro y Gato");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Animal {
    void hacerSonido() {
        System.out.println("...");
    }
}

class Perro extends Animal {
    @Override
    void hacerSonido() {
        System.out.println("Guau!");
    }
}

class Gato extends Animal {
    @Override
    void hacerSonido() {
        System.out.println("Miau!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal perro = new Perro();
        Animal gato = new Gato();

        perro.hacerSonido();  // Guau!
        gato.hacerSonido();   // Miau!
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `class Perro extends Animal` — Perro HEREDA de Animal.
   Tiene automaticamente el metodo hacerSonido() de Animal.

2. `@Override void hacerSonido()` — SOBRESCRIBIMOS el metodo heredado.
   Ahora Perro.hacerSonido() hace algo DISTINTO a Animal.hacerSonido().

3. `Animal perro = new Perro()` — Variable de tipo Animal, pero objeto
   de tipo Perro. Java ejecuta el metodo del TIPO REAL (Perro), no del
   tipo declarado (Animal). Esto es la base del POLIMORFISMO.

4. `perro.hacerSonido()` — Imprime "Guau!" (el metodo de Perro).
   `gato.hacerSonido()` — Imprime "Miau!" (el metodo de Gato).
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: Vehiculo, Coche y Bicicleta");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Vehiculo {
    int velocidad;

    Vehiculo(int velocidad) {
        this.velocidad = velocidad;
    }

    void mover() {
        System.out.println("El vehiculo se mueve...");
    }
}

class Coche extends Vehiculo {
    Coche(int velocidad) {
        super(velocidad);  // Llama al constructor de Vehiculo
    }

    @Override
    void mover() {
        System.out.println("El coche acelera a " + velocidad + " km/h");
    }
}

class Bicicleta extends Vehiculo {
    Bicicleta(int velocidad) {
        super(velocidad);
    }

    @Override
    void mover() {
        System.out.println("La bicicleta pedalea a " + velocidad + " km/h");
    }
}

public class Main {
    public static void main(String[] args) {
        Vehiculo coche = new Coche(120);
        Vehiculo bici = new Bicicleta(25);

        coche.mover();  // El coche acelera a 120 km/h
        bici.mover();   // La bicicleta pedalea a 25 km/h
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `super(velocidad)` — Llama al CONSTRUCTOR de Vehiculo que recibe un
   int. Si no llamas a super() explicitamente, Java intenta llamar a
   super() sin argumentos y da error si no existe.

2. La subclase HEREDA el atributo `velocidad` de Vehiculo. Puede usarlo
   directamente (como en el println) aunque no lo haya declarado.

3. POLIMORFISMO: Aunque las variables son de tipo Vehiculo, los objetos
   son Coche y Bicicleta. Java ejecuta el metodo del tipo real.
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: Empleado, Gerente y Vendedor");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Empleado {
    String nombre;

    Empleado(String nombre) {
        this.nombre = nombre;
    }

    double calcularSalario() {
        return 0.0;
    }
}

class Gerente extends Empleado {
    double bono;

    Gerente(String nombre, double bono) {
        super(nombre);
        this.bono = bono;
    }

    @Override
    double calcularSalario() {
        return 50000 + bono;
    }
}

class Vendedor extends Empleado {
    double comision;

    Vendedor(String nombre, double comision) {
        super(nombre);
        this.comision = comision;
    }

    @Override
    double calcularSalario() {
        return 30000 + comision;
    }
}

public class Main {
    public static void main(String[] args) {
        Empleado gerente = new Gerente("Ana", 10000);
        Empleado vendedor = new Vendedor("Luis", 5000);

        System.out.println(gerente.nombre + ": $" + gerente.calcularSalario());
        // Ana: $60000.0  (50000 + 10000)
        System.out.println(vendedor.nombre + ": $" + vendedor.calcularSalario());
        // Luis: $35000.0  (30000 + 5000)
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. CADA subclase tiene su PROPIA implementacion de calcularSalario().
   Gerente usa 50000 + bono. Vendedor usa 30000 + comision.

2. CADA subclase agrega sus PROPIOS atributos (bono, comision) ademas
   de heredar nombre de Empleado.

3. `super(nombre)` EN AMBAS subclases — Cada una llama al constructor
   del padre para inicializar el nombre.

4. POLIMORFISMO EN ACCION:
   - gerente.calcularSalario() ejecuta el metodo de Gerente
   - vendedor.calcularSalario() ejecuta el metodo de Vendedor
   - AMBOS son tipo Empleado, pero se comportan diferente
""");
    }
}
