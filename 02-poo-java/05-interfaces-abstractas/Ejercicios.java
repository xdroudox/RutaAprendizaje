/**
 * EJERCICIOS - Interfaces y Clases Abstractas
 * Ejecuta desde raiz: python scripts/runner.py 2 5 [ejercicio]
 */
public class Ejercicios {

    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: ejercicio_1(); break;
                case 2: ejercicio_2(); break;
                case 3: ejercicio_3(); break;
                default: System.out.println("Ejercicio no encontrado");
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("1. Interface Volador, clases Pajaro y Avion");
            System.out.println("2. Clase abstracta Forma con area() abstracto e info() concreto");
            System.out.println("3. Interface Reproducible, clases Musica y Video");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Interface Volador");
        System.out.println("-".repeat(40));
        System.out.println("Crea una interface Volador con metodo volar().");
        System.out.println("Crea clase Pajaro que implemente Volador y en volar()");
        System.out.println("imprima \"El pajaro vuela batiendo alas\".");
        System.out.println("Crea clase Avion que implemente Volador y en volar()");
        System.out.println("imprima \"El avion vuela con motores\".");
        System.out.println("En el main, crea un Pajaro y un Avion y llama a volar().");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Clase abstracta Forma");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase abstracta Forma con:");
        System.out.println("  - Metodo abstracto double area()");
        System.out.println("  - Metodo concreto void info() que imprima \"Soy una forma\"");
        System.out.println("Crea Circulo que herede de Forma e implemente area().");
        System.out.println("Crea Rectangulo que herede de Forma e implemente area().");
        System.out.println("En el main, crea un Circulo y un Rectangulo, muestra area e info().");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Interface Reproducible");
        System.out.println("-".repeat(40));
        System.out.println("Crea una interface Reproducible con metodo reproducir().");
        System.out.println("Crea clase Musica que implemente Reproducible y en reproducir()");
        System.out.println("imprima \"Reproduciendo cancion...\".");
        System.out.println("Crea clase Video que implemente Reproducible y en reproducir()");
        System.out.println("imprima \"Reproduciendo video...\".");
        System.out.println("En el main, usa un array de Reproducible[] para mostrar polimorfismo.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
