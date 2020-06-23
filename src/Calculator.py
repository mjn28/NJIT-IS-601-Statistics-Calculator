#addition static method
def addition(a, b):
    return a + b

#subtraction static method
def subtraction (a, b):
    return a - b

class Calculator:

    result = 0

    #Defines constructor for Calculator object
    def __init__(self):
        pass

    #Add method
    def add(self, a, b):
        a=int(a)
        b=int(b)
        self.result = addition(a,b)
        return self.result

    #Subtract method
    def subtract(self, a, b):
        self.result = a - b
        return self.result