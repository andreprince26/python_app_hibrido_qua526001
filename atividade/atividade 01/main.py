import os

nome = input("informe seu nome: ").strip().title()      # srting
email = input("informe seu email: ").strip().lower()    # srting letra maiuscula ou minuscula
CPF = int(input("informe seu CPF: ").strip())           # srting
telefone = int(input("informe o telefone: ").strip())   # srting

os.system("cls") #limpa o console

print(f"nome: {nome}")
print(f"e-mail: {email}")
print(f"CPF: {CPF}")
print(f"telefone: {telefone}")
