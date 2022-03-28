def pos_negativa(a, b, negativo):
    if a != 0 or b != 0:
        if a > 0 and b < 0 and negativo == "False":
            return True

        if a < 0 and b > 0 and negativo == "False":
            return True

        if a < 0 and b < 0:
            return True
            
        if negativo == "True":
            return False
    else:
        print("El número ingresado no es negativo ni positivo")


primer_valor_a = int(input("Introduzca el primer valor: "))
segundo_valor_b = int(input("Introduzca el segundo valor:"))
bool_parameter = (input("Ingrese su parametro como booleano: True or False ---> "))
print(pos_negativa(primer_valor_a, segundo_valor_b, bool_parameter))
