
name = 'Factura de Steam'
game_1 = float(59.99)
game_2 = float(39.99)

def __main__():
    print("Factura")
    amount_bruto = game_1 + game_2
    amount_impuesto = amount_bruto * 0.19
    amount_total = amount_bruto + amount_impuesto
    print(f"El bruto es: ${amount_bruto:.2f}")
    print(f"El impuesto es: ${amount_impuesto:.2f}")
    print(f"El total es: ${amount_total:.2f}")

__main__()