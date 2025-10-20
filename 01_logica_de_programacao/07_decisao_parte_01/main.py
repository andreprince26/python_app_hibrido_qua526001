# declaraçao de variavel
nome = input("informe seu nome: ").strip().title()
idade = int(input("informe sua idade: ") .strip())

#decisao
if idade >= 18:
    print(f"{nome} e maior de idade.")
else:
    print(f"{nome} e menor de idade.")
