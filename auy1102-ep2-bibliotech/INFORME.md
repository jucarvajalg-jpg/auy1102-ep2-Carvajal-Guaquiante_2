# Informe de calidad: BiblioTech

## Integrantes

| Nombre | Usuario de GitHub |
|---|---|
| | |
| | |

## Parte 1. Línea base

Resultado de cada herramienta ANTES de hacer cambios.

| Herramienta | Comando | Resultado (copiar la línea de resumen) |
|---|---|---|
| pytest | `python -m pytest -v` | | 
|Resualtado|
================================================== test session starts =========================================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\jpmot\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech
plugins: platformdirs-4.13.3
collected 19 items                                                                                                                                                                            
tests/test_catalogo.py::test_isbn_con_guiones_es_valido PASSED                                                                                                                          [  5%]
tests/test_catalogo.py::test_isbn_chileno_es_valido PASSED                                                                                                                              [ 10%]
tests/test_catalogo.py::test_isbn_sin_guiones_es_valido PASSED                                                                                                                          [ 15%]
tests/test_catalogo.py::test_isbn_con_verificador_cero_es_valido FAILED                                                                                                                 [ 21%]
tests/test_catalogo.py::test_isbn_sin_guiones_con_verificador_cero_es_valido FAILED                                                                                                     [ 26%]
tests/test_catalogo.py::test_isbn_con_verificador_incorrecto_es_invalido PASSED                                                                                                         [ 31%]
tests/test_catalogo.py::test_isbn_de_12_digitos_es_invalido PASSED                                                                                                                      [ 36%]
tests/test_catalogo.py::test_isbn_con_letras_es_invalido PASSED                                                                                                                         [ 42%]
tests/test_catalogo.py::test_texto_vacio_es_invalido PASSED                                                                                                                             [ 47%]
tests/test_devolucion.py::test_estudiante_devuelve_en_7_dias FAILED                                                                                                                     [ 52%]
tests/test_devolucion.py::test_docente_devuelve_en_14_dias FAILED                                                                                                                       [ 57%]
tests/test_multas.py::test_estudiante_con_3_dias_de_atraso_paga_1500 PASSED                                                                                                             [ 63%]
tests/test_multas.py::test_multa_alta_queda_en_el_tope PASSED                                                                                                                           [ 68%]
tests/test_multas.py::test_docente_con_5_dias_paga_solo_3 PASSED                                                                                                                        [ 73%]
tests/test_usuarios.py::test_registrar_y_buscar_usuario PASSED                                                                                                                          [ 78%]
tests/test_usuarios.py::test_buscar_usuario_inexistente_devuelve_none PASSED                                                                                                            [ 84%]
tests/test_usuarios.py::test_autenticar_con_clave_correcta PASSED                                                                                                                       [ 89%]
tests/test_usuarios.py::test_autenticar_con_clave_incorrecta PASSED                                                                                                                     [ 94%]
tests/test_usuarios.py::test_token_tiene_32_caracteres_y_no_se_repite PASSED                                                                                                            [100%]
=============================================== FAILURE==========================================================
============================================= short test summary info ==================================================
FAILED tests/test_catalogo.py::test_isbn_con_verificador_cero_es_valido - AssertionError: assert False is True
FAILED tests/test_catalogo.py::test_isbn_sin_guiones_con_verificador_cero_es_valido - AssertionError: assert False is True
FAILED tests/test_devolucion.py::test_estudiante_devuelve_en_7_dias - NotImplementedError: Parte 2C: implementa calcular_fecha_devolucion()
FAILED tests/test_devolucion.py::test_docente_devuelve_en_14_dias - NotImplementedError: Parte 2C: implementa calcular_fecha_devolucion()
=========================================== 4 failed, 15 passed in 0.38s ===============================================

| Flake8 | `python -m flake8 --count` | |
|Resualtado|
.\bibliotech\prestamos.py:2:1: F401 'os' imported but unused
.\bibliotech\prestamos.py:44:48: E251 unexpected spaces around keyword / parameter equals
.\bibliotech\prestamos.py:44:50: E251 unexpected spaces around keyword / parameter equals
.\bibliotech\prestamos.py:48:21: E711 comparison to None should be 'if cond is None:'
.\bibliotech\prestamos.py:50:101: E501 line too long (117 > 100 characters)
.\bibliotech\reportes.py:4:1: F401 'sys' imported but unused
.\bibliotech\reportes.py:25:13: F841 local variable 'total' is assigned to but never used
.\bibliotech\reportes.py:27:5: E722 do not use bare 'except'
.\bibliotech\usuarios.py:25:101: E501 line too long (101 > 100 characters)

| Bandit | `python -m bandit -r bibliotech` | Alta: · Media: · Baja: |
|Resualtado|
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.12.10
Run started:2026-10-16 22:24:22.476618+00:00

Test results:
>> Issue: [B701:jinja2_autoescape_false] By default, jinja2 sets autoescape to False. Consider using autoescape=True or use the select_autoescape function to mitigate XSS vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b701_jinja2_autoescape_false.html
   Location: bibliotech\notificaciones.py:12:14
11      def armar_mensaje(nombre, titulo, fecha):
12          entorno = Environment()
13          return entorno.from_string(PLANTILLA).render(nombre=nombre, titulo=titulo, fecha=fecha)

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: bibliotech\notificaciones.py:17:16
16      def enviar_aviso(url_webhook, mensaje):
17          respuesta = requests.post(url_webhook, json={"texto": mensaje})
18          return respuesta.status_code == 200

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: bibliotech\reportes.py:12:11
11          """
12          return eval(formula, {}, datos)
13

--------------------------------------------------
>> Issue: [B605:start_process_with_a_shell] Starting a process with a shell, possible injection detected, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b605_start_process_with_a_shell.html
   Location: bibliotech\reportes.py:17:4
16          """Copia la base de datos a la carpeta de respaldos."""
17          os.system("cp biblioteca.db respaldos/" + nombre_archivo)
18

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: bibliotech\usuarios.py:20:11
19      def _hash_clave(clave):
20          return hashlib.md5(clave.encode()).hexdigest()
21

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Low
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: bibliotech\usuarios.py:25:17
24          """Registra un usuario nuevo guardando su clave como hash."""
25          consulta = f"INSERT INTO usuarios VALUES ('{rut}', '{nombre}', '{_hash_clave(clave)}', '{tipo}')"
26          conexion.execute(consulta)

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Low
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: bibliotech\usuarios.py:32:15
31          """Devuelve (rut, nombre, tipo) del usuario, o None si no existe."""
32          consulta = "SELECT rut, nombre, tipo FROM usuarios WHERE rut = '" + rut + "'"
33          return conexion.execute(consulta).fetchone()

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b311-random
   Location: bibliotech\usuarios.py:49:19
48          letras = "abcdefghijklmnopqrstuvwxyz0123456789"
49          return "".join(random.choice(letras) for _ in range(32))

--------------------------------------------------

Code scanned:
        Total lines of code: 132
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 1
                Medium: 4
                High: 3
        Total issues (by confidence):
                Undefined: 0
                Low: 3
                Medium: 0
                High: 5
Files skipped (0):

| pip-audit | `python -m pip_audit -r requirements.txt --no-deps --disable-pip` | |
|Resultado|
WARNING:pip_audit._cli:--no-deps is supported, but users are encouraged to fully hash their pinned dependencies
WARNING:pip_audit._cli:Consider using a tool like `pip-compile`: https://pip-tools.readthedocs.io/en/latest/#using-hashes
Found 36 known vulnerabilities in 3 packages
Name     Version ID              Fix Versions
-------- ------- --------------- -------------
requests 2.25.1  PYSEC-2023-74   2.31.0
requests 2.25.1  PYSEC-2023-74   2.31.0
requests 2.25.1  PYSEC-2026-1873 2.32.0
requests 2.25.1  PYSEC-2026-1872 2.32.4
requests 2.25.1  PYSEC-2026-2275 2.33.0
requests 2.25.1  PYSEC-2026-1873 2.32.0
requests 2.25.1  PYSEC-2026-1872 2.32.4
requests 2.25.1  PYSEC-2026-2275 2.33.0
urllib3  1.26.5  PYSEC-2026-1995 1.26.19,2.2.2
urllib3  1.26.5  PYSEC-2023-192  1.26.17,2.0.6
urllib3  1.26.5  PYSEC-2023-192  1.26.17,2.0.6
urllib3  1.26.5  PYSEC-2023-212  1.26.18,2.0.7
urllib3  1.26.5  PYSEC-2023-212  1.26.18,2.0.7
urllib3  1.26.5  PYSEC-2026-1999 2.5.0
urllib3  1.26.5  PYSEC-2026-1998 2.6.0
urllib3  1.26.5  PYSEC-2026-1994 2.6.0
urllib3  1.26.5  PYSEC-2026-1996 2.6.3
urllib3  1.26.5  PYSEC-2026-141  2.7.0
urllib3  1.26.5  PYSEC-2026-141  2.7.0
urllib3  1.26.5  PYSEC-2026-1999 2.5.0
urllib3  1.26.5  PYSEC-2026-1998 2.6.0
urllib3  1.26.5  PYSEC-2026-1995 1.26.19,2.2.2
urllib3  1.26.5  PYSEC-2026-1994 2.6.0
urllib3  1.26.5  PYSEC-2026-1996 2.6.3
urllib3  1.26.5  PYSEC-2026-4177 2.8.0
urllib3  1.26.5  PYSEC-2026-4175 2.8.0
jinja2   2.11.2  PYSEC-2021-66   2.11.3
jinja2   2.11.2  PYSEC-2021-66   2.11.3
jinja2   2.11.2  PYSEC-2026-1473 3.1.3
jinja2   2.11.2  PYSEC-2026-1474 3.1.4
jinja2   2.11.2  PYSEC-2026-1475 3.1.5
jinja2   2.11.2  PYSEC-2026-1471 3.1.6
jinja2   2.11.2  PYSEC-2026-1473 3.1.3
jinja2   2.11.2  PYSEC-2026-1471 3.1.6
jinja2   2.11.2  PYSEC-2026-1474 3.1.4
jinja2   2.11.2  PYSEC-2026-1475 3.1.5


## Parte 2. Pruebas unitarias

### Defectos encontrados catalogo.py

| Función | Prueba que lo evidencia | Causa del defecto | Corrección aplicada |
|catalogo.py| python -m pytest tests/test_catalogo.py -v|
|Causa del defecto|
================================================ FAILURES ==========================================
__________________________________________________________________________ test_isbn_con_verificador_cero_es_valido __________________________________________________________________________

    def test_isbn_con_verificador_cero_es_valido():
>       assert validar_isbn13("978-956-00-0004-0") is True
E       AssertionError: assert False is True
E        +  where False = validar_isbn13('978-956-00-0004-0')

tests\test_catalogo.py:20: AssertionError
____________________________________________________________________ test_isbn_sin_guiones_con_verificador_cero_es_valido ____________________________________________________________________

    def test_isbn_sin_guiones_con_verificador_cero_es_valido():
>       assert validar_isbn13("9789560000200") is True
E       AssertionError: assert False is True
E        +  where False = validar_isbn13('9789560000200')

tests\test_catalogo.py:24: AssertionError
============================================================================================================
|Correccion aplicada|
Motivo: Si suma % 10 resultaba en 0 (por ejemplo, suma = 100), la fórmula anterior calculaba 10 - 0 = 10. Al comparar 10 con el 13.º dígito (que siempre es un carácter individual de 0 a 9), la validación fallaba. Agregar el módulo % 10 final convierte el 10 en 0 automáticamente, mientras que cualquier otro número entre 1 y 9 se mantiene igual (ejemplo: 8 % 10 = 8).

PS C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech> python -m pytest tests/test_catalogo.py -v
============================================ test session starts ===============================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\jpmot\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech
plugins: platformdirs-4.13.3
collected 9 items                                                                                                                                                                       

tests/test_catalogo.py::test_isbn_con_guiones_es_valido PASSED                                                                                                                    [ 11%]
tests/test_catalogo.py::test_isbn_chileno_es_valido PASSED                                                                                                                        [ 22%]
tests/test_catalogo.py::test_isbn_sin_guiones_es_valido PASSED                                                                                                                    [ 33%]
tests/test_catalogo.py::test_isbn_con_verificador_cero_es_valido PASSED                                                                                                           [ 44%]
tests/test_catalogo.py::test_isbn_sin_guiones_con_verificador_cero_es_valido PASSED                                                                                               [ 55%]
tests/test_catalogo.py::test_isbn_con_verificador_incorrecto_es_invalido PASSED                                                                                                   [ 66%]
tests/test_catalogo.py::test_isbn_de_12_digitos_es_invalido PASSED                                                                                                                [ 77%]
tests/test_catalogo.py::test_isbn_con_letras_es_invalido PASSED                                                                                                                   [ 88%]
tests/test_catalogo.py::test_texto_vacio_es_invalido PASSED                                                                                                                       [100%]

============================================== 9 passed in 0.08s ==========================================


| Función | Prueba que lo evidencia | Causa del defecto | Corrección aplicada |
|test_multas.py| python -m pytest tests/test_multas.py -v|
|Resultado|
PS C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech> python -m pytest tests/test_multas.py  -v
============================================ test session starts =======================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\jpmot\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech
plugins: platformdirs-4.13.3
collected 3 items                                                                                                                                                                       
tests/test_multas.py::test_estudiante_con_3_dias_de_atraso_paga_1500 PASSED                                                                                                       [ 33%]
tests/test_multas.py::test_multa_alta_queda_en_el_tope PASSED                                                                                                                     [ 66%]
tests/test_multas.py::test_docente_con_5_dias_paga_solo_3 PASSED                                                                                                                  [100%]
### Defectos encontrados teste_multas.py

| Función | Prueba que lo evidencia | Causa del defecto | Corrección aplicada |
|test_multas.py| python -m pytest tests/test_multas.py -v| No comunica errores
|resultado|
PS C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech> python -m pytest tests/test_multas.py  -v
=========================================== test session starts =========================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\jpmot\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech
plugins: platformdirs-4.13.3
collected 3 items                                                                                                                                                                       
tests/test_multas.py::test_estudiante_con_3_dias_de_atraso_paga_1500 PASSED                                                                                                       [ 33%]
tests/test_multas.py::test_multa_alta_queda_en_el_tope PASSED                                                                                                                     [ 66%]
tests/test_multas.py::test_docente_con_5_dias_paga_solo_3 PASSED                                                                                                                  [100%]

========================================== 3 passed in 0.03s ==================================================
### Pruebas agregadas

| Archivo | Nombre de la prueba | Qué caso o valor límite cubre |
|test_multas.py|def test_dias_atraso_negativos_lanza_value_error():|Valida que una cantidad negativa de días de atraso lance ValueError.|
|test_multas.py|def test_sin_atraso_paga_cero():Valida que con 0 días de atraso la multa sea $0.|
|test_multas.py|def test_docente_dentro_del_periodo_de_gracia_paga_cero():|Valida que un docente con 1 o 2 días de atraso pague $0 y no montos negativos.|
|test_multas.py|def test_tope_multa_exacto_para_docente():|Valida que la multa máxima de $10.000 se aplique correctamente al docente tras la gracia.|
Resultado final de `pytest tests/test_multas.py -v`:
========================================== test session starts ============================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\jpmot\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech
plugins: platformdirs-4.13.3
collected 7 items                                                                                                                                                                       
tests/test_multas.py::test_estudiante_con_3_dias_de_atraso_paga_1500 PASSED                                                                                                       [ 14%]
tests/test_multas.py::test_multa_alta_queda_en_el_tope PASSED                                                                                                                     [ 28%]
tests/test_multas.py::test_docente_con_5_dias_paga_solo_3 PASSED                                                                                                                  [ 42%]
tests/test_multas.py::test_dias_atraso_negativos_lanza_value_error FAILED                                                                                                         [ 57%]
tests/test_multas.py::test_sin_atraso_paga_cero FAILED                                                                                                                            [ 71%]
tests/test_multas.py::test_docente_dentro_del_periodo_de_gracia_paga_cero FAILED                                                                                                  [ 85%]
tests/test_multas.py::test_tope_multa_exacto_para_docente PASSED                                                                                                                  [100%]
================================================= FAILURES ======================================================
_________________________________________ test_dias_atraso_negativos_lanza_value_error _______________________________________

    def test_dias_atraso_negativos_lanza_value_error():
        """Valida que una cantidad negativa de días de atraso lance ValueError."""
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

tests\test_multas.py:26: Failed
____________________________________ test_sin_atraso_paga_cero ___________________________________________

    def test_sin_atraso_paga_cero():
        """Valida que con 0 días de atraso la multa sea $0."""
        assert calcular_multa(0, "estudiante") == 0
>       assert calcular_multa(0, "docente") == 0
E       AssertionError: assert -1000 == 0
E        +  where -1000 = calcular_multa(0, 'docente')

tests\test_multas.py:36: AssertionError
___________________________________ test_docente_dentro_del_periodo_de_gracia_paga_cero ______________________________________

    def test_docente_dentro_del_periodo_de_gracia_paga_cero():
        """Valida que un docente con 1 o 2 días de atraso pague $0 y no montos negativos."""
>       assert calcular_multa(1, "docente") == 0
E       AssertionError: assert -500 == 0
E        +  where -500 = calcular_multa(1, 'docente')

tests\test_multas.py:41: AssertionError
======================================= short test summary info =========================================
FAILED tests/test_multas.py::test_dias_atraso_negativos_lanza_value_error - Failed: DID NOT RAISE ValueError
FAILED tests/test_multas.py::test_sin_atraso_paga_cero - AssertionError: assert -1000 == 0
FAILED tests/test_multas.py::test_docente_dentro_del_periodo_de_gracia_paga_cero - AssertionError: assert -500 == 0
======================================== 3 failed, 4 passed in 0.21s =========================================

|codigo corregido|
=========================================== test session starts ==========================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\jpmot\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech
plugins: platformdirs-4.13.3
collected 7 items                                                                                                                                                                       

tests/test_multas.py::test_estudiante_con_3_dias_de_atraso_paga_1500 PASSED                                                                                                       [ 14%]
tests/test_multas.py::test_multa_alta_queda_en_el_tope PASSED                                                                                                                     [ 28%]
tests/test_multas.py::test_docente_con_5_dias_paga_solo_3 PASSED                                                                                                                  [ 42%]
tests/test_multas.py::test_dias_atraso_negativos_lanza_value_error PASSED                                                                                                         [ 57%]
tests/test_multas.py::test_sin_atraso_paga_cero PASSED                                                                                                                            [ 71%]
tests/test_multas.py::test_docente_dentro_del_periodo_de_gracia_paga_cero PASSED                                                                                                  [ 85%]
tests/test_multas.py::test_tope_multa_exacto_para_docente PASSED                                                                                                                  [100%]

=========================================== 7 passed in 0.04s ===========================================

### Defectos encontrados teste_devoluciones.py

| Archivo | Nombre de la prueba | Qué caso o valor límite cubre |
|test_devoluciones.py|def test_devolucion_que_cae_sabado_se_mueve_al_lunes():|Sábado 3 de octubre de 2026 + 7 días = Sábado 10 de octubre -> se mueve al Lunes 12|
|test_devoluciones.py|def test_devolucion_que_cae_domingo_se_mueve_al_lunes():|Domingo 4 de octubre de 2026 + 7 días = Domingo 11 de octubre -> se mueve al Lunes 12|
|test_devoluciones.py|def test_docente_devolucion_que_cae_fin_de_semana_se_mueve_al_lunes():|Sábado 10 de octubre de 2026 + 14 días = Sábado 24 de octubre -> se mueve al Lunes 26|
|test_devoluciones.py|def test_tipo_usuario_invalido_lanza_value_error():|Cualquier tipo distinto de 'estudiante' o 'docente' debe lanzar ValueError|
Resultado final de `pytest tests/devoluciones.py -v`:
PS C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech> pytest tests/test_devolucion.py -v
========================================= test session starts =========================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\jpmot\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jpmot\Documents\Evaluacion_parcial_2\auy1102-ep2-bibliotech
plugins: platformdirs-4.13.3
collected 6 items                                                                                                                                                                       

tests/test_devolucion.py::test_estudiante_devuelve_en_7_dias PASSED                                                                                                               [ 16%]
tests/test_devolucion.py::test_docente_devuelve_en_14_dias PASSED                                                                                                                 [ 33%]
tests/test_devolucion.py::test_devolucion_que_cae_sabado_se_mueve_al_lunes PASSED                                                                                                 [ 50%]
tests/test_devolucion.py::test_devolucion_que_cae_domingo_se_mueve_al_lunes PASSED                                                                                                [ 66%]
tests/test_devolucion.py::test_docente_devolucion_que_cae_fin_de_semana_se_mueve_al_lunes PASSED                                                                                  [ 83%]
tests/test_devolucion.py::test_tipo_usuario_invalido_lanza_value_error PASSED                                                                                                     [100%]

============================================= 6 passed in 0.09s ========================================
## Parte 3. Análisis estático (Flake8)

| Código | Archivo:línea | Qué significa | Cómo lo corrigieron |
|E501|.\bibliotech\prestamos.py:65|La línea excede el límite máximo permitido de caracteres|Divide la línea o la cadena de texto en varias líneas usando paréntesis.|
|W292|.\bibliotech\prestamos.py:68|El archivo finaliza directamente en la última línea de código sin una línea vacía al final|Ve al final de ambos archivos, presiona la tecla Enter para agregar un salto de línea en blanco y guarda el archivo.|
|F401|.\bibliotech\reportes.py:4|Se importó la librería sys, pero no se utiliza en ninguna parte del código.|Borra la línea import sys (o remueve sys si está dentro de una importación múltiple).|
|F841|.\bibliotech\reportes.py:25|Se definió la variable total, pero nunca se lee, retorna o utiliza en el resto de la función.|Elimina la variable si no es necesaria, o utiliza su valor más adelante (por ejemplo, en un return total).|
|E722|.\bibliotech\reportes.py:27|e utilizó un bloque except: sin especificar la clase de error a capturar|Reemplaza except: especificando el tipo de excepción genérica Exception o una específica (como ValueError o KeyError).|
|W293|.\tests\test_devolucion.py:45|La línea 45 de test_devolucion.py parece estar vacía, pero contiene espacios o sangría invisibles|Ve a la línea 45 de tests\test_devolucion.py, borra todos los espacios ocultos en esa línea dejándola totalmente limpia|
|W292|.\tests\test_devolucion.py:44|El archivo termina directamente en la línea 45 sin incluir un salto de línea final al final del archivo|Ve al final de la línea 45, presiona la tecla Enter para generar una línea en blanco extra (línea 46) y guarda el archivo.|


Resultado final de `python -m flake8 --count`:
No entrega ningun error 

## Parte 4. Análisis de seguridad

### 4A. Bandit

| ID | Severidad / Confianza | Archivo:línea | Riesgo concreto en BiblioTech | Corrección aplicada |
|B701|alta / alta|bibliotech\notificaciones.py:12:14|Al deshabilitar el escape automático en plantillas Jinja2, si los nombres de usuarios o títulos de libros contienen código HTML o scripts maliciosos, podrían ejecutarse al renderizar el mensaje|autoescape=select_autoescape() al instanciar el entorno de Jinja2.|

|B113|media / baja|bibliotech\notificaciones.py:17:16|La llamada HTTP no define un tiempo límite de espera. Si el servicio del webhook no responde, la aplicación puede quedar bloqueada indefinidamente, provocando una denegación de servicio (DoS).|Se agregó el argumento timeout=5 a la petición requests.post().|

|B307|media / alta|bibliotech\reportes.py:11:11|El uso de eval() permite la ejecución arbitraria de código Python si la fórmula o los datos son manipulados por un usuario malintencionado.|Se reemplazó la llamada a eval() utilizando ast.literal_eval para evaluaciones seguras de estructuras simples o parsing numérico controlado.|

|B605|alta / alta|bibliotech\reportes.py:16:4|Ejecutar comandos del sistema operativo mediante os.system() abre la puerta a inyecciones de comandos si nombre_archivo contiene caracteres especiales (como ; o &&), permitiendo que un atacante tome control del servidor.|Se reemplazó el comando del sistema operativo por la librería nativa de Python shutil.copy().|

|B324|alta / alta|bibliotech\usuarios.py:20:11|MD5 es un algoritmo de hashing obsoleto y vulnerable a colisiones y ataques de tablas arcoíris, lo que compromete la confidencialidad de las contraseñas guardadas.|Se reemplazó el algoritmo por hashlib.sha256().|

|B608|media / baja|bibliotech\usuarios.py:25:17|Concatenar cadenas directamente dentro de una sentencia SQL permite inyección SQL, exponiendo la base de datos a modificaciones no autorizadas o borrado masivo. |Se modificó la consulta para utilizar parámetros formateados seguros (?).|

|B608|media / baja|bibliotech\usuarios.py:32:15|Concatenar la variable rut en la consulta SELECT permite inyección SQL, facilitando la evasión de autenticación o la extracción ilegítima de datos de usuarios.|Se parametrizó la consulta sustituyendo la concatenación por la tupla de argumentos (rut,).|

|B311|baja / alta|bibliotech\usuarios.py:49:19|La librería estándar random es pseudoaleatoria y predecible, lo que no la hace apta para generar tokens de seguridad, identificadores o contraseñas temporales.|Se reemplazó el módulo random por secrets, diseñado específicamente para generación aleatoria criptográficamente segura.||

Pruebas de seguridad agregadas (nombre y qué demuestran):

# test_sql_injection_en_obtener_usuario:

En el código original: La consulta concatenaba directamente el string ("SELECT ... WHERE rut = '" + rut + "'"). Al buscar ' OR '1'='1, la consulta ejecutada terminaba siendo SELECT ... WHERE rut = '' OR '1'='1', devolviendo siempre al primer usuario registrado en la base de datos (bypass de autenticación/búsqueda).

Con la corrección: Al usar parámetros ?, SQLite busca literalmente el texto ' OR '1'='1 dentro de la columna RUT y devuelve None al no encontrarlo.

# test_registrar_usuario_con_comilla_simple_en_nombre:

En el código original: Concatenar 'Bernardo O'Higgins' generaba un error de sintaxis SQL en la cadena (INSERT INTO usuarios VALUES (..., 'Bernardo O'Higgins', ...)), ya que la comilla de "O'Higgins" cerraba el string prematuramente provocando un crash (sqlite3.OperationalError).

Con la corrección: La consulta parametrizada escapa el carácter especial de manera transparente y permite guardar nombres con apóstrofes o comillas sin fallar.


### 4B. pip-audit

| Paquete | Versión original | N° de vulnerabilidades | Versión actualizada |
|requests|2.25.1|8|2.33.0|
|urllib3|1.26.5|18|2.8.0|
|jinja2|2.11.2|10|3.1.6|
| | | | |

### 4C. Revisión manual

Problema de seguridad que las herramientas NO reportaron, dónde está, por qué es un riesgo y cómo lo corrigieron:
# Hallazgo 1: Path Traversal (Navegación de Directorios) en reportes.py
Ubicación: exportar_respaldo(nombre_archivo)

Descripción del problema: La función concatena nombre_archivo directamente en la ruta de destino (respaldos/ + nombre_archivo). Si un usuario ingresa una secuencia con salto de directorio como ../../etc/cron.d/malicioso o ../config.py, la aplicación escribirá o sobrescribirá archivos fuera del directorio respaldos/.

Riesgo para BiblioTech: Permite la modificación o sobrescritura arbitraria de archivos críticos del servidor o del sistema operativo.

Por qué Bandit no lo detectó: Bandit evalúa la seguridad de funciones concretas (como os.system), pero no valida si las cadenas pasadas como argumento a funciones estándar del sistema de archivos (shutil.copy) provienen de entradas no sanitizadas.

# Hallazgo 2: Hashing de Contraseñas sin Sal (Salt) en usuarios.py
Ubicación: _hash_clave(clave)

Descripción del problema: La función aplica hashlib.sha256() directamente sobre la contraseña limpia sin incluir un prefijo/sufijo aleatorio o secreto (salt). Dos usuarios con la misma clave generarán exactamente el mismo hash en la base de datos.

Riesgo para BiblioTech: Expone las credenciales a ataques por tablas precomputadas (Rainbow Tables) o ataques de diccionario inverso. Si se filtra la base de datos, un atacante puede averiguar las contraseñas originales de forma masiva.

Por qué Bandit no lo detectó: Bandit valida que el algoritmo utilizado no sea considerado débil (flagay MD5 o SHA1), pero no analiza la arquitectura lógica del hashing ni la presencia de mecanismos de salado (salting).

## Parte 5. Pruebas de carga y estrés

Criterio de aceptación: con 30 usuarios simultáneos, el 95% de las búsquedas responde en menos de 500 ms y no hay errores.

### 5A. Línea base (antes de corregir)

| Usuarios | Peticiones/s | p95 (ms) | Errores (%) | ¿Cumple? |
|---:|---:|---:|---:|:---:|
| 10       |  49         |164       | 0        | si cumple|
| 30       |  49         |613       |0         | no cumple
| 60       |  49         |1227      |0         | no cumple


### 5B. Diagnóstico y corrección

¿Qué observaron en las peticiones por segundo al aumentar los usuarios? ¿Qué línea de `carga/servidor.py` causaba el problema y por qué? ¿Cómo lo corrigieron?

| Usuarios | Peticiones/s | p95 (ms) | Errores (%) | ¿Cumple? |
|---:|---:|---:|---:|:---:|
| 30       | 49           |614       |     0       | No cumple |

R:  Se usa numero_visita y no visitas porque, cuando se arma la respuesta, otro hilo pudo haber cambiado visitas. La variable local guarda el número correcto de esta petición.
    pese a la correccion del codigo, la prueba  sigue fallando ya que no se cumple por el tiempo de la consulta, que es demasiado corto para que se pueda saturar el servidor.
    esto por seguir la REGLA DEL EXAMEN: no se permite modificar CAPACIDAD, TIEMPO_CONSULTA ni ESPERA_MAXIMA. estipulada en servidor.py

### 5C. Prueba de estrés

| Usuarios | Peticiones/s | p95 (ms) | Errores (%) | ¿Cumple? |

| 100      |     76      |  1310      |  359        | no cumple|
| 300      |     237     |  1311      | 2386        | no cumple
| 500      |     372     |  1315      | 4388        | no cumple 
| 
R: como resultado las pruebas por 100,300 y 500 usuario no cumple los requisitos debido a que pese que se corrigio el codigo, el examen tiene reglas de no modificar CAPACIDAD, TIEMPO_CONSULTA ni ESPERA_MAXIMA esto sumado a que el tiempo de la consulta  es demasiado corto para que se pueda saturar el servidor.

Punto de quiebre, cómo falla el sistema (lentitud o errores 503) y si se recupera:

## Parte 6. Pipeline de calidad

Enlace a la ejecución en verde de GitHub Actions:

## Parte 7. Análisis

### 7.1 Análisis estático y dinámico
Diferencien análisis estático y dinámico. Clasifiquen las cuatro herramientas usadas y den un defecto de este examen que solo podía encontrarse con cada tipo de análisis.

### 7.2 Pruebas de regresión
¿Qué es una prueba de regresión? Indiquen qué pruebas cumplieron ese rol durante la Parte 4 y qué habría pasado sin ellas.

### 7.3 Pruebas de integración, carga y estrés
a) Propongan una prueba de integración para BiblioTech: qué módulos probarían juntos, con qué herramienta y con qué criterio de aceptación medible.
b) Con los resultados de su Parte 5, expliquen la diferencia entre la prueba de carga y la prueba de estrés que ejecutaron. ¿Por qué el defecto del servidor no podía detectarse con pruebas unitarias? Con sus números, ¿qué le recomendarían a la biblioteca para el inicio de semestre?

### 7.4 Evaluación de herramientas

| Herramienta | Qué detecta | Etapa del ciclo de vida / del pipeline donde actúa | Qué NO detecta (limitación) | Costo de no usarla |
|---|---|---|---|---|
| pytest | | | | |
| Flake8 | | | | |
| Bandit | | | | |
| pip-audit | | | | |
| Prueba de carga (`prueba_carga.py`) | | | | |

### 7.5 Recomendación
Si el equipo de BiblioTech solo pudiera mantener dos puertas de calidad en su pipeline, ¿cuáles elegirían y en qué orden? Justifiquen con los conceptos de detección temprana y mejora continua.
