texto = "no"
def no_cadena(str):

    if str[0] == "n" and str[1] == "o" and str[2] == " ":
        return str
    else:
        return texto + ' ' + str
    

cadena = input("Ingrese cadena de texto:")
print(no_cadena(cadena))
