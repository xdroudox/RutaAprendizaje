# NIVEL 2: Programacion Orientada a Objetos con Java

```java
System.out.println("Bienvenido al Nivel 2, Guerrero Java!");
System.out.println("Aqui dominaras los objetos y las clases.");
```

## Que aprenderas en este nivel

La **Programacion Orientada a Objetos (POO)** es un paradigma que organiza el codigo en **objetos** que tienen **datos** (atributos) y **comportamiento** (metodos). Java es un lenguaje PURAMENTE orientado a objetos.

Cada tema sigue la misma estructura:

```
📖 TEORIA → Explicacion con ejemplos linea por linea
📖 GLOSARIO → Terminos del tema definidos
🔄 COMPARATIVA → Mismo concepto en Java / Python / JavaScript
📝 EJEMPLO GUIADO → Problema resuelto paso a paso
🎯 EJERCICIOS → 3 niveles: 🟢 Basico, 🟡 Intermedio, 🔴 Avanzado
```

## Temas

| # | Tema | Que aprenderas |
|---|------|----------------|
| 1 | **Clases y Objetos** | Crear clases, constructores, instanciar objetos, metodos |
| 2 | **Encapsulacion** | private, public, getters, setters, proteger datos |
| 3 | **Herencia** | extends, super, @Override, reutilizar codigo |
| 4 | **Polimorfismo** | Sobrecarga, sobrescritura, tipos polymorphicos |
| 5 | **Interfaces y Clases Abstractas** | interface, abstract, contratos, implements |
| 6 | **Principios SOLID** | SRP, OCP, LSP, ISP, DIP |
| 7 | **Excepciones** | try, catch, throw, finally, excepciones personalizadas |
| 8 | **Colecciones y Genericos** | ArrayList, HashMap, Set, generics \<T\> |
| 9 | **Java I/O** | Leer y escribir archivos, File, InputStream, OutputStream |

## Requisitos

- **Java 17+** → `java -version` y `javac -version`
- Un editor de codigo

## Como ejecutar los ejercicios

```bash
# Ver la teoria
code 02-poo-java/03-herencia/README.md

# Ejecutar ejercicio
python scripts/runner.py 2 3 1

# Ver solucion
python scripts/runner.py 2 3 1 -s

# Ver pista
python scripts/runner.py 2 3 1 -p 1
```

## Diferencia con Python

En Python podias editar `ejercicios.py` directamente y ejecutar. En Java, los archivos `Ejercicios.java` muestran las instrucciones y debes crear tus propios archivos `.java` para practicar. Esto es INTENCIONAL: en el mundo real, los proyectos Java tienen multiples archivos.

**Pero los READMEs siguen siendo tu guia principal:** alli tienes la teoria, ejemplos, y ejercicios explicados igual que en Python.
