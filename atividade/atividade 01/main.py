import os

nome = input("informe seu nome: ").strip().title()# srting
email = input("informe seu email: ").strip().lower()# srting
CPF = input("informe seu CPF: ").strip()# srting
telefone = input("informe o telefone: ").strip()# srting

os.system("cls")

print(f"nome: {nome}")
print(f"e-mail: {email}")
print(f"CPF: {CPF}")
print(f"telefone: {telefone}")
