#biblioteca
import os

#funcao
def boas_vindas(nome):
    os.system("cls")
    return f"seja bem vindo, {nome}!"

# algoritmo principal
os.system("cls")
nome = input("informe seu nome: ").strip().title()
resultado = boas_vindas(nome)
print(resultado)
