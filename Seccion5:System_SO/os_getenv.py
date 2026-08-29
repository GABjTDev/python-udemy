"""
Ejemplo de acceso a variables de entorno y al identificador del proceso.

Uso básico (ejecutando el comando desde esta carpeta):
    python3 os_getenv.py

Para definir variables solo durante esta ejecución (Linux/macOS), se escriben
antes del comando de Python:
    OTRA_VAR="un valor" JAVA_HOME_II="/ruta/a/java" python3 os_getenv.py

Si se escribieran después de ``os_getenv.py``, Python las recibiría como
argumentos del script y ``os.getenv()`` no podría leerlas.

En PowerShell se definen antes de ejecutar el archivo:
    $env:OTRA_VAR = "un valor"
    python Seccion5:System_SO/os_getenv.py
"""

# El módulo os permite interactuar con funciones ofrecidas por el sistema
# operativo, como variables de entorno, rutas y procesos.
import os

# os.getenv(nombre) busca una variable de entorno y devuelve su valor como str.
# PATH contiene los directorios donde el sistema busca programas ejecutables.
# Si una variable no existe, getenv devuelve None (a menos que se indique un
# segundo argumento como valor predeterminado).
path = os.getenv('PATH')
print(path)

# Estas variables dependen de la configuración del equipo. Por eso es normal
# que se imprima None cuando JAVA_HOME_II u OTRA_VAR no están definidas.
print(os.getenv('JAVA_HOME_II'))
print(os.getenv('OTRA_VAR'))

# getpid() devuelve el Process ID (PID) del proceso de Python que está
# ejecutando este script. El sistema asigna uno distinto en cada ejecución.
print(os.getpid())
