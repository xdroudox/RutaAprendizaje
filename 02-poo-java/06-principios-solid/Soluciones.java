/**
 * SOLUCIONES - Principios SOLID (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 6 [ejercicio] -s
 */
public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0 && !args[0].startsWith("-")) {
            int num;
            try {
                num = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Solucion no encontrada");
                return;
            }
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Ejercicio no encontrado. Valores: 1-3");
            }
        } else {
            System.out.println("SOLUCIONES:");
            System.out.println("  🟢 1. SRP: Reporte e Impresora");
            System.out.println("  🟡 2. OCP: Sistema de descuentos");
            System.out.println("  🔴 3. DIP: Servicio con inyeccion");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: SRP");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Reporte {
    String titulo;
    String contenido;

    Reporte(String titulo, String contenido) {
        this.titulo = titulo;
        this.contenido = contenido;
    }
}

class Impresora {
    static void imprimir(Reporte r) {
        System.out.println(r.titulo);
        System.out.println("---");
        System.out.println(r.contenido);
    }
}

public class Main {
    public static void main(String[] args) {
        Reporte r = new Reporte("Ventas", "Resumen del mes");
        Impresora.imprimir(r);
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. SRP = cada clase tiene UNA responsabilidad:
   - Reporte: solo ALMACENAR datos (titulo, contenido)
   - Impresora: solo IMPRIMIR reportes

2. `static void imprimir(Reporte r)` — Metodo estatico: no necesita
   instancia de Impresora. Se llama con `Impresora.imprimir(r)`.

3. Ventajas: si cambia el formato de impresion, solo modificas
   Impresora. Si cambian los datos del reporte, solo modificas Reporte.

4. ANTES (violando SRP): Reporte tenia metodo imprimir(). Si querias
   cambiar la impresion, modificabas Reporte. Si querias cambiar los
   datos, tambien modificabas Reporte. DOS RAZONES para cambiar.
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: OCP");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
interface Descuento {
    double aplicar(double precio);
}

class DescuentoPorcentaje implements Descuento {
    double porcentaje;

    DescuentoPorcentaje(double porcentaje) {
        this.porcentaje = porcentaje;
    }

    public double aplicar(double precio) {
        return precio * (1 - porcentaje / 100);
    }
}

class DescuentoFijo implements Descuento {
    double cantidad;

    DescuentoFijo(double cantidad) {
        this.cantidad = cantidad;
    }

    public double aplicar(double precio) {
        return Math.max(0, precio - cantidad);
    }
}

class CalculadoraPrecio {
    double calcular(double precio, Descuento d) {
        return d.aplicar(precio);
    }
}

public class Main {
    public static void main(String[] args) {
        CalculadoraPrecio calc = new CalculadoraPrecio();

        System.out.println(calc.calcular(100, new DescuentoPorcentaje(10)));
        // 90.0 (100 - 10%)

        System.out.println(calc.calcular(100, new DescuentoFijo(15)));
        // 85.0 (100 - 15)
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. OCP = abierto a EXTENSION, cerrado a MODIFICACION.

2. La interface `Descuento` es el CONTRATO. Cualquier nuevo descuento
   implementa esta interface. CalculadoraPrecio NO SE MODIFICA.

3. `DescuentoPorcentaje`: aplica (100 * (1 - 10/100) = 100 * 0.9 = 90)
   `DescuentoFijo`: aplica Math.max(0, 100 - 15) = 85

4. `Math.max(0, precio - cantidad)` — Evita precios negativos.
   Si el descuento fijo es mayor que el precio, devuelve 0.

5. Para aniadir "Descuento2x1": creas una NUEVA clase que implemente
   Descuento. NO tocas CalculadoraPrecio. Eso es OCP.
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: DIP");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
interface BaseDatos {
    void guardar(String dato);
}

class BaseDatosMySQL implements BaseDatos {
    public void guardar(String dato) {
        System.out.println("Guardado en MySQL: " + dato);
    }
}

class BaseDatosArchivo implements BaseDatos {
    public void guardar(String dato) {
        System.out.println("Guardado en archivo: " + dato);
    }
}

class Servicio {
    private BaseDatos db;

    Servicio(BaseDatos db) {
        this.db = db;
    }

    void procesar(String dato) {
        db.guardar(dato);
    }
}

public class Main {
    public static void main(String[] args) {
        Servicio s1 = new Servicio(new BaseDatosMySQL());
        s1.procesar("datos");

        Servicio s2 = new Servicio(new BaseDatosArchivo());
        s2.procesar("datos");
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. DIP = depender de ABSTRACCIONES, no de IMPLEMENTACIONES.

2. `Servicio` tiene un atributo de tipo `BaseDatos` (la INTERFACE),
   no `BaseDatosMySQL` ni `BaseDatosArchivo`.

3. La dependencia se INYECTA por constructor (Inyeccion de dependencia):
   `new Servicio(new BaseDatosMySQL())`. Servicio no crea la dependencia,
   la RECIBE.

4. Ventajas:
   - Podemos CAMBIAR la base de datos sin modificar Servicio
   - Podemos MOCKear la base de datos en tests
   - Menos acoplamiento entre clases

5. Sin DIP: Servicio crearia su propia base de datos con `new`.
   Para cambiar de MySQL a Archivo, habria que MODIFICAR Servicio.
   Con DIP, solo cambiamos lo que pasamos al constructor.
""");
    }
}
