def suma_doble(a, b):
    if a == b:
        return (a + b)*2
    else:
        return a + b

primer_valor_a = int(input("Introduzca el primer valor a sumar: "))
segundo_valor_b = int(input("Introduzca el segundo valor a sumar:"))
valor = suma_doble(primer_valor_a, segundo_valor_b)
print(valor)
