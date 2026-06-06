/**
 * SOLUCIONES - MVC, Repository e Inyeccion de Dependencias
 * Ejecuta desde raiz: python scripts/runner.py 8 4 [ejercicio] -s
 */
public class Soluciones {
    public static void main(String[] args) {
        if (args.length > 0 && args[0].matches("\\d+")) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
            }
        } else {
            for (int i = 1; i <= 3; i++) {
                System.out.println("  " + i + ". [Solucion " + i + "]");
            }
        }
    }

    static void solucion_1() {
        System.out.println(">> SOLUCION 1: MVC basico");
        System.out.println("-".repeat(40));

        class Usuario {
            private int id;
            private String nombre;
            private String email;
            public Usuario(int id, String nombre, String email) {
                this.id = id; this.nombre = nombre; this.email = email;
            }
            public int getId() { return id; }
            public String getNombre() { return nombre; }
            public String getEmail() { return email; }
            public String toString() {
                return id + " - " + nombre + " (" + email + ")";
            }
        }

        class RepositorioUsuarios {
            private java.util.Map<Integer, Usuario> datos = new java.util.HashMap<>();
            private int contador = 1;
            public Usuario guardar(String nombre, String email) {
                Usuario u = new Usuario(contador++, nombre, email);
                datos.put(u.getId(), u);
                return u;
            }
            public java.util.List<Usuario> listar() {
                return new java.util.ArrayList<>(datos.values());
            }
        }

        class ControladorUsuario {
            private RepositorioUsuarios repo = new RepositorioUsuarios();
            public void crearUsuario(String nombre, String email) {
                Usuario u = repo.guardar(nombre, email);
                System.out.println("Creado: " + u);
            }
            public void listarUsuarios() {
                for (Usuario u : repo.listar()) {
                    System.out.println(u);
                }
            }
        }

        ControladorUsuario ctrl = new ControladorUsuario();
        ctrl.crearUsuario("Ana", "ana@test.com");
        ctrl.crearUsuario("Luis", "luis@test.com");
        ctrl.listarUsuarios();
    }

    static void solucion_2() {
        System.out.println(">> SOLUCION 2: Vista simple");
        System.out.println("-".repeat(40));

        class Usuario {
            private String nombre;
            private String email;
            public Usuario(String n, String e) { this.nombre = n; this.email = e; }
            public String getNombre() { return nombre; }
            public String getEmail() { return email; }
        }

        interface VistaUsuario {
            void mostrar(Usuario u);
            void mostrarTodos(java.util.List<Usuario> lista);
        }

        class VistaConsola implements VistaUsuario {
            public void mostrar(Usuario u) {
                System.out.println("Nombre: " + u.getNombre());
                System.out.println("Email: " + u.getEmail());
                System.out.println("-".repeat(20));
            }
            public void mostrarTodos(java.util.List<Usuario> lista) {
                for (Usuario u : lista) mostrar(u);
            }
        }

        VistaConsola vista = new VistaConsola();
        vista.mostrar(new Usuario("Maria", "maria@test.com"));
    }

    static void solucion_3() {
        System.out.println(">> SOLUCION 3: Inyeccion de Dependencias");
        System.out.println("-".repeat(40));

        interface RepositorioUsuario {
            void guardar(String nombre, String email);
            java.util.List<String> listarNombres();
        }

        class RepositorioMemoria implements RepositorioUsuario {
            private java.util.List<String> nombres = new java.util.ArrayList<>();
            public void guardar(String nombre, String email) { nombres.add(nombre); }
            public java.util.List<String> listarNombres() { return nombres; }
        }

        class ServicioUsuario {
            private RepositorioUsuario repo;
            public ServicioUsuario(RepositorioUsuario repo) { this.repo = repo; }
            public void registrar(String nombre, String email) {
                repo.guardar(nombre, email);
                System.out.println("Usuario registrado: " + nombre);
            }
            public void listar() {
                System.out.println("Usuarios: " + repo.listarNombres());
            }
        }

        RepositorioUsuario repo = new RepositorioMemoria();
        ServicioUsuario servicio = new ServicioUsuario(repo);
        servicio.registrar("Carlos", "carlos@test.com");
        servicio.registrar("Diana", "diana@test.com");
        servicio.listar();
        System.out.println("DI funciona: ServicioUsuario usa RepositorioMemoria");
    }
}
