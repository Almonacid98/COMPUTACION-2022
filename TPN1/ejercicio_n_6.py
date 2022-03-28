
from re import S


def hacer10(a,b):
    suma = a + b 
    if suma == 10:
        return True

    if a == 10 or b == 10:
        return True

    if a == 10 and b != 10:
        return True

    if a != 10 and b == 10:
        return True
        
    if a != 10 and b != 10:
        return False
   
    

primer_valor_a = int(input("Introduzca el primer valor a sumar: "))
segundo_valor_b = int(input("Introduzca el segundo valor a sumar:"))
valor = hacer10(primer_valor_a, segundo_valor_b)
print(valor)
