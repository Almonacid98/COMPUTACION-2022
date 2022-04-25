from curses import ACS_GEQUAL



class Custumer:
    name = ""
    age = ""
    adress = ""


    def __init__(self, name, age, adress) -> None:
        self.__name = name
        self.__age = age
        self.__adress = adress

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def name(self, age):
        self.__age = age

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress):
        self.__adress = adress
    
    
    def view(self):
        pass


