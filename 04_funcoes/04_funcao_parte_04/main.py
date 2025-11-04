# biblioteca
import os
import math

def limpar():    #def(ele simplifica define)
    os.system("cls")


 # funçao de calculo
def quadrado(l):
    return l**2

def retangulo(b, h):
    return b*h

def triangulo(b, h):
    return (b*h)/2
def hipotenusa(c1, C2):
     return math.sqrt(c1**2)+(c2**2)

# algoritmo principal
limpar()

while True:
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retangulo")
    print("3 - Calcular Triangulo")
    print("4 - calcular hipotenusa")
    print("5 - Sair do Programa")
    opcao = input("Opçao desejada: ").strip()
    limpar()
    match opcao:
        case "1":
            l = float(input("informe o nome do quadrado:").strip().replace(",","."))
            resultado = quadrado(1)
            limpar()
            print(f"area do quadrado; {resultado}")
            continue
        case "2":
            b = float(input("informe a base do triangulo:").strip().replace(",","."))
            h = float(input("informe a altura do retangulo:").strip().replace(",","."))
            resultado = retangulo(b, h)
            limpar()
            print(f"area do triangulo: {resultado}")
            continue
        case "3":
            b = float(input("informe a base do triangulo: ").strip().replace(",","."))
            h = float(input("informe a altura do triangulo:").strip().replace(",","."))
            resultado = triangulo(b, h)
            limpar()
            print(f"area do triangulo: {resultado}")
            continue
        case "4":
            c1= float(input("informe 1 cateto: ").strip().replace(",","."))
            c2 = float(input("informe 2 cateto:").strip().replace(",","."))
            resultado = (c1, c2)
            limpar()
            print(f"hipotenusa e igual a : {resultado}")
            continue

        case "5":
            break
        case _:
            print("opçao invalida")











