"""
Ejemplo de salida estándar, salida de error, excepciones y códigos de salida.

Uso:
    python Seccion5:System_SO/system_sample.py

El código de salida puede consultarse justo después de ejecutarlo:
    python Seccion5:System_SO/system_sample.py
    echo $?                 # Linux/macOS

En PowerShell se consulta con:
    $LASTEXITCODE
"""

# datetime se usa para representar fechas y horas. Aquí se importa la clase
# directamente para poder escribir datetime.strptime(...) en vez de
# datetime.datetime.strptime(...).
from datetime import datetime

# sys da acceso a los flujos estándar y permite finalizar el programa con un
# código de salida que otro programa o el sistema operativo puede interpretar.
import sys

# stdout es la salida normal del programa. write(), a diferencia de print(),
# no agrega un salto de línea automáticamente; por eso se incluye "\n".
sys.stdout.write('Hola Mundo desde std out!\n')

# stderr es el canal reservado para errores y diagnósticos. La línea está
# comentada para que no se ejecute; se puede quitar el # para probarla.
# sys.stderr.write('Hola tenemos un problema de error!\n')

# print() también escribe en stdout por defecto y agrega un salto de línea.
print('Hola Mundo!')

# El bloque try intenta convertir una cadena con el formato año-mes-día en un
# objeto datetime. Cada letra de '%Y-%m-%d' describe la parte esperada:
# %Y = año con cuatro cifras, %m = mes y %d = día.
try:
    date_event = datetime.strptime('2026-09-18', '%Y-%m-%d')
    print(date_event)

# Si la fecha o el patrón no coinciden, strptime lanza ValueError. El error se
# captura para mostrar el diagnóstico por stderr y terminar de forma controlada.
except ValueError as err:
    sys.stderr.write(f'Error con el formato de fecha {err}\n')

    # Un código distinto de cero indica que el programa terminó con un error.
    sys.exit(1)

# Esta tarea solo se ejecuta si no se produjo el error anterior.
print('Otra tarea a ejecutar!')

# El código 0 comunica al sistema que el programa finalizó correctamente.
# sys.exit() detiene la ejecución, por lo que nada posterior llegaría a correr.
sys.exit(0)
