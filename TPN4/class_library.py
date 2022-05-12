from cgi import print_form
from class_book import *
from class_custumer import *
class Library():
    
    __list_of_availible_books = []
    __client_list = []
    __diccionario_libros = {}
    __diccionario_clientes = {}

    def set_lista_de_libros(self, lista):
        self.__list_of_availible_books = lista

    def set_lista_clientes(self, lista):
        self.__client_list = lista

    def agregar_cliente(self):
        opcional = input("Desea agregar clientes si/no:")
        while(opcional == "si"):
            if(opcional == "si"):   
                name = input("Ingrese su nombre completo:")
                age = int(input("Ingrese su edad:"))
                adress = input("Ingrese su dirección de vivienda:")
                identificador = format(id(name))
                custumer = Custumer(identificador, name, age, adress)
                self.__client_list.append(custumer)
                finalizar = input("¿Desea seguir agregando clientes a la bibloteca? si / no :")    
                if(finalizar == "no"):
                    input("Presiona enter para volver al menu.......")
                    break

            
    def agregar_libros(self):
        opcional = input("Desea agregar libros si/no:")
        while(opcional == "si"):
            if(opcional == "si"): 
                title = input("Ingresa el titulo del libro: ")
                author = input("Ingresa el nombre del autor: ")
                cost = int(input("Ingresa el monto total del libro: "))
                identificador = format(id(title))
                book = Book(identificador, title, author, cost)
                book.set_title(title)
                book.set_author(author)
                book.set_cost(cost)
                self.__list_of_availible_books.append(book)
                finalizar = input("¿Desea seguir agregando libros a la bibloteca? si / no :")  
                if(finalizar == "no"):
                    input("Presiona enter para volver al menu.......")
                    break


    def show_books(self):
        for x in self.__list_of_availible_books:
            print("ID:", x.get_id(),"\nEl nombre del libro es: ", x.get_title())
        input("Presiona enter para volver al menu.......")

    def view_book(self):
        for x in self.__list_of_availible_books:
            print("ID:", x.get_id(),"\nEl nombre del libro es: ", x.get_title(), "\nEl autor del libro es:", x.get_author(), "\nEl precio del libro es: ", x.get_cost())
        input("Presiona enter para volver al menu.......")

    def show_clients(self):
        for x in self.__client_list:
            print("ID:", x.get_id(),"\nEl nombre del cliente es:", x.get_name())
        input("Presiona enter para volver al menu.......")

    def view_custumers(self):
        for x in self.__client_list:
            print("ID:", x.get_id(),"\nEl nombre del cliente es: ", x.get_name(), "\nLa edad del cliente es:", x.get_age(), "\nLa dirección de vivienda del cliente es: ", x.get_adress())
        input("Presiona enter para volver al menu.......")

    def assign_wach(self):
        for i in self.__client_list:
                self.__diccionario_clientes = {"id": i.get_id(),
                                               "Nombre del cliente": i.get_name()}
        for x in self.__list_of_availible_books:
                self.__diccionario_libros = {"id": x.get_id(),
                                             "Nombre del libro": x.get_title()}
        print(self.__diccionario_clientes)
        print(self.__diccionario_libros)
        nombre_cliente = input("Ingresa el numero de cliente para asociarlo al libro que requiera: ")
        nombre_libro = input("Ingresa el numero del libro para asociarlo con el cliente: ")
        if nombre_cliente == self.__diccionario_clientes['Nombre del cliente'] and nombre_libro == self.__diccionario_libros['Nombre del libro']:
            self.__diccionario_clientes.update(self.__diccionario_libros)

    def assign(self):
            print(self.__diccionario_clientes)
            input("Presiona enter para volver al menu.......")