tank_status = float(input("Introduce el estado del tanque de gasolina: "))

if tank_status == 70:
    print('Estanque lleno')
elif tank_status >= 60 and tank_status < 70:
    print('Estanque casi lleno')
elif tank_status >= 40 and tank_status < 60:
    print('Estanque 3/4')
elif tank_status >= 35 and tank_status < 40:
    print('Medio Estanque')
elif tank_status >= 20 and tank_status < 35:
    print('Suficiente')
elif tank_status >= 1 and tank_status < 20:
    print('Insuficiente')