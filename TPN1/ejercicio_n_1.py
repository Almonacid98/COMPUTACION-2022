def dormimos(dia_semana, vacaciones):

    if dia_semana == "no" and vacaciones == "no":
        return True

    elif dia_semana == "si" and vacaciones == "no":
        return False

    elif dia_semana == "no" and vacaciones == "si":
        return True
        
    elif dia_semana == "si" and vacaciones == "si":
        return True

dia_semana = input("¿Es un dia de semana? si/no: ")
vacaciones = input("¿Usted está de vacaciones? si/no:")
print(dormimos(dia_semana, vacaciones))




