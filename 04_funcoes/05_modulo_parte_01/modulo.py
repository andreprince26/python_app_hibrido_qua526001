# biblioteca
import math
import os

# funcoes
def quadrado(l):
    return l**2

def retangulo(b, h):
    return b*h

def triangulo(b, h):
    return (b*h)/2

def circulo(r):
    return math.pi*(r**2)

def trapezio(b,B, h):
    return ((b+B)*h)/2

def limpar():
    os.system("cls")
