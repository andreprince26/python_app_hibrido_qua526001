# biblioteca
import os

# funcao

def boas_vindas(nome):
    os.system("cls")
    print(f"seja bem vindo, {nome} ")

    #algoritmo principal
os.system("cls")
nome = input("informe seu nome: ").strip().title()
boas_vindas(nome)
