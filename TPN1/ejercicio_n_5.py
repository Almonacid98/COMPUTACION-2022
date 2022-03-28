
def problema_loro(hablando, hora):
    if hablando == "si":
        if hora >= 0 and hora < 7:
            return True
    
        elif hora >= 7 and hora <= 20:
            return False
        
        elif hora > 20 and hora <= 23:
            return True
    else:
        if hora >= 0 and hora < 7:
            return False
            
        elif hora >= 7 and hora <= 20:
            return False

        elif hora > 20 and hora <= 23:
            return False


loro_hablando = input("¿El loro está hablando? si/no: ")
hora_hablando = int(input("¿Cual es la hora actual?: "))
print(problema_loro(loro_hablando, hora_hablando))