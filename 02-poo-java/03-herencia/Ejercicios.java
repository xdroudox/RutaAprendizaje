/**
 * EJERCICIOS - Herencia
 * Ejecuta desde raiz: python scripts/runner.py 2 3 [ejercicio]
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
            System.out.println("1. Clase Animal, Perro y Gato con herencia");
            System.out.println("2. Clase Vehiculo, Coche y Bicicleta con herencia");
            System.out.println("3. Clase Empleado, Gerente y Vendedor con herencia");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Animal, Perro y Gato");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Animal con metodo hacerSonido() que imprima \"...\".");
        System.out.println("Crea clase Perro que extienda Animal y sobrescriba hacerSonido()");
        System.out.println("imprimiendo \"Guau!\".");
        System.out.println("Crea clase Gato que extienda Animal y sobrescriba haciendo \"Miau!\".");
        System.out.println("En el main, crea un Perro y un Gato y llama a hacerSonido().");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Vehiculo, Coche y Bicicleta");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Vehiculo con atributo velocidad (int) y metodo");
        System.out.println("mover() que imprima \"El vehiculo se mueve...\".");
        System.out.println("Crea Coche que extienda Vehiculo y sobrescriba mover()");
        System.out.println("imprimiendo \"El coche acelera a \" + velocidad + \" km/h\".");
        System.out.println("Crea Bicicleta que extienda Vehiculo y sobrescriba mover()");
        System.out.println("imprimiendo \"La bicicleta pedalea a \" + velocidad + \" km/h\".");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Empleado, Gerente y Vendedor");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Empleado con atributo nombre y metodo");
        System.out.println("calcularSalario() que retorne 0.0.");
        System.out.println("Crea Gerente que herede de Empleado, con atributo bono,");
        System.out.println("y calcularSalario() retorne 50000 + bono.");
        System.out.println("Crea Vendedor que herede de Empleado, con atributo comision,");
        System.out.println("y calcularSalario() retorne 30000 + comision.");
        System.out.println("En el main, crea un Gerente y un Vendedor y muestra sus salarios.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
