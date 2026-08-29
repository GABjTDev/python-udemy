def multiplicar(a, b):
    resultado = 0

    for _ in range(abs(b)):
        resultado += a

    return resultado if b >= 0 else -resultado


print(multiplicar(6, 4))   # 24
print(multiplicar(6, -4))  # -24