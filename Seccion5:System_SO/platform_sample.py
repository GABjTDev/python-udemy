"""
Muestra información del sistema operativo, Python y los argumentos recibidos.

Uso (ejecutando el comando desde esta carpeta):

    python3 platform_sample.py uno dos tres cuatro cinco seis

Los valores escritos después de ``platform_sample.py`` son los argumentos del
script. Este ejemplo accede directamente a las posiciones 1 a 6, por lo que se
deben enviar al menos seis argumentos para evitar un ``IndexError``.

En ``sys.argv``, la posición 0 contiene el nombre/ruta del script y las
posiciones siguientes contienen los argumentos escritos en la terminal.
Todos esos valores llegan como cadenas de texto (str).
"""

# platform ofrece información de alto nivel sobre el sistema y la máquina.
import platform
# sys permite consultar el intérprete e interactuar con su ejecución.
import sys
# locale permite consultar la configuración regional usada por el proceso.
import locale

# Nombre general del sistema operativo, por ejemplo: Linux, Windows o Darwin.
system = platform.system()
print(system)

# Versión informada por el sistema operativo. Su formato cambia según el SO.
version = platform.version()
print(version)

# Versión corta del intérprete de Python, por ejemplo "3.12.3".
print(platform.python_version())

# uname() agrupa varios datos: sistema, nodo/equipo, release, versión,
# arquitectura de la máquina y procesador.
print(platform.uname())

# machine() muestra la arquitectura, por ejemplo x86_64, AMD64 o arm64.
print(platform.machine())

# processor() intenta mostrar el nombre del procesador. Puede devolver una
# cadena vacía si el sistema operativo no proporciona esa información.
print(platform.processor())

# sys.version contiene información detallada de la versión y compilación de
# Python; sys.platform es un identificador breve del sistema (linux, win32...).
print(sys.version)
print(sys.platform)

# Ruta absoluta al ejecutable de Python que está ejecutando este archivo. Es
# útil para comprobar si se está usando un entorno virtual o el Python global.
print(sys.executable)

# Codificación de texto predeterminada de Python (normalmente "utf-8").
print(sys.getdefaultencoding())

# getlocale() devuelve la configuración regional como una tupla
# (idioma_región, codificación); getencoding() devuelve la codificación actual.
print(locale.getlocale())
print(locale.getencoding())

object_str = 'Hola que tal'

# getsizeof() informa el tamaño superficial del objeto en bytes. No suma el
# tamaño de otros objetos que este pudiera contener o referenciar.
print(sys.getsizeof(object_str))

# argv es la lista de argumentos de la línea de comandos. Estos accesos son
# directos: el script necesita seis argumentos además del nombre del archivo.
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv[5])
print(sys.argv[6])

# argv[0] siempre identifica el script que se solicitó ejecutar.
print(f'Script Name: {sys.argv[0]}')

# Antes de leer argumentos opcionales se puede comprobar len(sys.argv). El
# nombre del script también cuenta, por eso > 1 significa que existe argv[1].
# En este ejemplo los seis accesos anteriores ya exigen esos argumentos; estas
# condiciones sirven para mostrar la forma segura de tratarlos en otros casos.
if len(sys.argv) > 1:
    print('Primer argumento', sys.argv[1])
if len(sys.argv) > 2:
    print('Segundo argumento: ', sys.argv[2])
