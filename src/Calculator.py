#addition static method
def addition(a, b):
    return a + b

#subtraction static method
def subtraction (a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

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
        self.result = subtraction(a,b)
        return self.result