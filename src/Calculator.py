#addition static method
def addition(a, b):
    return a + b

class Calculator:

    result = 0

    #Defines constructor for Calculator object
    def __init__(self):
        pass

    #Addition method
    def add(self, a, b):
        self.result = a + b
        return addition(a,b)