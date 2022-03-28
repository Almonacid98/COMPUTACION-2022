def cerca_cien(n):
    if abs(n) >= 90 and abs(n) <= 100 or abs(n) >= 190 and abs(n) <= 200:
        return True
    else:
        return False

numero = int(input("Ingresa un numero dentro del rango 10, de 100 o 200: "))
print(cerca_cien(numero))