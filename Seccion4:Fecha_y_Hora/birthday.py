# Importamos:
# - datetime: permite convertir un texto (string) en una fecha.
# - date: permite obtener la fecha actual.
from datetime import datetime, date


# Solicitamos al usuario su fecha de nacimiento.
# El dato ingresado se guarda inicialmente como un string.
fecha_nacimiento_str = input(
    "Ingrese su fecha de nacimiento (DD/MM/AAAA): "
)


# Convertimos el string ingresado en un objeto de tipo date.
#
# strptime() interpreta el texto según el formato indicado:
# %d = día con dos dígitos
# %m = mes con dos dígitos
# %Y = año con cuatro dígitos
#
# Por ejemplo: "25/08/1995"
#
# strptime() devuelve un objeto datetime, por eso utilizamos
# .date() para quedarnos únicamente con la fecha.
fecha_nacimiento = datetime.strptime(
    fecha_nacimiento_str,
    "%d/%m/%Y"
).date()


# Obtenemos la fecha actual del sistema.
fecha_actual = date.today()


# Calculamos una edad inicial restando el año de nacimiento
# al año actual.
edad = fecha_actual.year - fecha_nacimiento.year


# Comparamos el mes y el día actuales con el mes y el día
# del cumpleaños.
#
# Python compara las tuplas de izquierda a derecha:
# primero compara el mes y, si son iguales, compara el día.
#
# Si la fecha actual está antes del cumpleaños, significa que
# la persona todavía no cumplió años este año.
if (fecha_actual.month, fecha_actual.day) < (
    fecha_nacimiento.month,
    fecha_nacimiento.day
):
    # Restamos un año porque todavía no llegó su cumpleaños.
    edad -= 1


# Mostramos la edad calculada.
print(f"La persona tiene {edad} años.")