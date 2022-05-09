from class_book import *
from class_custumer import *
class Library():
    
    __list_of_availible_books = []
    __client_list = []

    def set_lista_de_libros(self, lista):
        self.__list_of_availible_books = lista

    def set_lista_clientes(self, lista):
        self.__client_list = lista

    def agregar_cliente(self):
        name = input("Ingrese su nombre completo:")
        age = int(input("Ingrese su edad:"))
        adress = input("Ingrese su dirección de vivienda:")
        custumer = Custumer(name, age, adress)
        self.__client_list.append(custumer)
    
    def agregar_libros(self):
        title = input("Ingresa el titulo del libro: ")
        author = input("Ingresa el nombre del autor: ")
        cost = int(input("Ingresa el monto total del libro: "))
        book = Book(title, author, cost)
        book.set_title(title)
        book.set_author(author)
        book.set_cost(cost)
        self.__list_of_availible_books.append(book)


    def show_books(self):
        contador = 0
        for x in self.__list_of_availible_books:
            contador = contador + 1
            print("\n", contador)
            print("\nEl nombre del libro es: ", x.get_title())
        input("Presiona enter para volver al menu.......")

    def view_book(self):
        contador = 0
        for x in self.__list_of_availible_books:
            contador = contador + 1
            print("\n", contador)
            print("\nEl nombre del libro es: ", x.get_title(), "\nEl autor del libro es:", x.get_author(), "\nEl precio del libro es: ", x.get_cost())
        input("Presiona enter para volver al menu.......")

    def show_clients(self):
        contador = 0
        for x in self.__client_list:
            contador = contador + 1
            print("\n", contador)
            print("\nEl nombre del cliente es:", x.get_name())
        input("Presiona enter para volver al menu.......")

    def view_custumers(self):
        contador = 0
        for x in self.__client_list:
            contador = contador + 1
            print("\n", contador)
            print("\nEl nombre del cliente es: ", x.get_name(), "\nLa edad del cliente es:", x.get_age(), "\nLa dirección de vivienda del cliente es: ", x.get_adress())
        input("Presiona enter para volver al menu.......")



    def assign(self):
        contador = int(input("Ingrese el numero del libro a asignar:"))
        contador1 = int(input("Ingrese el numero del cliente a asignar:"))
        if contador:
            print("\nEl nombre del libro: ", self.show_books(),"\n")
            if contador1:
                print("\nEl nombre del cliente es: ", self.show_books())
        input("Presiona enter para volver al menu.......")
"""     contador = 0
        for x in self.__client_list:
            contador = contador + 1
            numero_libro = input("Ingrese el numero del indice del libro que quiere adquirir:")
            numero_cliente = input("Ingrese el cliente al cual asignar el libro:")
            if numero_libro == self.__list_of_availible_books[contador] and numero_cliente == self.__client_list[contador]:
                result = self.__client_list[numero_cliente] + self.__list_of_availible_books[numero_libro]
                lista = [result]
                print(lista)
"""