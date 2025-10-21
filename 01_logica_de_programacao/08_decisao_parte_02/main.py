# declaraçao de variaveis
nome = input("informe seu nome: ").strip().title()
idade = int(input("informe sua idade: ").strip())
altura = float(input("informe a altura: ").strip().replace(",","."))

# verificaçao das condiçoes
if idade >= 12 and altura >= 1.15:
    print(f"Entrada de {nome} autorizada.")
else:
    print(f"Entrada de {nome} nao autorizado.")


