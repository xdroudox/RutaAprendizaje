# 04 - OWASP Top 10

## Introduccion

El OWASP Top 10 es una lista de las vulnerabilidades mas criticas en aplicaciones web,
publicada por la Open Web Application Security Project.

---

## A01: Broken Access Control

Ocurre cuando un usuario puede acceder a recursos o funciones para los que no tiene
permiso. Ejemplos: modificar la URL para acceder al perfil de otro usuario, escalar
de rol usuario a administrador.

**Prevencion**: validar permisos en cada peticion del lado del servidor, nunca
confiar en parametros del cliente.

---

## A02: Cryptographic Failures

Informacion sensible expuesta por cifrado debil o inexistente. Incluye credenciales
en texto plano, uso de protocolos inseguros (HTTP en lugar de HTTPS), algoritmos
obsoletos (MD5, SHA-1).

**Prevencion**: usar HTTPS siempre, cifrar datos sensibles en reposo y en transito,
usar algoritmos modernos (AES-256, SHA-256, bcrypt).

---

## A03: Injection

Cuando datos no confiables se envian a un interprete como parte de un comando o
consulta. El mas comun es SQL Injection.

Ejemplo: `' OR '1'='1' --` en un campo de login.

**Prevencion**: usar consultas parametrizadas (prepared statements), escapar entradas,
principio de minimo privilegio en la base de datos.

---

## A04: Insecure Design

Vulnerabilidades derivadas de un diseno inseguro, no solo de una implementacion
defectuosa. Ejemplo: no limitar la tasa de intentos de login (brute force).

**Prevencion**: modelado de amenazas en la fase de diseno, establecer limites y
restricciones por diseno.

---

## A05: Security Misconfiguration

Configuraciones inseguras por defecto, cuentas con contrasenas debiles, directorios
listables, headers HTTP faltantes, servicios innecesarios activos.

**Prevencion**: hardening de servidores, eliminar configuraciones por defecto,
automatizar la configuracion con IaC.

---

## A06: Vulnerable and Outdated Components

Uso de librerias, frameworks o dependencias con vulnerabilidades conocidas.

**Prevencion**: mantener dependencias actualizadas, usar herramientas como
Dependabot, Snyk u OWASP Dependency-Check.

---

## A07: Identification and Authentication Failures

Funciones de autenticacion debiles: permitir brute force, contrasenas debiles,
sesiones sin expiracion, credenciales por defecto.

**Prevencion**: MFA, politicas de contrasenas fuertes, limitar intentos de login,
sesiones con expiracion.

---

## A08: Software and Data Integrity Failures

Falta de verificacion de integridad en actualizaciones o pipelines CI/CD.
Ejemplo: dependencias descargadas sin verificar checksum, pipeline sin firmar.

**Prevencion**: firmar artefactos, verificar checksums, usar SBOM (Software Bill
of Materials).

---

## A09: Security Logging and Monitoring Failures

Falta de registros y monitoreo que impide detectar incidentes a tiempo.

**Prevencion**: registrar eventos de seguridad, alertar sobre anomalias, tener un
sistema SIEM o de monitoreo centralizado.

---

## A10: Server-Side Request Forgery (SSRF)

Un atacante fuerza al servidor a hacer peticiones a recursos internos o externos
no previstos. Comun en aplicaciones que aceptan URLs para descargar recursos.

**Prevencion**: validar y restringir URLs permitidas, segmentacion de red, no
acceder a servicios internos desde el servidor web.

---

## Preguntas de reflexion

<details>
<summary>Pregunta 1: Un usuario modifica el id en la URL de /perfil/123 a /perfil/456 y ve los datos de otro usuario. Que vulnerabilidad OWASP es?</summary>

A01: Broken Access Control. No se valida que el usuario sea propietario del recurso.
</details>

<details>
<summary>Pregunta 2: Que tecnica de programacion evita completamente la inyeccion SQL?</summary>

Usar consultas parametrizadas (prepared statements) en lugar de concatenar cadenas.
Esto separa los datos del codigo SQL, haciendo imposible la inyeccion.
</details>

<details>
<summary>Pregunta 3: Cual es la diferencia entre A02 (Cryptographic Failures) y A07 (Authentication Failures)?</summary>

A02 se refiere a datos no cifrados o cifrados con algoritmos debiles (ej: usar MD5 para
contrasenas). A07 se refiere a fallos en la autenticacion (ej: permitir brute force, no
tener MFA). Se relacionan pero A02 es sobre cifrado y A07 es sobre procesos de login.
</details>

---

## Glosario

- **Cifrado**: proceso de convertir informacion legible en ilegible usando un algoritmo y una clave. Puede ser simetrico (misma clave para cifrar y descifrar) o asimetrico (claves publica y privada).
- **Hashing**: funcion unidireccional que convierte datos en una cadena de longitud fija (hash). No se puede revertir. Se usa para verificar integridad y almacenar contrasenas.
- **SQL Injection**: vulnerabilidad donde un atacante inserta codigo SQL malicioso a traves de entradas de usuario para manipular la base de datos.
- **XSS (Cross-Site Scripting)**: vulnerabilidad que permite inyectar scripts maliciosos en paginas web vistas por otros usuarios.
- **CSRF (Cross-Site Request Forgery)**: ataque que fuerza a un usuario autenticado a ejecutar acciones no deseadas en una aplicacion web.
- **CSP (Content Security Policy)**: header HTTP que permite restringir que recursos (scripts, estilos, imagenes) puede cargar un navegador.
- **CORS (Cross-Origin Resource Sharing)**: mecanismo que permite o restringe peticiones entre diferentes origenes en el navegador.
- **JWT (JSON Web Token)**: formato compacto y autónomo para transmitir informacion entre partes como un objeto JSON firmado digitalmente.
- **OAuth**: protocolo de autorizacion que permite a aplicaciones acceder a recursos de un usuario sin compartir sus credenciales.
- **Salt**: valor aleatorio que se agrega a una contrasena antes de hashearla para evitar ataques de rainbow tables.
- **HTTPS**: version segura de HTTP que cifra la comunicacion entre el navegador y el servidor usando TLS/SSL.
- **Cifrado simetrico**: algoritmo que usa la misma clave para cifrar y descifrar datos (ej: AES).
- **Cifrado asimetrico**: algoritmo que usa un par de claves (publica y privada) donde una cifra y la otra descifra (ej: RSA).
- **Prepared Statement**: consulta SQL parametrizada donde los datos se pasan por separado del codigo SQL, previniendo inyeccion.
- **MFA (Multi-Factor Authentication)**: metodo de autenticacion que requiere dos o mas factores (algo que sabes, tienes o eres).
- **SIEM (Security Information and Event Management)**: sistema que centraliza y analiza logs de seguridad para detectar amenazas.
- **SBOM (Software Bill of Materials)**: inventario de componentes y dependencias de un software para rastrear vulnerabilidades.
