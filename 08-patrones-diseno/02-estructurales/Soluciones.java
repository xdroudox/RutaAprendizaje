/**
 * SOLUCIONES - Patrones Estructurales
 * Ejecuta desde raiz: python scripts/runner.py 8 2 [ejercicio] -s
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
        System.out.println(">> SOLUCION 1: Adapter - Enchufes");
        System.out.println("-".repeat(40));

        interface EnchufeEuropeo { void conectar(); }
        interface EnchufeAmericano { void plugIn(); }

        class EnchufeEuropeoConcreto implements EnchufeEuropeo {
            public void conectar() {
                System.out.println("Conectado a 220V (clavija redonda)");
            }
        }

        class Adaptador implements EnchufeAmericano {
            private EnchufeEuropeo enchufe;
            public Adaptador(EnchufeEuropeo e) { this.enchufe = e; }
            public void plugIn() {
                System.out.println("Adaptador: convirtiendo...");
                enchufe.conectar();
            }
        }

        EnchufeEuropeo euro = new EnchufeEuropeoConcreto();
        EnchufeAmericano adapter = new Adaptador(euro);
        adapter.plugIn();
    }

    static void solucion_2() {
        System.out.println(">> SOLUCION 2: Decorator - Cafe");
        System.out.println("-".repeat(40));

        interface Bebida {
            double costo();
            String descripcion();
        }

        class CafeSimple implements Bebida {
            public double costo() { return 2.0; }
            public String descripcion() { return "Cafe simple"; }
        }

        abstract class BebidaDecorator implements Bebida {
            protected Bebida bebida;
            public BebidaDecorator(Bebida b) { this.bebida = b; }
        }

        class Leche extends BebidaDecorator {
            public Leche(Bebida b) { super(b); }
            public double costo() { return bebida.costo() + 0.5; }
            public String descripcion() { return bebida.descripcion() + ", leche"; }
        }

        class Azucar extends BebidaDecorator {
            public Azucar(Bebida b) { super(b); }
            public double costo() { return bebida.costo() + 0.2; }
            public String descripcion() { return bebida.descripcion() + ", azucar"; }
        }

        Bebida cafe = new Azucar(new Leche(new CafeSimple()));
        System.out.println(cafe.descripcion() + " = $" + cafe.costo());
    }

    static void solucion_3() {
        System.out.println(">> SOLUCION 3: Proxy - Control de Acceso");
        System.out.println("-".repeat(40));

        interface Documento { void mostrar(); }

        class DocumentoReal implements Documento {
            private String contenido;
            public DocumentoReal(String c) { this.contenido = c; }
            public void mostrar() {
                System.out.println("Contenido: " + contenido);
            }
        }

        class ProxyDocumento implements Documento {
            private DocumentoReal doc;
            private String usuario;
            private String rol;
            public ProxyDocumento(String contenido, String u, String r) {
                this.doc = new DocumentoReal(contenido);
                this.usuario = u;
                this.rol = r;
            }
            public void mostrar() {
                if ("admin".equalsIgnoreCase(rol)) {
                    System.out.println("Acceso concedido a " + usuario);
                    doc.mostrar();
                } else {
                    System.out.println("Acceso DENEGADO para " + usuario
                        + " (rol: " + rol + ")");
                }
            }
        }

        new ProxyDocumento("Secreto", "Juan", "admin").mostrar();
        new ProxyDocumento("Secreto", "Pedro", "invitado").mostrar();
    }
}
