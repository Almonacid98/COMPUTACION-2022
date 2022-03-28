def caracter_perdido(str, n):

    if n >= -1 and n < len(str):
        str = str.replace(str[n], "")
        return str
    else:
        return "Fuera de rango"

cadena = input("Ingrese cadena de texto:")
valor_de_indice = int(input("Ingrese valor del indice a eliminar: "))
print(caracter_perdido(cadena, valor_de_indice))
