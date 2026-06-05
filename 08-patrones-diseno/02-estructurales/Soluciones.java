import java.util.HashSet;
import java.util.Set;

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
    // SOLUCION 1: Adapter - Enchufes
    // ============================================================
    interface EnchufeEuropeo {
        void conectar();
    }

    interface EnchufeAmericano {
        void plugIn();
    }

    static class Lavadora implements EnchufeEuropeo {
        private String modelo;

        public Lavadora(String modelo) {
            this.modelo = modelo;
        }

        public void conectar() {
            System.out.println("Lavadora " + modelo + " conectada a 220V (clavija redonda)");
        }
    }

    static class AdaptadorEuropeoAamericano implements EnchufeAmericano {
        private EnchufeEuropeo enchufe;

        public AdaptadorEuropeoAamericano(EnchufeEuropeo enchufe) {
            this.enchufe = enchufe;
        }

        public void plugIn() {
            System.out.println("Adaptador: convirtiendo clavija redonda a plana...");
            enchufe.conectar();
            System.out.println("Adaptador: funcionando a 110V");
        }
    }

    static void solucion_1() {
        System.out.println("IMPLEMENTACION: Adapter para Enchufes");
        System.out.println("=====================================");
        System.out.println("""
    interface EnchufeEuropeo { void conectar(); }
    interface EnchufeAmericano { void plugIn(); }
    
    class Lavadora implements EnchufeEuropeo {
        public void conectar() {
            System.out.println("Conectado a 220V (clavija redonda)");
        }
    }
    
    class AdaptadorEuropeoAamericano implements EnchufeAmericano {
        private EnchufeEuropeo enchufe;
        
        public AdaptadorEuropeoAamericano(EnchufeEuropeo e) {
            this.enchufe = e;
        }
        
        public void plugIn() {
            System.out.println("Adaptando...");
            enchufe.conectar();
        }
    }
        """);
        System.out.println("DEMOSTRACION:");
        EnchufeEuropeo lavadora = new Lavadora("LG X100");
        EnchufeAmericano adaptador = new AdaptadorEuropeoAamericano(lavadora);
        adaptador.plugIn();
    }

    // ============================================================
    // SOLUCION 2: Decorator - Cafe
    // ============================================================
    interface Bebida {
        double costo();
        String descripcion();
    }

    static class CafeSimple implements Bebida {
        public double costo() { return 2.0; }
        public String descripcion() { return "Cafe simple"; }
    }

    static abstract class BebidaDecorator implements Bebida {
        protected Bebida bebida;

        public BebidaDecorator(Bebida bebida) {
            this.bebida = bebida;
        }

        public abstract double costo();
        public abstract String descripcion();
    }

    static class Leche extends BebidaDecorator {
        public Leche(Bebida bebida) { super(bebida); }
        public double costo() { return bebida.costo() + 0.5; }
        public String descripcion() { return bebida.descripcion() + ", leche"; }
    }

    static class Azucar extends BebidaDecorator {
        public Azucar(Bebida bebida) { super(bebida); }
        public double costo() { return bebida.costo() + 0.2; }
        public String descripcion() { return bebida.descripcion() + ", azucar"; }
    }

    static class Crema extends BebidaDecorator {
        public Crema(Bebida bebida) { super(bebida); }
        public double costo() { return bebida.costo() + 0.7; }
        public String descripcion() { return bebida.descripcion() + ", crema"; }
    }

    static class Chocolate extends BebidaDecorator {
        public Chocolate(Bebida bebida) { super(bebida); }
        public double costo() { return bebida.costo() + 0.8; }
        public String descripcion() { return bebida.descripcion() + ", chocolate"; }
    }

    static void solucion_2() {
        System.out.println("IMPLEMENTACION: Decorator para Cafe");
        System.out.println("===================================");
        System.out.println("""
    interface Bebida { double costo(); String descripcion(); }
    
    class CafeSimple implements Bebida { ... }
    
    abstract class BebidaDecorator implements Bebida {
        protected Bebida bebida;
        public BebidaDecorator(Bebida b) { this.bebida = b; }
    }
    
    class Leche extends BebidaDecorator {
        public double costo() { return bebida.costo() + 0.5; }
        public String descripcion() { return bebida.descripcion() + ", leche"; }
    }
    // Azucar, Crema, Chocolate similar
        """);
        System.out.println("DEMOSTRACION:");
        Bebida cafe1 = new CafeSimple();
        System.out.println(cafe1.descripcion() + " = $" + cafe1.costo());

        Bebida cafe2 = new Leche(new CafeSimple());
        System.out.println(cafe2.descripcion() + " = $" + cafe2.costo());

        Bebida cafe3 = new Chocolate(new Crema(new Leche(new CafeSimple())));
        System.out.println(cafe3.descripcion() + " = $" + cafe3.costo());

        Bebida cafe4 = new Azucar(new Leche(new CafeSimple()));
        System.out.println(cafe4.descripcion() + " = $" + cafe4.costo());
    }

    // ============================================================
    // SOLUCION 3: Proxy - Control de Acceso
    // ============================================================
    interface Servicio {
        void ejecutar(String usuario);
    }

    static class ServicioReal implements Servicio {
        public void ejecutar(String usuario) {
            System.out.println("EJECUTANDO: Operacion critica realizada por " + usuario);
        }
    }

    static class ProxyServicio implements Servicio {
        private ServicioReal servicioReal;
        private Set<String> usuariosValidos;

        public ProxyServicio() {
            this.servicioReal = new ServicioReal();
            this.usuariosValidos = new HashSet<>();
            usuariosValidos.add("admin");
            usuariosValidos.add("javier");
            usuariosValidos.add("operador");
        }

        public void ejecutar(String usuario) {
            if (usuariosValidos.contains(usuario.toLowerCase())) {
                System.out.println("Proxy: Acceso autorizado para " + usuario);
                servicioReal.ejecutar(usuario);
            } else {
                System.out.println("PROXY: Acceso DENEGADO para " + usuario + " (no autorizado)");
            }
        }
    }

    static void solucion_3() {
        System.out.println("IMPLEMENTACION: Proxy de Control de Acceso");
        System.out.println("==========================================");
        System.out.println("""
    interface Servicio { void ejecutar(String usuario); }
    
    class ServicioReal implements Servicio {
        public void ejecutar(String usuario) {
            System.out.println("Operacion ejecutada por " + usuario);
        }
    }
    
    class ProxyServicio implements Servicio {
        private ServicioReal real;
        private Set<String> usuariosValidos;
        
        public void ejecutar(String usuario) {
            if (usuariosValidos.contains(usuario)) {
                real.ejecutar(usuario);
            } else {
                System.out.println("Acceso denegado");
            }
        }
    }
        """);
        System.out.println("DEMOSTRACION:");
        Servicio proxy = new ProxyServicio();
        proxy.ejecutar("admin");
        proxy.ejecutar("javier");
        proxy.ejecutar("hacker");
        proxy.ejecutar("operador");
        proxy.ejecutar("invitado");
    }
}
