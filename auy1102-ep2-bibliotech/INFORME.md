# Informe de calidad: BiblioTech

## Integrantes

| Nombre | Usuario de GitHub |
|---|---|
| Juan Pablo Carvajal | `ju.carvajalg-jpg` |
| Mario Enrique Guaquiante | |

---

# Parte 1. Línea base de calidad

## 1.1 Objetivo

El objetivo de esta evaluación es analizar la calidad del software BiblioTech mediante pruebas unitarias, análisis estático, revisión de seguridad, auditoría de dependencias y pruebas de rendimiento. A partir de los resultados iniciales, se identifican defectos y se aplican correcciones para mejorar la confiabilidad, seguridad y mantenibilidad del sistema.

## 1.2 Resultados iniciales

| Herramienta | Propósito | Resultado inicial |
|---|---|---|
| pytest | Verificar el funcionamiento mediante pruebas automatizadas. | 19 pruebas ejecutadas: 15 aprobadas y 4 fallidas. |
| Flake8 | Detectar problemas de estilo y calidad del código Python. | Se encontraron imports sin uso, líneas demasiado largas, variables sin uso y excepciones genéricas, entre otros problemas. |
| Bandit | Detectar patrones de código potencialmente inseguros. | 8 hallazgos: 3 de severidad alta, 4 media y 1 baja. |
| pip-audit | Identificar vulnerabilidades conocidas en las dependencias. | 36 vulnerabilidades reportadas en 3 paquetes. |
| Pruebas de carga | Evaluar el rendimiento bajo distintos niveles de concurrencia. | Con 30 usuarios simultáneos, el percentil 95 de latencia superó el límite de 500 ms. |

## 1.3 Resultados detallados de pytest

En la primera ejecución se obtuvieron los siguientes resultados:

| Métrica | Resultado |
|---|---:|
| Total de pruebas | 19 |
| Pruebas aprobadas | 15 |
| Pruebas fallidas | 4 |
| Porcentaje de aprobación | 78,95 % |

Los cuatro fallos iniciales correspondieron a dos pruebas de validación ISBN con dígito verificador 0 y dos pruebas de cálculo de fechas de devolución que generaban `NotImplementedError`.

Estos resultados permitieron identificar funcionalidades que necesitaban correcciones antes de continuar con las pruebas de calidad.

## 1.4 Resultados iniciales de Flake8

| Archivo | Problema detectado | Código |
|---|---|---|
| `bibliotech/prestamos.py` | Importación de `os` sin uso. | F401 |
| `bibliotech/prestamos.py` | Espacios incorrectos alrededor del signo `=` en parámetros. | E251 |
| `bibliotech/prestamos.py` | Comparación incorrecta con `None`. | E711 |
| `bibliotech/prestamos.py` | Línea demasiado larga. | E501 |
| `bibliotech/reportes.py` | Importación de `sys` sin uso. | F401 |
| `bibliotech/reportes.py` | Variable `total` asignada, pero no utilizada. | F841 |
| `bibliotech/reportes.py` | Uso de una excepción genérica sin especificar el tipo. | E722 |
| `bibliotech/usuarios.py` | Línea demasiado larga. | E501 |

Los problemas encontrados afectaban principalmente la legibilidad, el mantenimiento y la claridad del código. Se propuso corregirlos antes de continuar con las demás etapas de validación.

## 1.5 Resultados iniciales de Bandit

| Hallazgo | Riesgo identificado | Severidad |
|---|---|---|
| B701 | Configuración de Jinja2 sin escape automático explícito. | Alta |
| B113 | Solicitudes HTTP sin tiempo límite. | Media |
| B307 | Uso de `eval()`, que puede ejecutar código arbitrario. | Media |
| B605 | Uso de `os.system()` para ejecutar comandos del sistema. | Alta |
| B324 | Uso de MD5 para operaciones relacionadas con hashes. | Alta |
| B608 | Construcción de consultas SQL mediante cadenas. | Media |
| B608 | Otro caso de construcción insegura de consultas SQL. | Media |
| B311 | Uso de `random` para generar valores que podrían emplearse en contextos de seguridad. | Baja |

Bandit identificó patrones potencialmente inseguros que requerían revisión manual. Estos hallazgos no demuestran por sí solos que exista una vulnerabilidad explotable, pero permiten detectar prácticas que deben corregirse o justificarse.

## 1.6 Resultados iniciales de pip-audit

| Paquete | Versión inicial | Vulnerabilidades reportadas | Versión objetivo de actualización |
|---|---:|---:|---:|
| `requests` | 2.25.1 | 8 | 2.33.0 |
| `urllib3` | 1.26.5 | 18 | 2.8.0 |
| `jinja2` | 2.11.2 | 10 | 3.1.6 |
| **Total** | | **36** | |

La auditoría indicó que las versiones utilizadas tenían vulnerabilidades conocidas. Se planteó actualizar las dependencias a versiones corregidas y compatibles con el proyecto.

Las versiones objetivo corresponden a las registradas durante la evaluación; debe confirmarse que sean apropiadas y estén disponibles para el entorno del proyecto.

---

# Parte 2. Pruebas unitarias y corrección de defectos

## 2.1 Validación ISBN en `catalogo.py`

Las pruebas iniciales detectaron dos fallos relacionados con ISBN cuyo dígito verificador era 0.

| Caso de prueba | Defecto detectado | Corrección aplicada | Resultado posterior |
|---|---|---|---|
| ISBN con dígito verificador 0 | El cálculo podía producir 10 en vez de 0. | Se ajustó el cálculo del dígito verificador mediante el módulo 10. | Aprobado |
| ISBN sin guiones con dígito verificador 0 | El mismo problema de cálculo aparecía al procesar el ISBN sin guiones. | Se corrigió la fórmula para obtener el dígito verificador esperado. | Aprobado |

El problema se encontraba en el cálculo final del dígito verificador. La corrección permitió que los casos con resultado matemático equivalente a 10 se representaran correctamente como 0.

**Resultado registrado después de la corrección:** 9 pruebas aprobadas y ninguna fallida.

## 2.2 Cálculo de multas en `multas.py`

Se ampliaron las pruebas para cubrir valores límite y comportamientos que no estaban suficientemente protegidos.

| Caso de prueba | Problema detectado | Corrección aplicada | Resultado esperado |
|---|---|---|---|
| Días de atraso negativos | La función no rechazaba valores negativos. | Se agregó validación para lanzar `ValueError`. | Los días negativos se rechazan. |
| Cero días de atraso | La fórmula podía producir una multa negativa para docentes. | Se corrigió el cálculo para evitar multas negativas. | Multa de $0. |
| Docente dentro del período de gracia | No se aplicaba correctamente el período de gracia de dos días. | Se ajustó la lógica del período de gracia. | Multa de $0 durante los dos primeros días. |
| Tope máximo de multa para docentes | Se necesitaba comprobar el límite de la multa. | Se incorporó una prueba específica para el valor límite. | La multa respeta el máximo definido por las reglas del sistema. |

Durante la primera ejecución de las nuevas pruebas se obtuvieron 3 fallos y 4 aprobaciones. Los fallos estaban relacionados con los días negativos, la generación de multas negativas y el período de gracia de los docentes.

Después de las correcciones, el resultado registrado fue de 7 pruebas aprobadas y ninguna fallida.

## 2.3 Fechas de devolución en `prestamos.py`

Se corrigieron y ampliaron las pruebas de fechas de devolución, incluyendo el tratamiento de fines de semana y tipos de usuario no válidos.

| Caso de prueba | Objetivo | Resultado posterior |
|---|---|---|
| Devolución de estudiante a los 7 días | Verificar el plazo de devolución para estudiantes. | Aprobado |
| Devolución de docente a los 14 días | Verificar el plazo de devolución para docentes. | Aprobado |
| Fecha de devolución en sábado | Comprobar que la fecha se traslade al lunes. | Aprobado |
| Fecha de devolución en domingo | Comprobar que la fecha se traslade al lunes. | Aprobado |
| Tipo de usuario inválido | Verificar que se rechacen tipos no permitidos mediante `ValueError`. | Aprobado |

**Resultado registrado después de la corrección:** 6 pruebas aprobadas y ninguna fallida.

## 2.4 Importancia de las pruebas unitarias

Las pruebas unitarias permitieron identificar defectos concretos en las reglas de negocio y comprobar que las correcciones no alteraran el comportamiento esperado.

Se priorizaron los siguientes aspectos:

- Validación correcta de ISBN.
- Cálculo de multas sin valores negativos.
- Aplicación de períodos de gracia.
- Cumplimiento de los plazos de devolución.
- Ajuste de fechas que coinciden con fines de semana.
- Rechazo de entradas no válidas.

Estas pruebas también ayudan a prevenir regresiones: si una modificación posterior vuelve a introducir un defecto, la prueba correspondiente puede detectarlo antes de que el cambio llegue a producción.

---

# Parte 3. Análisis estático con Flake8

## 3.1 Defectos identificados y correcciones

| Código | Archivo o ubicación | Significado | Corrección aplicada |
|---|---|---|---|
| E501 | `bibliotech/prestamos.py` | Línea demasiado larga. | Se dividieron las instrucciones extensas. |
| W292 | Archivos Python afectados | Falta el salto de línea final. | Se agregó el salto de línea al final del archivo. |
| F401 | `bibliotech/reportes.py` | Importación sin uso. | Se eliminaron los imports innecesarios. |
| F841 | `bibliotech/reportes.py` | Variable asignada que no se utiliza. | Se eliminó la asignación innecesaria o se ajustó el uso de la variable. |
| E722 | `bibliotech/reportes.py` | Excepción genérica sin tipo específico. | Se especificaron las excepciones correspondientes. |
| W293 | Archivos de pruebas afectados | Línea en blanco con espacios. | Se eliminaron los espacios sobrantes. |
| E711 | `bibliotech/prestamos.py` | Comparación incorrecta con `None`. | Se reemplazó por una comparación apropiada, como `is None` o `is not None`. |
| E251 | `bibliotech/prestamos.py` | Espacios incorrectos en parámetros. | Se ajustó el formato de los parámetros. |

## 3.2 Resultado final

Después de aplicar las correcciones se ejecutó el análisis estático mediante:

```bash
python -m flake8 --count
```

**Resultado registrado:** Flake8 no reportó infracciones.

La corrección de estos problemas mejora la consistencia del código, facilita la lectura y reduce errores evitables durante el desarrollo y el mantenimiento.

---

# Parte 4. Análisis de seguridad

## 4.1 Correcciones propuestas a partir de Bandit

| ID | Riesgo | Corrección aplicada o propuesta | Beneficio |
|---|---|---|---|
| B701 | Configuración de Jinja2 sin escape automático explícito. | Configurar el entorno mediante `select_autoescape()`. | Reduce el riesgo de inyección de contenido HTML o scripts en plantillas compatibles con el escape automático. |
| B113 | Peticiones HTTP sin tiempo límite. | Agregar `timeout=5` a las solicitudes correspondientes. | Evita esperas indefinidas ante respuestas lentas o servicios no disponibles. |
| B307 | Uso de `eval()`. | Eliminar `eval()` y limitar la evaluación a las operaciones permitidas. | Evita ejecutar código arbitrario a partir de entradas no confiables. |
| B605 | Ejecución de comandos mediante `os.system()`. | Sustituir el mecanismo por operaciones de archivos o procesos controlados según la necesidad. | Reduce el riesgo de inyección de comandos. |
| B324 | Uso de MD5 en operaciones relacionadas con hashes. | Utilizar un mecanismo apropiado según el propósito del hash. Para contraseñas, emplear un algoritmo de derivación de claves con sal. | Mejora la resistencia frente a ataques contra las contraseñas almacenadas. |
| B608 | Construcción de consultas SQL mediante cadenas. | Utilizar consultas parametrizadas. | Reduce el riesgo de inyección SQL. |
| B311 | Uso de `random` para generar tokens de seguridad. | Utilizar el módulo `secrets`. | Proporciona valores adecuados para usos que requieren impredecibilidad. |

**Nota técnica:** `ast.literal_eval()` es adecuado para interpretar ciertos valores literales de Python, pero no constituye un reemplazo general para evaluar expresiones o fórmulas. Si el sistema necesita evaluar fórmulas, debe permitir explícitamente las operaciones admitidas y rechazar el resto.

Asimismo, reemplazar `os.system()` por `shutil.copy()` solo es apropiado si la operación original consiste en copiar archivos. La sustitución debe respetar la finalidad real de la función.

## 4.2 Pruebas de seguridad para consultas SQL

Se incorporaron pruebas para comprobar que las entradas del usuario no alteraran las consultas SQL.

| Prueba | Entrada o escenario | Resultado esperado |
|---|---|---|
| `test_sql_injection_en_obtener_usuario` | Entrada manipulada como `' OR '1'='1`. | La entrada se trata como un valor y no modifica la estructura de la consulta. |
| `test_registrar_usuario_con_comilla_simple_en_nombre` | Registro de un nombre como `Bernardo O'Higgins`. | El usuario se registra correctamente sin romper la consulta SQL. |

La parametrización permite separar la estructura de una consulta de los datos suministrados por el usuario. Esto reduce la posibilidad de que una entrada se interprete como parte del código SQL.

## 4.3 Auditoría de dependencias con pip-audit

| Paquete | Versión inicial | Vulnerabilidades reportadas inicialmente | Versión objetivo registrada |
|---|---:|---:|---:|
| `requests` | 2.25.1 | 8 | 2.33.0 |
| `urllib3` | 1.26.5 | 18 | 2.8.0 |
| `jinja2` | 2.11.2 | 10 | 3.1.6 |
| **Total** | | **36** | |

La auditoría inicial mostró que las dependencias utilizadas podían contener vulnerabilidades conocidas.

La medida correctiva consiste en actualizar las dependencias, comprobar la compatibilidad con el proyecto y repetir la auditoría para verificar el resultado.

Comando de referencia:

```bash
python -m pip_audit
```

El resultado final debe documentar las versiones efectivamente instaladas y las vulnerabilidades que continúen pendientes. La actualización de una dependencia no debe considerarse validada hasta que la nueva auditoría confirme el estado.

## 4.4 Revisión manual de seguridad

Además de los resultados de Bandit, se revisaron posibles problemas que necesitan análisis contextual.

| Hallazgo | Ubicación | Riesgo | Medida correctiva |
|---|---|---|---|
| Path Traversal | `bibliotech/reportes.py`, función `exportar_respaldo(nombre_archivo)` | Una ruta manipulada puede permitir escribir o sobrescribir archivos fuera del directorio autorizado. | Validar el nombre y resolver la ruta final, comprobando que permanezca dentro del directorio de respaldos permitido. |
| Protección de contraseñas | `bibliotech/usuarios.py`, función `_hash_clave(clave)` | Un hash rápido sin sal, como SHA-256 utilizado directamente para contraseñas, no proporciona una protección adecuada. | Utilizar un algoritmo específico para contraseñas, como PBKDF2, con una sal aleatoria única por contraseña. |

### Path Traversal

Si `nombre_archivo` puede ser controlado por el usuario, se deben rechazar rutas que intenten salir del directorio autorizado.

Una validación apropiada debe comprobar la ruta de destino después de resolverla, no limitarse a eliminar algunos caracteres del nombre.

### Protección de contraseñas

Es importante distinguir entre los hashes utilizados para verificar la integridad de datos y los mecanismos empleados para almacenar contraseñas.

SHA-256 es un hash criptográfico general, pero no es una función de derivación de claves diseñada específicamente para contraseñas. Para ese propósito es preferible utilizar PBKDF2, scrypt o Argon2, con una sal aleatoria y parámetros apropiados.

**Verificación pendiente:** confirmar que la implementación final de `_hash_clave()` utiliza efectivamente el mecanismo de derivación de claves indicado y que la autenticación sigue funcionando correctamente.

---

# Parte 5. Pruebas de carga y estrés

## 5.1 Objetivo y criterio de aceptación

El objetivo de las pruebas de rendimiento es evaluar cómo responde BiblioTech cuando recibe múltiples solicitudes simultáneas.

Se definió el siguiente criterio de aceptación:

- 30 usuarios simultáneos.
- El 95 % de las búsquedas debe responder en menos de 500 ms.
- No deben producirse errores durante la prueba.

La latencia p95 representa el tiempo por debajo del cual se completó el 95 % de las solicitudes medidas.

## 5.2 Resultados de la línea base

| Usuarios simultáneos | Peticiones/s | Latencia p95 (ms) | Errores reportados (%) | ¿Cumple? |
|---:|---:|---:|---:|:---:|
| 10 | 49 | 164 | 0 | Sí |
| 30 | 49 | 613 | 0 | No |
| 60 | 49 | 1227 | 0 | No |

Con 10 usuarios simultáneos, la latencia p95 fue de 164 ms y no se registraron errores. Sin embargo, al aumentar la concurrencia a 30 usuarios, la latencia alcanzó 613 ms, superando el límite de 500 ms.

Con 60 usuarios, la latencia aumentó hasta 1227 ms. Estos resultados indican que la versión evaluada no cumplía el criterio de latencia a partir de 30 usuarios simultáneos.

## 5.3 Diagnóstico y corrección

Durante el análisis se revisó el uso de la variable `visitas` al construir las respuestas del servidor.

Se identificó que una variable compartida podía cambiar mientras se procesaba una solicitud concurrente. Como medida correctiva, se utilizó una variable local, `numero_visita`, para conservar el número correspondiente a cada petición durante la construcción de su respuesta.

| Usuarios simultáneos | Peticiones/s | Latencia p95 (ms) | Errores reportados (%) | ¿Cumple? |
|---:|---:|---:|---:|:---:|
| 30 | 49 | 614 | 0 | No |

Aunque el cambio busca evitar inconsistencias entre solicitudes concurrentes, el resultado registrado continúa por encima del umbral de latencia establecido.

Por lo tanto, la corrección de la variable compartida no demuestra, por sí sola, que se haya alcanzado el criterio de rendimiento.

La evaluación debe respetar las restricciones del encargo, que prohíben modificar `CAPACIDAD`, `TIEMPO_CONSULTA` y `ESPERA_MAXIMA` en `servidor.py`.

## 5.4 Pruebas de estrés

Se realizaron pruebas adicionales para observar el comportamiento del sistema bajo cargas superiores.

| Usuarios simultáneos | Peticiones/s | Latencia p95 (ms) | Errores reportados | ¿Cumple? |
|---:|---:|---:|---:|:---:|
| 100 | 76 | 1310 | 359 | No |
| 300 | 237 | 1311 | 2386 | No |
| 500 | 372 | 1315 | 4388 | No |

Las pruebas muestran que el volumen de solicitudes procesadas por segundo aumenta al elevar la concurrencia, pero también se registran errores y una latencia elevada.

Las cifras de la columna de errores se presentan como cantidades absolutas, según los datos proporcionados. No deben interpretarse como porcentajes sin calcular previamente la proporción de errores respecto del total de solicitudes.

Para obtener una evaluación reproducible, cada ejecución debe registrar:

- Número de usuarios simultáneos.
- Duración de la prueba.
- Número total de solicitudes.
- Solicitudes correctas y fallidas.
- Peticiones por segundo.
- Latencia p50, p95 y, cuando corresponda, p99.
- Tipo de error HTTP o excepción observada.

## 5.5 Limitaciones y análisis de resultados

Los resultados disponibles muestran que la versión evaluada incumple el criterio de latencia con 30 usuarios simultáneos.

También se registraron pruebas con cargas de 100, 300 y 500 usuarios, en las que aumentaron las cantidades de errores.

Sin embargo, existe una diferencia entre los resultados registrados de aproximadamente 614 ms para 30 usuarios y el resultado cercano a 21 ms mencionado en el análisis posterior del informe. Para evitar conclusiones incorrectas, estos valores deben identificarse por separado según la ejecución, la versión del código y la configuración utilizada.

Hasta que se verifiquen los resultados, no corresponde afirmar que el criterio de aceptación se cumple después de la corrección.

---

# Parte 6. Integración continua con GitHub Actions

## 6.1 Objetivo

La integración continua permite ejecutar verificaciones automáticas cada vez que se incorporan cambios al repositorio.

El objetivo del pipeline es detectar errores funcionales y problemas de seguridad antes de aceptar cambios que puedan afectar la estabilidad del proyecto.

## 6.2 Ejecución registrada

Enlace a la ejecución de GitHub Actions:

[Consultar ejecución del pipeline en GitHub Actions](https://github.com/jucarvajalg-jpg/auy1102-ep2-Carvajal-Guaquiante_2/actions/runs/39053414367/job/117456428004)

La ejecución debe revisarse para comprobar qué pruebas se ejecutaron, cuáles aprobaron y cuáles fallaron.

## 6.3 Puertas de calidad recomendadas

| Orden | Herramienta | Objetivo | Criterio |
|---:|---|---|---|
| 1 | pytest | Comprobar el funcionamiento de las funcionalidades y detectar regresiones. | Todas las pruebas deben aprobar. |
| 2 | Bandit | Detectar patrones potencialmente inseguros en el código. | Revisar los hallazgos y evitar que vulnerabilidades graves conocidas pasen inadvertidas. |
| 3 | Flake8 | Mantener la consistencia del código Python. | No deben quedar infracciones no justificadas. |
| 4 | pip-audit | Revisar vulnerabilidades conocidas en dependencias. | Verificar y documentar los hallazgos pendientes. |

El orden de las etapas puede ajustarse según los requisitos del encargo. Las comprobaciones más rápidas y fundamentales deben ejecutarse temprano para detectar problemas antes de invertir tiempo en etapas posteriores.

---

# Parte 7. Análisis y conclusiones

## 7.1 Análisis estático y análisis dinámico

Las herramientas utilizadas cumplen funciones complementarias.

| Tipo de análisis | Herramientas | Qué comprueba | Limitaciones |
|---|---|---|---|
| Análisis estático | Flake8 | Estilo, formato y determinados problemas de calidad del código. | No demuestra que la lógica de negocio sea correcta. |
| Análisis estático de seguridad | Bandit | Patrones potencialmente inseguros en el código Python. | Puede generar falsos positivos y no detectar todas las vulnerabilidades. |
| Auditoría de dependencias | pip-audit | Vulnerabilidades conocidas en paquetes instalados. | No detecta todos los defectos del código propio ni vulnerabilidades desconocidas. |
| Pruebas automatizadas | pytest | Comportamiento de las funciones en los escenarios cubiertos por las pruebas. | No garantiza que los casos no probados funcionen correctamente. |
| Pruebas de carga | Script de carga del proyecto | Latencia, solicitudes por segundo y errores bajo concurrencia. | No garantiza por sí sola la corrección funcional ni la seguridad del sistema. |

El análisis estático permite detectar determinados problemas sin ejecutar la aplicación. Por ejemplo, Bandit puede señalar el uso de `eval()` sin necesidad de ejecutar la ruta de código correspondiente.

Las pruebas dinámicas permiten observar el comportamiento real del sistema. Las pruebas unitarias verifican casos específicos, mientras que las pruebas de carga ayudan a identificar problemas que aparecen cuando múltiples solicitudes se procesan simultáneamente.

La combinación de ambos enfoques ofrece una evaluación más completa que utilizar una sola herramienta.

## 7.2 Prevención de regresiones

Las pruebas unitarias creadas para usuarios, préstamos, multas y catálogo ayudan a detectar regresiones después de modificar el código.

En el módulo de usuarios, las pruebas de registro, búsqueda, autenticación y tokens permiten comprobar que los cambios relacionados con la seguridad no alteren el funcionamiento esperado.

| Área | Pruebas o controles | Objetivo |
|---|---|---|
| Registro de usuarios | Registro y búsqueda de usuarios. | Comprobar que los usuarios puedan registrarse y consultarse correctamente. |
| Consultas SQL | Entradas con comillas y cadenas manipuladas. | Comprobar que los datos no alteren la estructura de las consultas. |
| Autenticación | Contraseña correcta e incorrecta. | Verificar el comportamiento de la autenticación. |
| Contraseñas | Pruebas del mecanismo de hash y verificación. | Comprobar que la autenticación sea compatible con el almacenamiento seguro de contraseñas. |
| Tokens | Generación y validación de tokens. | Comprobar el comportamiento esperado del mecanismo de seguridad. |

Una prueba de regresión es especialmente importante cuando se reemplazan mecanismos de seguridad. Por ejemplo, cambiar el algoritmo de almacenamiento de contraseñas requiere comprobar tanto la creación de nuevas credenciales como su verificación durante el inicio de sesión.

## 7.3 Propuesta de prueba de integración

Se propone una prueba de integración que conecte el registro de un usuario con el cálculo de una devolución y la generación de una notificación.

El objetivo es comprobar que los módulos funcionen correctamente cuando interactúan entre sí.

### Flujo propuesto

1. Crear una base de datos SQLite temporal para la prueba.
2. Registrar un usuario de prueba.
3. Recuperar los datos del usuario registrado.
4. Calcular la fecha de devolución según el tipo de usuario.
5. Generar la notificación asociada al préstamo.
6. Verificar que el mensaje contenga el nombre, título del libro y fecha de devolución correctos.

### Criterios de aceptación

| Criterio | Resultado esperado |
|---|---|
| Registro del usuario | El usuario queda almacenado correctamente en SQLite. |
| Recuperación de datos | Los datos recuperados coinciden con los registrados. |
| Cálculo de devolución | La fecha coincide con las reglas del tipo de usuario. |
| Generación de notificación | El mensaje contiene los datos correctos del préstamo. |
| Aislamiento de la prueba | La base de datos temporal no modifica datos reales del proyecto. |
| Tiempo de ejecución | La prueba debe ejecutarse en menos de 1 segundo, si el entorno y la implementación lo permiten. |

Esta prueba es una propuesta de integración y no debe presentarse como ejecutada hasta que exista una implementación y un resultado real.

## 7.4 Evaluación de las herramientas de calidad

| Herramienta | Qué detecta | Etapa del ciclo de vida o pipeline | Qué no detecta | Costo de no utilizarla |
|---|---|---|---|---|
| pytest | Resultados incorrectos en los casos de prueba definidos. | Desarrollo e integración continua. | Casos no cubiertos y algunos problemas de concurrencia. | Defectos funcionales pueden llegar al usuario. |
| Flake8 | Problemas de estilo, imports sin uso y determinadas infracciones de calidad. | Codificación e integración continua. | Errores de negocio y vulnerabilidades complejas. | Mayor dificultad de mantenimiento y lectura. |
| Bandit | Patrones de código potencialmente inseguros. | Análisis estático de seguridad. | Todas las vulnerabilidades posibles y errores de lógica. | Aumenta el riesgo de prácticas inseguras en el código. |
| pip-audit | Vulnerabilidades conocidas en dependencias. | Gestión de dependencias e integración continua. | Defectos propios y vulnerabilidades desconocidas. | Las dependencias pueden permanecer vulnerables. |
| Pruebas de carga | Latencia, capacidad de procesamiento y errores bajo concurrencia. | Pruebas de sistema y rendimiento. | Corrección funcional completa y seguridad. | Los problemas de rendimiento pueden descubrirse cuando el sistema ya está en uso. |

Cada herramienta aborda una dimensión diferente de la calidad. Por ello, ninguna reemplaza por completo a las demás.

## 7.5 Selección de dos puertas de calidad

Si solo fuera posible mantener dos puertas de calidad obligatorias en el pipeline, se priorizarían pytest y Bandit.

### 1. pytest

Permite detectar defectos funcionales y prevenir regresiones. Las pruebas automatizadas comprueban que las funcionalidades principales sigan funcionando después de modificar el código.

### 2. Bandit

Permite detectar patrones potencialmente inseguros sin ejecutar la aplicación. Ayuda a identificar tempranamente prácticas que requieren corrección o revisión, como el uso de `eval()`, comandos del sistema y consultas SQL construidas mediante cadenas.

Esta selección prioriza la detección de errores funcionales y riesgos de seguridad. No obstante, Flake8, pip-audit y las pruebas de carga siguen siendo importantes para obtener una evaluación más completa del proyecto.

---

# Conclusiones generales

La evaluación de BiblioTech permitió identificar defectos funcionales, problemas de calidad del código, riesgos de seguridad y limitaciones de rendimiento.

En las pruebas unitarias se corrigieron casos relacionados con la validación ISBN, el cálculo de multas y las fechas de devolución. Las pruebas agregadas también permitieron cubrir valores límite y entradas no válidas, fortaleciendo la detección de regresiones.

El análisis estático con Flake8 permitió identificar y corregir infracciones relacionadas con el formato, imports innecesarios, variables sin uso y manejo de excepciones. Por su parte, Bandit señaló patrones que requerían revisión de seguridad, mientras que pip-audit identificó vulnerabilidades conocidas en dependencias.

La revisión manual destacó la importancia de validar las rutas utilizadas para los respaldos y de utilizar un mecanismo apropiado para proteger las contraseñas. Estas medidas deben verificarse en la implementación final, además de comprobar que las correcciones no introduzcan regresiones.

En cuanto al rendimiento, los resultados registrados muestran que la versión evaluada no cumple el criterio de latencia p95 inferior a 500 ms con 30 usuarios simultáneos. Las pruebas de estrés también registraron errores bajo cargas mayores. Por este motivo, es necesario mantener separados los resultados de cada ejecución y verificar las mediciones posteriores antes de declarar cumplido el criterio de aceptación.

Finalmente, la integración continua permite automatizar las comprobaciones y detectar problemas antes de incorporar cambios al proyecto. La combinación de pruebas unitarias, análisis estático, auditoría de dependencias y pruebas de rendimiento contribuye a desarrollar un sistema más confiable, seguro y mantenible.

## Resumen de resultados

| Área evaluada | Resultado registrado | Estado |
|---|---|---|
| Pruebas unitarias de ISBN | 9 aprobadas después de la corrección. | Corregido según los resultados proporcionados. |
| Pruebas de multas | 7 aprobadas después de la corrección. | Corregido según los resultados proporcionados. |
| Pruebas de devolución | 6 aprobadas después de la corrección. | Corregido según los resultados proporcionados. |
| Flake8 | Sin infracciones en la ejecución final registrada. | Aprobado según el informe. |
| Bandit | Se identificaron varios patrones inseguros que requerían corrección. | Requiere confirmar el resultado final del análisis. |
| pip-audit | Se registraron 36 vulnerabilidades iniciales. | Requiere confirmar el resultado después de actualizar las dependencias. |
| Prueba de carga con 30 usuarios | p95 registrado de 614 ms en la ejecución posterior descrita. | No cumple el límite de 500 ms. |
| Prueba de estrés | Se registraron errores con 100, 300 y 500 usuarios. | Requiere análisis de los errores y nuevas mediciones. |
| Integración continua | Se dispone de un enlace a una ejecución de GitHub Actions. | Verificar el resultado de la ejecución. |

**Conclusión final:** la evaluación permitió identificar y abordar distintos problemas de calidad en BiblioTech. Para cerrar el proceso de validación, es necesario confirmar los resultados finales de seguridad y dependencias, verificar la implementación real del almacenamiento de contraseñas y reconciliar las mediciones de rendimiento antes de declarar que se cumplen todos los criterios de aceptación.
