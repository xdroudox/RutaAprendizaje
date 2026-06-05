import java.util.*;

public class Ejercicios {
    public static void main(String[] args) {
        if (args.length == 0) {
            menu();
        } else if (args[0].equals("-s") && args.length > 1) {
            mostrarSolucion(Integer.parseInt(args[1]));
        } else {
            int num = Integer.parseInt(args[0]);
            if (args.length > 1 && args[1].equals("-p")) {
                mostrarPista(num);
            } else {
                ejecutarEjercicio(num);
            }
        }
    }

    static void menu() {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("=== MENU - Colecciones y Genericos ===");
            System.out.println("1. ArrayList de estudiantes");
            System.out.println("2. HashMap de contactos");
            System.out.println("3. Clase generica Par");
            System.out.println("0. Salir");
            System.out.print("Selecciona un ejercicio: ");
            String opt = sc.nextLine();
            if (opt.equals("0")) break;
            try {
                int n = Integer.parseInt(opt);
                ejecutarEjercicio(n);
            } catch (NumberFormatException e) {
                System.out.println("Opcion invalida");
            }
        }
        sc.close();
    }

    static void ejecutarEjercicio(int n) {
        switch (n) {
            case 1: ejercicio_1(); break;
            case 2: ejercicio_2(); break;
            case 3: ejercicio_3(); break;
            default: System.out.println("Ejercicio no encontrado");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: ArrayList de estudiantes");
        System.out.println("Crea un programa que gestione una lista de estudiantes.");
        System.out.println("Cada estudiante tiene nombre y nota.");
        System.out.println("Usa ArrayList. Implementa:");
        System.out.println("  - Agregar estudiante");
        System.out.println("  - Listar todos");
        System.out.println("  - Calcular promedio de notas");
        System.out.println("  - Mostrar el de mayor nota");
        System.out.println();
        System.out.println("PISTA: 'ArrayList<Estudiante> lista = new ArrayList<>();'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: HashMap de contactos");
        System.out.println("Crea una agenda telefonica con HashMap<String, String>.");
        System.out.println("Implementa:");
        System.out.println("  - Anadir contacto (nombre, telefono)");
        System.out.println("  - Buscar por nombre");
        System.out.println("  - Eliminar contacto");
        System.out.println("  - Listar todos");
        System.out.println();
        System.out.println("PISTA: 'HashMap<String, String> agenda = new HashMap<>();'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Clase generica Par");
        System.out.println("Crea una clase generica Par<K, V> con:");
        System.out.println("  - getClave(), setClave(K clave)");
        System.out.println("  - getValor(), setValor(V valor)");
        System.out.println("En el main, crea:");
        System.out.println("  - Par<String, Integer> (nombre, edad)");
        System.out.println("  - Par<Integer, String> (id, nombre)");
        System.out.println();
        System.out.println("PISTA: 'public class Par<K, V> { private K clave; private V valor; }'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: Crea clase Estudiante con nombre y nota",
                "Pista 2: Promedio = suma / lista.size()",
                "Pista 3: Usa for-each para recorrer y encontrar el mayor"
            },
            {
                "Pista 1: 'agenda.put(nombre, telefono)' para anadir",
                "Pista 2: 'agenda.get(nombre)' para buscar",
                "Pista 3: 'agenda.remove(nombre)' para eliminar"
            },
            {
                "Pista 1: 'class Par<K, V> { private K clave; private V valor; }'",
                "Pista 2: Constructor: 'public Par(K clave, V valor) { this.clave = clave; this.valor = valor; }'",
                "Pista 3: Getters y setters para clave y valor"
            }
        };
        if (n >= 1 && n <= pistas.length) {
            for (String p : pistas[n - 1]) {
                System.out.println(p);
            }
        }
    }

    static void mostrarSolucion(int n) {
        Soluciones.main(new String[]{String.valueOf(n)});
    }
}
