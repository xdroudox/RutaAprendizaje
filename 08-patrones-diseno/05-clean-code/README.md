# Clean Code

Principios y practicas para escribir codigo legible, mantenible y eficiente.

## Convenciones de Nombres

Los nombres deben revelar la intencion del codigo.

**Malos nombres:**
```java
int d; // que representa?
List<String> lst;
public void proc() { ... }
```

**Buenos nombres:**
```java
int diasDelMes;
List<String> nombresDeUsuarios;
public void calcularTotalFactura() { ... }
```

**Reglas:**
- Clases: sustantivos en PascalCase (Usuario, FacturaService)
- Metodos: verbos en camelCase (calcularTotal(), obtenerNombre())
- Variables: camelCase descriptivo (totalConIVA, fechaNacimiento)
- Constantes: UPPER_SNAKE_CASE (MAX_INTENTOS, IVA_POR_DEFECTO)

## Funciones Pequenas

Una funcion debe hacer una sola cosa y hacerla bien.

**Reglas:**
- Funciones de menos de 20 lineas
- Un solo nivel de abstraccion
- Sin efectos secundarios sorprendentes
- Nombres que describan exactamente lo que hacen

**Mal ejemplo:**
```java
void procesar(String d) {
    // 50 lineas que validan, transforman, guardan y envian email
}
```

**Bien:**
```java
void procesarPedido(Pedido p) {
    validarPedido(p);
    calcularTotal(p);
    guardarPedido(p);
    notificarCliente(p);
}
```

## Principio DRY (Don't Repeat Yourself)

Cada pieza de conocimiento debe tener una representacion unica y no ambigua en el sistema.

**Mal ejemplo:**
```java
if (usuario.edad >= 18) { System.out.println("Mayor de edad"); }
// ... 50 lineas ...
if (persona.edad >= 18) { System.out.println("Mayor de edad"); }
```

**Bien:**
```java
boolean esMayorDeEdad(int edad) { return edad >= 18; }
```

## Comentarios vs Codigo

El codigo deberia explicarse por si mismo. Los comentarios no deberian explicar el "como", sino el "por que".

**Mal comentario:**
```java
// incrementar i en 1
i++;
```

**Buen codigo sin comentario:**
```java
// El nombre del metodo ya explica todo
void calcularDescuentoParaClienteVip() { ... }
```

**Buen comentario:**
```java
// Se usa BigDecimal en vez de double para evitar errores de redondeo
// en calculos financieros segun regulacion ISO 4217
```

## Ejercicios de Refactorizacion

Los ejercicios de este modulo presentan codigo de baja calidad que debes refactorizar aplicando los principios de Clean Code.

## Ejecuta

```
javac Ejercicios.java && java Ejercicios 1
javac Ejercicios.java && java Ejercicios 1 -p
javac Ejercicios.java && java Ejercicios -s 1
```
