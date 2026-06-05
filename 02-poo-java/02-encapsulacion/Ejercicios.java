/**
 * EJERCICIOS - Encapsulacion
 * Ejecuta desde raiz: python scripts/runner.py 2 2 [ejercicio]
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
            System.out.println("1. Clase CuentaBancaria con saldo private y validacion");
            System.out.println("2. Clase Producto con precio private que rechace negativos");
            System.out.println("3. Clase Estudiante con notas private y promedio()");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: CuentaBancaria");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase CuentaBancaria con atributo saldo (private double).");
        System.out.println("Incluye getSaldo() que retorne el saldo.");
        System.out.println("Incluye setSaldo(double) que solo acepte valores mayores o iguales a 0.");
        System.out.println("Si el valor es negativo, imprime \"Error: saldo no puede ser negativo\".");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Producto");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Producto con atributo precio (private double).");
        System.out.println("Incluye getPrecio() y setPrecio(double).");
        System.out.println("El setter debe rechazar precios negativos imprimiendo un mensaje.");
        System.out.println("Incluye un constructor que reciba nombre y precio.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Estudiante");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Estudiante con atributo notas (private double[]).");
        System.out.println("Incluye un constructor que reciba el array de notas.");
        System.out.println("Incluye getNotas() y setNotas(double[]).");
        System.out.println("Incluye metodo promedio() que calcule la media de las notas.");
        System.out.println("En el main, crea un estudiante con notas {7.5, 8.0, 6.5} y muestra su promedio.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
