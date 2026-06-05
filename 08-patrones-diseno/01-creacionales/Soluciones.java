import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

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
    // SOLUCION 1: Singleton - Logger
    // ============================================================
    static class Logger {
        private static Logger instancia;
        private static final DateTimeFormatter FORMATO =
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        private Logger() {
            System.out.println("Logger inicializado.");
        }

        public static synchronized Logger getInstance() {
            if (instancia == null) {
                instancia = new Logger();
            }
            return instancia;
        }

        public void log(String mensaje) {
            String timestamp = LocalDateTime.now().format(FORMATO);
            System.out.println("[" + timestamp + "] " + mensaje);
        }
    }

    static void solucion_1() {
        System.out.println("IMPLEMENTACION: Singleton Logger");
        System.out.println("================================");
        System.out.println("""
    public class Logger {
        private static Logger instancia;
        private static final DateTimeFormatter FORMATO =
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        
        private Logger() {
            System.out.println("Logger inicializado.");
        }
        
        public static synchronized Logger getInstance() {
            if (instancia == null) {
                instancia = new Logger();
            }
            return instancia;
        }
        
        public void log(String mensaje) {
            String timestamp = LocalDateTime.now().format(FORMATO);
            System.out.println("[" + timestamp + "] " + mensaje);
        }
    }
        """);
        System.out.println("DEMOSTRACION:");
        Logger l1 = Logger.getInstance();
        Logger l2 = Logger.getInstance();
        l1.log("Primer mensaje de prueba");
        l2.log("Segundo mensaje de prueba");
        System.out.println("Misma instancia? " + (l1 == l2));
    }

    // ============================================================
    // SOLUCION 2: Factory Method - Figuras
    // ============================================================
    interface Figura {
        void dibujar();
    }

    static class Circulo implements Figura {
        public void dibujar() {
            System.out.println("Dibujando un circulo de radio 10.0");
        }
    }

    static class Cuadrado implements Figura {
        public void dibujar() {
            System.out.println("Dibujando un cuadrado de lado 15.0");
        }
    }

    static class Triangulo implements Figura {
        public void dibujar() {
            System.out.println("Dibujando un triangulo de base 12.0 y altura 8.0");
        }
    }

    static class FiguraFactory {
        public static Figura crearFigura(String tipo) {
            switch (tipo.toLowerCase()) {
                case "circulo": return new Circulo();
                case "cuadrado": return new Cuadrado();
                case "triangulo": return new Triangulo();
                default:
                    throw new IllegalArgumentException("Figura desconocida: " + tipo);
            }
        }
    }

    static void solucion_2() {
        System.out.println("IMPLEMENTACION: Factory Method para Figuras");
        System.out.println("===========================================");
        System.out.println("""
    interface Figura {
        void dibujar();
    }
    
    class Circulo implements Figura {
        public void dibujar() {
            System.out.println("Dibujando un circulo");
        }
    }
    
    class Cuadrado implements Figura {
        public void dibujar() {
            System.out.println("Dibujando un cuadrado");
        }
    }
    
    class Triangulo implements Figura {
        public void dibujar() {
            System.out.println("Dibujando un triangulo");
        }
    }
    
    class FiguraFactory {
        public static Figura crearFigura(String tipo) {
            switch (tipo.toLowerCase()) {
                case "circulo": return new Circulo();
                case "cuadrado": return new Cuadrado();
                case "triangulo": return new Triangulo();
                default:
                    throw new IllegalArgumentException("Figura desconocida: " + tipo);
            }
        }
    }
        """);
        System.out.println("DEMOSTRACION:");
        System.out.println("Creando las tres figuras via factory:");
        Figura f1 = FiguraFactory.crearFigura("circulo");
        Figura f2 = FiguraFactory.crearFigura("cuadrado");
        Figura f3 = FiguraFactory.crearFigura("triangulo");
        f1.dibujar();
        f2.dibujar();
        f3.dibujar();
    }

    // ============================================================
    // SOLUCION 3: Builder - Computadora
    // ============================================================
    static class Computadora {
        private final String cpu;
        private final int ram;
        private final int almacenamiento;
        private final String tarjetaGrafica;
        private final String sistemaOperativo;

        private Computadora(Builder builder) {
            this.cpu = builder.cpu;
            this.ram = builder.ram;
            this.almacenamiento = builder.almacenamiento;
            this.tarjetaGrafica = builder.tarjetaGrafica;
            this.sistemaOperativo = builder.sistemaOperativo;
        }

        @Override
        public String toString() {
            return "Computadora{cpu='" + cpu + "', ram=" + ram +
                   "GB, almacenamiento=" + almacenamiento + "GB, " +
                   "grafica='" + tarjetaGrafica + "', so='" + sistemaOperativo + "'}";
        }

        static class Builder {
            private String cpu = "Intel i5";
            private int ram = 8;
            private int almacenamiento = 256;
            private String tarjetaGrafica = "Integrada";
            private String sistemaOperativo = "Sin SO";

            public Builder cpu(String cpu) {
                this.cpu = cpu;
                return this;
            }

            public Builder ram(int ram) {
                this.ram = ram;
                return this;
            }

            public Builder almacenamiento(int almacenamiento) {
                this.almacenamiento = almacenamiento;
                return this;
            }

            public Builder tarjetaGrafica(String tarjetaGrafica) {
                this.tarjetaGrafica = tarjetaGrafica;
                return this;
            }

            public Builder sistemaOperativo(String sistemaOperativo) {
                this.sistemaOperativo = sistemaOperativo;
                return this;
            }

            public Computadora build() {
                return new Computadora(this);
            }
        }
    }

    static void solucion_3() {
        System.out.println("IMPLEMENTACION: Builder para Computadora");
        System.out.println("========================================");
        System.out.println("""
    class Computadora {
        private final String cpu;
        private final int ram;
        private final int almacenamiento;
        private final String tarjetaGrafica;
        private final String sistemaOperativo;
        
        private Computadora(Builder builder) { ... }
        
        static class Builder {
            private String cpu = "Intel i5";
            private int ram = 8;
            private int almacenamiento = 256;
            private String tarjetaGrafica = "Integrada";
            private String sistemaOperativo = "Sin SO";
            
            public Builder cpu(String cpu) { this.cpu = cpu; return this; }
            public Builder ram(int ram) { this.ram = ram; return this; }
            // ... otros setters que retornan this
            public Computadora build() { return new Computadora(this); }
        }
    }
        """);
        System.out.println("DEMOSTRACION:");
        Computadora basica = new Computadora.Builder().build();
        Computadora gaming = new Computadora.Builder()
            .cpu("Intel i9")
            .ram(32)
            .almacenamiento(1000)
            .tarjetaGrafica("NVIDIA RTX 4080")
            .sistemaOperativo("Windows 11")
            .build();
        Computadora oficina = new Computadora.Builder()
            .cpu("AMD Ryzen 5")
            .ram(16)
            .almacenamiento(512)
            .build();
        System.out.println("Basica: " + basica);
        System.out.println("Gaming: " + gaming);
        System.out.println("Oficina: " + oficina);
    }
}
