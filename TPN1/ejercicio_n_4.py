def diferencia_absoluta(n):
    
    if n <= 21 and n >= 0:
        n = abs(n) - 21
        return abs(n)
    else:
        n = (abs(n) - 21)*2
        return abs(n)

valor_n = int(input("Introduzca un número: "))
print(diferencia_absoluta(valor_n))