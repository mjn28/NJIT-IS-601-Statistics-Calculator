import math

#Addition static method
def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b

#Subtraction static method
def subtraction (a, b):
    a = int(a)
    b = int(b)
    return b - a

#Multiplication static method
def multiplication (a, b):
    a = int(a)
    b = int(b)
    return a * b

#Division static method
def division (a, b):
    a = float(a)
    b = float(b)
    return b / a

#Squared static method
def squared (a):
    a = int(a)
    return a*a

#Squared root static method
def squared_root (a):
    a = int(a)
    return a/a

class Calculator:

    result = 0

    #Defines constructor for Calculator object
    def __init__(self):
        pass

    #Add method
    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    #Subtract method
    def subtract(self, a, b):
        self.result = subtraction(a,b)
        return self.result

    #Multiply method
    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    #Divide method
    def divide(self, a, b):
        self.result = division(a, b)
        return round(float(self.result), 9)

    #Square method
    def square(self, a):
        self.result = squared(a)
        return self.result