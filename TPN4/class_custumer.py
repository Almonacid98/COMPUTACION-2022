class Custumer():


    def __init__(self, name, age, adress) -> None:
        self.__name = name
        self.__age = age
        self.__adress = adress
    
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_adress(self, adress):
        self.__adress = adress

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def get_adress(self):
        return self.__adress

