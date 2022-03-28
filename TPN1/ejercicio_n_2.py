
def problema_monos(a_sonriendo, b_sonriendo):

    if a_sonriendo == "si" and b_sonriendo == "si":
        print("¡ESTAMOS EN PROBLEMAS!")
        return True

    elif a_sonriendo == "no" and b_sonriendo == "no":
        print("¡ESTAMOS EN PROBLEMAS!")
        return True

    elif a_sonriendo == "si" and b_sonriendo == "no":
        print("NO HAY PROBLEMAS")
        return False
        
    elif a_sonriendo == "no" and b_sonriendo == "si":
        print("NO HAY PROBLEMAS")
        return False

mono_a = input("¿Mono A está sonriendo?: si/no: ")
mono_b = input("¿Mono B está sonriendo?: si/no: ")
print(problema_monos(mono_a, mono_b))

    
