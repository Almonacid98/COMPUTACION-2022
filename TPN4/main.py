from class_book import *
from class_custumer import *
from class_library import *

def menuinicio():
    while True:
            print("Bienvenidos a la bibloteca virtual, que desea realizar")
            print("1 = Agregar clientes:")
            print("2 = Agregar libros:")
            print("3 = Mostrar libros de la biblioteca:")
            print("4 = Mostrar clientes de la biblioteca:")
            print("5 = Ver información de cada libro:")
            print("6 = Ver información de cada cliente:")
            print("7 = Asignar un libro a un cliente:")
            print("8 = Ver libro asignado")
            print("9 = EXIT")
            choice = input("PRESIONE LAS SIGUIENTES OPCIONES PARA PODER EMPEZAR[1/2/3/4/5/6/7/8/9]  = ")
            if choice == '1':
                libreria.agregar_cliente()

            elif choice == '2':
                libreria.agregar_libros()

            elif choice == '3':
                libreria.show_books()

            elif choice == "4":
                libreria.show_clients()

            elif choice == "5":
                libreria.view_book()

            elif choice == "6":
                libreria.view_custumers()

            elif choice == "7":
                libreria.assign_wach()
                
            elif choice == "8":
                libreria.assign()
                
            elif choice == '9':
                print(
                    "GRACIAS POR UTILIZAR NUESTRO SERVICIO.... ESPERAMOS QUE SE HAYA PODIDO INFORMAR... HASTA LA PRÓXIMA!!")
                break
            else:
                print("\n OPCION INCORRECTA.... VUELVA A ELEGIR UNA OPCION EXISTENTE EN EL SISTEMA....")

libreria = Library()

menuinicio()