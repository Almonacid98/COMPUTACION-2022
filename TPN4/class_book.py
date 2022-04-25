from class_library import Library
class Book(Library):
    title = ""
    author = ""
    cost = ""
    def __init__(self, title, author, cost) -> None:
        super().__list_of_availible_books
        self.__title = title
        self.__author = author 
        self.__cost = cost


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author
    
    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    
    def view(self):
        pass