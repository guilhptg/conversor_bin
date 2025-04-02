def decimal_para_binario(numero):
    if numero == 0:
        return "000000"
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    # Preenche com zeros à esquerda para ter 6 dígitos
    return binario.zfill(6)

numero = int(input("Digite um número decimal: "))
print(f"Binário (6 dígitos): {decimal_para_binario(numero)}")


def binario_para_decimal(binario):
    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal

binario = input("Digite um número binário: ")
print(f"Decimal: {binario_para_decimal(binario)}")


# TODO Interface interativa para escolher a conversão

# TODO Binário / Hexadecimal

# TODO Binario / Octal

# TODO Hexadecimal / Binário 
