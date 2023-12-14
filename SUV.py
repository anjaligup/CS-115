class Automobile:
    def __init__(self, make, model, price):
        self.__make = make
        # defined with double underscore -> class atributes MUST be private
        self.__model = model
        self.__price = price

    #getters 
    def get_make(self):
        # must create getter and setter for every private atribute
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    # setters
    def set_make(self, newMake):
        # one more parameter besides self
        # set method DOES NOT return anything 
        self.__make = newMake

    def set_model(self, newModel):
        self.__model = newModel

    def set_price(self, newPrice):
        self.__price = newPrice
        

    def __gt__(self, other):
        # gt = greater than
        return self.__price > other.__price

    def __ge__(self, other):
        # ge = greater than or equal to
        return self.__price >= other.__price

    def __str__(self):
        return self.__make + " " + self.__model

# subclass can use superclass methods not vica versa 

class SUV(Automobile):
    # subclass of Automobile
    def __init__(self, make, model, price, pass_cap):
        Automobile.__init__(self, make, model, price)
        self.__pass_cap = pass_cap

    # getter
    def get_pass_cap(self):
        return self.__pass_cap

    # setter
    def set_pass_cap(self, p):
        self.__pass_cap = p

    def __str__(self):
        # can not directly access private variables from superclass like this: 
        # return self.__make + " " + self.__model
        return self.get_make() + " " + self.get_model() + " " + str(self.get_pass_cap())

    # polymorphism 
