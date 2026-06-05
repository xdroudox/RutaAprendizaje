import java.util.*;

public class Soluciones {
    public static void main(String[] args) {
        if (args.length == 0) {
            for (int i = 1; i <= 3; i++) {
                System.out.println("--- Solucion " + i + " ---");
                ejecutarSolucion(i);
                System.out.println();
            }
        } else {
            int num = Integer.parseInt(args[0]);
            ejecutarSolucion(num);
        }
    }

    static void ejecutarSolucion(int n) {
        switch (n) {
            case 1: solucion_1(); break;
            case 2: solucion_2(); break;
            case 3: solucion_3(); break;
            default: System.out.println("Solucion no valida");
        }
    }

    // ============================================================
    // CLASES COMPARTIDAS (Modelo)
    // ============================================================
    static class Usuario {
        private int id;
        private String nombre;
        private String email;

        public Usuario(int id, String nombre, String email) {
            this.id = id;
            this.nombre = nombre;
            this.email = email;
        }

        public int getId() { return id; }
        public String getNombre() { return nombre; }
        public String getEmail() { return email; }
        public void setNombre(String nombre) { this.nombre = nombre; }
        public void setEmail(String email) { this.email = email; }

        @Override
        public String toString() {
            return "Usuario{id=" + id + ", nombre='" + nombre + "', email='" + email + "'}";
        }
    }

    // ============================================================
    // SOLUCION 1: MVC - Gestion de Usuarios
    // ============================================================
    interface VistaUsuario {
        void mostrarUsuario(Usuario u);
        void mostrarTodos(List<Usuario> usuarios);
        int mostrarMenu(Scanner sc);
        String[] pedirDatos(Scanner sc);
        void mostrarMensaje(String msg);
    }

    static class VistaConsola implements VistaUsuario {
        public void mostrarUsuario(Usuario u) {
            System.out.println("ID: " + u.getId());
            System.out.println("Nombre: " + u.getNombre());
            System.out.println("Email: " + u.getEmail());
            System.out.println("------------------------");
        }

        public void mostrarTodos(List<Usuario> usuarios) {
            if (usuarios.isEmpty()) {
                System.out.println("No hay usuarios registrados.");
                return;
            }
            for (Usuario u : usuarios) {
                mostrarUsuario(u);
            }
        }

        public int mostrarMenu(Scanner sc) {
            System.out.println("--- Gestion de Usuarios MVC ---");
            System.out.println("1. Crear usuario");
            System.out.println("2. Listar usuarios");
            System.out.println("3. Buscar usuario por ID");
            System.out.println("4. Eliminar usuario");
            System.out.println("0. Salir");
            System.out.print("Opcion: ");
            return sc.nextInt();
        }

        public String[] pedirDatos(Scanner sc) {
            sc.nextLine();
            System.out.print("Nombre: ");
            String nombre = sc.nextLine();
            System.out.print("Email: ");
            String email = sc.nextLine();
            return new String[]{nombre, email};
        }

        public void mostrarMensaje(String msg) {
            System.out.println(msg);
        }
    }

    static class ControladorUsuario {
        private List<Usuario> usuarios = new ArrayList<>();
        private VistaUsuario vista;
        private int nextId = 1;

        public ControladorUsuario(VistaUsuario vista) {
            this.vista = vista;
        }

        public void iniciar() {
            Scanner sc = new Scanner(System.in);
            int opcion;
            do {
                opcion = vista.mostrarMenu(sc);
                switch (opcion) {
                    case 1: crearUsuario(sc); break;
                    case 2: listarUsuarios(); break;
                    case 3: buscarUsuario(sc); break;
                    case 4: eliminarUsuario(sc); break;
                }
            } while (opcion != 0);
            sc.close();
        }

        private void crearUsuario(Scanner sc) {
            String[] datos = vista.pedirDatos(sc);
            Usuario u = new Usuario(nextId++, datos[0], datos[1]);
            usuarios.add(u);
            vista.mostrarMensaje("Usuario creado: " + u.getNombre());
        }

        private void listarUsuarios() {
            vista.mostrarTodos(usuarios);
        }

        private void buscarUsuario(Scanner sc) {
            System.out.print("ID del usuario: ");
            int id = sc.nextInt();
            for (Usuario u : usuarios) {
                if (u.getId() == id) {
                    vista.mostrarUsuario(u);
                    return;
                }
            }
            vista.mostrarMensaje("Usuario no encontrado.");
        }

        private void eliminarUsuario(Scanner sc) {
            System.out.print("ID del usuario a eliminar: ");
            int id = sc.nextInt();
            Iterator<Usuario> it = usuarios.iterator();
            while (it.hasNext()) {
                if (it.next().getId() == id) {
                    it.remove();
                    vista.mostrarMensaje("Usuario eliminado.");
                    return;
                }
            }
            vista.mostrarMensaje("Usuario no encontrado.");
        }
    }

    static void solucion_1() {
        System.out.println("IMPLEMENTACION: MVC - Gestion de Usuarios");
        System.out.println("=========================================");
        System.out.println("""
    // Modelo: Usuario (id, nombre, email)
    // Vista: VistaUsuario (interfaz) y VistaConsola (implementacion)
    // Controlador: ControladorUsuario (maneja la logica)
    
    class ControladorUsuario {
        private List<Usuario> usuarios;
        private VistaUsuario vista;
        
        public void iniciar() {
            // loop menu: crear, listar, buscar, eliminar
        }
    }
        """);
        System.out.println("DEMOSTRACION:");
        System.out.println("(Ejecucion automatica con datos de prueba)");
        VistaUsuario vista = new VistaConsola();
        ControladorUsuario ctrl = new ControladorUsuario(vista);

        // Simular creacion de usuarios
        Usuario u1 = new Usuario(1, "Juan Perez", "juan@email.com");
        Usuario u2 = new Usuario(2, "Maria Lopez", "maria@email.com");
        ctrl.getClass().getDeclaredFields(); // placeholder, demo manual

        System.out.println("Usuarios creados:");
        vista.mostrarUsuario(u1);
        vista.mostrarUsuario(u2);
        System.out.println("Para interactuar, ejecuta Ejercicios 1");
    }

    // ============================================================
    // SOLUCION 2: Repository - Abstraccion de Datos
    // ============================================================
    interface RepositorioUsuario {
        Usuario save(Usuario u);
        Optional<Usuario> findById(int id);
        List<Usuario> findAll();
        Usuario update(Usuario u);
        boolean deleteById(int id);
    }

    static class RepositorioUsuarioMemoria implements RepositorioUsuario {
        private Map<Integer, Usuario> almacen = new HashMap<>();
        private int contador = 1;

        public Usuario save(Usuario u) {
            Usuario nuevo = new Usuario(contador++, u.getNombre(), u.getEmail());
            almacen.put(nuevo.getId(), nuevo);
            return nuevo;
        }

        public Optional<Usuario> findById(int id) {
            return Optional.ofNullable(almacen.get(id));
        }

        public List<Usuario> findAll() {
            return new ArrayList<>(almacen.values());
        }

        public Usuario update(Usuario u) {
            if (almacen.containsKey(u.getId())) {
                almacen.put(u.getId(), u);
                return u;
            }
            return null;
        }

        public boolean deleteById(int id) {
            return almacen.remove(id) != null;
        }
    }

    static class ControladorUsuarioRepo {
        private RepositorioUsuario repo;
        private VistaUsuario vista;

        public ControladorUsuarioRepo(RepositorioUsuario repo, VistaUsuario vista) {
            this.repo = repo;
            this.vista = vista;
        }

        public void iniciar() {
            Scanner sc = new Scanner(System.in);
            int opcion;
            do {
                opcion = vista.mostrarMenu(sc);
                switch (opcion) {
                    case 1: crearUsuario(sc); break;
                    case 2: listarUsuarios(); break;
                    case 3: buscarUsuario(sc); break;
                    case 4: eliminarUsuario(sc); break;
                }
            } while (opcion != 0);
            sc.close();
        }

        private void crearUsuario(Scanner sc) {
            String[] datos = vista.pedirDatos(sc);
            Usuario u = new Usuario(0, datos[0], datos[1]);
            Usuario creado = repo.save(u);
            vista.mostrarMensaje("Usuario creado con ID " + creado.getId());
        }

        private void listarUsuarios() {
            vista.mostrarTodos(repo.findAll());
        }

        private void buscarUsuario(Scanner sc) {
            System.out.print("ID: ");
            int id = sc.nextInt();
            Optional<Usuario> opt = repo.findById(id);
            if (opt.isPresent()) {
                vista.mostrarUsuario(opt.get());
            } else {
                vista.mostrarMensaje("Usuario no encontrado.");
            }
        }

        private void eliminarUsuario(Scanner sc) {
            System.out.print("ID a eliminar: ");
            int id = sc.nextInt();
            if (repo.deleteById(id)) {
                vista.mostrarMensaje("Usuario eliminado.");
            } else {
                vista.mostrarMensaje("Usuario no encontrado.");
            }
        }
    }

    static void solucion_2() {
        System.out.println("IMPLEMENTACION: Repository - Abstraccion de Datos");
        System.out.println("================================================");
        System.out.println("""
    interface RepositorioUsuario {
        Usuario save(Usuario u);
        Optional<Usuario> findById(int id);
        List<Usuario> findAll();
        Usuario update(Usuario u);
        boolean deleteById(int id);
    }
    
    class RepositorioUsuarioMemoria implements RepositorioUsuario {
        private Map<Integer, Usuario> almacen = new HashMap<>();
        // Implementacion de metodos CRUD con HashMap
    }
    
    class ControladorUsuarioRepo {
        private RepositorioUsuario repo;
        private VistaUsuario vista;
        
        public ControladorUsuarioRepo(RepositorioUsuario r, VistaUsuario v) {
            this.repo = r;
            this.vista = v;
        }
    }
        """);
        System.out.println("DEMOSTRACION:");
        RepositorioUsuario repo = new RepositorioUsuarioMemoria();
        Usuario u1 = repo.save(new Usuario(0, "Juan", "juan@email.com"));
        Usuario u2 = repo.save(new Usuario(0, "Maria", "maria@email.com"));
        System.out.println("Usuarios en repositorio:");
        for (Usuario u : repo.findAll()) {
            System.out.println(u);
        }
    }

    // ============================================================
    // SOLUCION 3: Inyeccion de Dependencias
    // ============================================================
    static class VistaResumida implements VistaUsuario {
        public void mostrarUsuario(Usuario u) {
            System.out.println(u.getId() + " - " + u.getNombre());
        }

        public void mostrarTodos(List<Usuario> usuarios) {
            if (usuarios.isEmpty()) {
                System.out.println("Sin usuarios.");
                return;
            }
            for (Usuario u : usuarios) {
                mostrarUsuario(u);
            }
        }

        public int mostrarMenu(Scanner sc) {
            System.out.println("1.Crear 2.Listar 3.Buscar 4.Eliminar 0.Salir");
            System.out.print("Opcion: ");
            return sc.nextInt();
        }

        public String[] pedirDatos(Scanner sc) {
            sc.nextLine();
            System.out.print("Nombre: ");
            String n = sc.nextLine();
            System.out.print("Email: ");
            String e = sc.nextLine();
            return new String[]{n, e};
        }

        public void mostrarMensaje(String msg) {
            System.out.println(">> " + msg);
        }
    }

    static class Aplicacion {
        private ControladorUsuarioRepo controlador;

        public Aplicacion(RepositorioUsuario repo, VistaUsuario vista) {
            this.controlador = new ControladorUsuarioRepo(repo, vista);
        }

        public void ejecutar() {
            controlador.iniciar();
        }
    }

    static void solucion_3() {
        System.out.println("IMPLEMENTACION: Inyeccion de Dependencias");
        System.out.println("=========================================");
        System.out.println("""
    // Las dependencias se inyectan via constructor
    
    class Aplicacion {
        private ControladorUsuarioRepo controlador;
        
        public Aplicacion(RepositorioUsuario r, VistaUsuario v) {
            this.controlador = new ControladorUsuarioRepo(r, v);
        }
        
        public void ejecutar() { controlador.iniciar(); }
    }
    
    // Uso:
    // RepositorioUsuario repo = new RepositorioUsuarioMemoria();
    // VistaUsuario vista = new VistaConsola();
    // Aplicacion app = new Aplicacion(repo, vista);
    // app.ejecutar();
        """);
        System.out.println("DEMOSTRACION:");
        System.out.println("Inyectando RepositorioUsuarioMemoria + VistaResumida:");
        RepositorioUsuario repo = new RepositorioUsuarioMemoria();
        VistaUsuario vista = new VistaResumida();
        Aplicacion app = new Aplicacion(repo, vista);
        System.out.println("Demo: creando 2 usuarios de prueba...");
        repo.save(new Usuario(0, "Admin", "admin@email.com"));
        repo.save(new Usuario(0, "Usuario", "user@email.com"));
        System.out.println("Listando (vista resumida):");
        vista.mostrarTodos(repo.findAll());
        System.out.println();
        System.out.println("Cambiando a VistaConsola:");
        VistaUsuario vista2 = new VistaConsola();
        Aplicacion app2 = new Aplicacion(repo, vista2);
        System.out.println("Listando (vista detallada):");
        vista2.mostrarTodos(repo.findAll());
        System.out.println();
        System.out.println("Las dependencias son intercambiables sin cambiar el controlador.");
    }
}
