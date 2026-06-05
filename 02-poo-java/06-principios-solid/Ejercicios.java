/**
 * EJERCICIOS - Principios SOLID
 * Ejecuta desde raiz: python scripts/runner.py 2 6 [ejercicio]
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
            System.out.println("1. SRP: Separar Reporte en Reporte + Impresora");
            System.out.println("2. OCP: Sistema de descuentos con interface Descuento");
            System.out.println("3. DIP: Depender de interface BaseDatos, no de implementacion");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: SRP - Single Responsibility Principle");
        System.out.println("-".repeat(40));
        System.out.println("Imagina una clase Reporte que tiene dos responsabilidades:");
        System.out.println("  - Contener los datos del reporte (titulo, contenido)");
        System.out.println("  - Imprimir el reporte en consola");
        System.out.println("Refactoriza separando en dos clases:");
        System.out.println("  - Reporte: solo con atributos titulo y contenido, getters");
        System.out.println("  - Impresora: con metodo estatico imprimir(Reporte r)");
        System.out.println("En el main, crea un Reporte y pasalo a Impresora.imprimir().");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: OCP - Open/Closed Principle");
        System.out.println("-".repeat(40));
        System.out.println("Crea una interface Descuento con metodo double aplicar(double precio).");
        System.out.println("Crea DescuentoPorcentaje que aplique un % de descuento.");
        System.out.println("Crea DescuentoFijo que reste una cantidad fija.");
        System.out.println("Crea clase CalculadoraPrecio con metodo calcular(double precio, Descuento d)");
        System.out.println("que aplique el descuento y retorne el precio final.");
        System.out.println("En el main, prueba ambos descuentos.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: DIP - Dependency Inversion Principle");
        System.out.println("-".repeat(40));
        System.out.println("Crea una interface BaseDatos con metodo void guardar(String dato).");
        System.out.println("Crea BaseDatosMySQL que implemente BaseDatos e imprima");
        System.out.println("\"Guardado en MySQL: \" + dato.");
        System.out.println("Crea BaseDatosArchivo que implemente BaseDatos e imprima");
        System.out.println("\"Guardado en archivo: \" + dato.");
        System.out.println("Crea Servicio que reciba BaseDatos en su constructor");
        System.out.println("y tenga un metodo procesar(String dato) que llame a guardar().");
        System.out.println("En el main, crea un Servicio con cada implementacion.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
