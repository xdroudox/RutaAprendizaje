import java.util.Scanner;

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
        int opcion;
        do {
            System.out.println("=== MVC, REPOSITORY e INYECCION DE DEPENDENCIAS ===");
            System.out.println("1. MVC - Gestion de Usuarios");
            System.out.println("2. Repository - Abstraccion de Datos");
            System.out.println("3. Inyeccion de Dependencias - Integracion");
            System.out.println("0. Salir");
            System.out.print("Selecciona un ejercicio: ");
            opcion = sc.nextInt();
            if (opcion > 0 && opcion <= 3) {
                ejecutarEjercicio(opcion);
            }
        } while (opcion != 0);
        sc.close();
    }

    static void ejecutarEjercicio(int n) {
        switch (n) {
            case 1: ejercicio_1(); break;
            case 2: ejercicio_2(); break;
            case 3: ejercicio_3(); break;
            default: System.out.println("Ejercicio no valido");
        }
    }

    // MVC - Gestion de Usuarios
    static void ejercicio_1() {
        System.out.println("=== EJERCICIO 1: MVC - Gestion de Usuarios ===");
        System.out.println("Implementa una aplicacion MVC simple para gestionar");
        System.out.println("usuarios con operaciones CRUD desde consola.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Clase Usuario (Modelo) con id, nombre y email");
        System.out.println("- Interface VistaUsuario con metodos mostrarUsuario(),");
        System.out.println("  mostrarTodos(), mostrarMenu(), obtenerDatos()");
        System.out.println("- Clase ControladorUsuario que coordina modelo y vista");
        System.out.println("- El controlador maneja: crear, listar, buscar, eliminar");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 1 -p'");
    }

    // Repository - Abstraccion de Datos
    static void ejercicio_2() {
        System.out.println("=== EJERCICIO 2: Repository - Abstraccion de Datos ===");
        System.out.println("Anade una capa de repositorio al sistema anterior.");
        System.out.println("Implementa un repositorio en memoria generico.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Interface RepositorioUsuario con CRUD (crear, obtener,");
        System.out.println("  listar, actualizar, eliminar)");
        System.out.println("- Clase RepositorioUsuarioMemoria que implemente la interfaz");
        System.out.println("- Usar HashMap<Integer, Usuario> para almacenamiento");
        System.out.println("- El controlador ahora recibe el repositorio por constructor");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 2 -p'");
    }

    // Inyeccion de Dependencias - Integracion
    static void ejercicio_3() {
        System.out.println("=== EJERCICIO 3: Inyeccion de Dependencias ===");
        System.out.println("Integra todo usando inyeccion de dependencias.");
        System.out.println("El controlador recibe el repositorio y la vista por");
        System.out.println("constructor (Constructor Injection).");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- ControladorUsuario recibe RepositorioUsuario y");
        System.out.println("  VistaUsuario como dependencias inyectadas");
        System.out.println("- Crear una clase Aplicacion que ensamble las dependencias");
        System.out.println("- Demostrar que se puede cambiar la implementacion de");
        System.out.println("  la vista (ej: VistaConsola, VistaResumida)");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 3 -p'");
    }

    static void mostrarPista(int n) {
        String[] pistas = {
            "",
            "PISTA 1: Usuario = (int id, String nombre, String email). " +
            "ControladorUsuario tiene Scanner, lista de usuarios y VistaUsuario. " +
            "VistaUsuario es una interfaz con metodos: mostrarUsuario(Usuario), " +
            "mostrarMenu(), pedirDatos(). Implementa VistaConsola.",
            "PISTA 2: Interface RepositorioUsuario con metodos: " +
            "save(Usuario), findById(int), findAll(), update(Usuario), deleteById(int). " +
            "RepositorioUsuarioMemoria usa HashMap. " +
            "ControladorUsuario ahora recibe RepositorioUsuario en el constructor.",
            "PISTA 3: Crea interface VistaUsuario y dos implementaciones: " +
            "VistaConsola (detallada) y VistaResumida (solo nombres). " +
            "ControladorUsuario constructor(RepositorioUsuario repo, VistaUsuario vista). " +
            "Clase Aplicacion crea las dependencias y las inyecta."
        };
        if (n >= 1 && n <= 3) {
            System.out.println(pistas[n]);
        }
    }

    static void mostrarSolucion(int n) {
        if (n >= 1 && n <= 3) {
            Soluciones.main(new String[]{String.valueOf(n)});
        }
    }
}
