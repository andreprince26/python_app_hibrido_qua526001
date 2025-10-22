# tratamento de execeçao
try:
    # entrada de dados
    nome = input("informe seu nome: ").strip().title()
    idade = int(input("informe sua idade: ").strip())
    altura = float(input("informe sua altura: ").strip().replace(",","."))
     
     # saida de dados
    print(f"nome: {nome}")
    print(f"idade: {idade}")
    print(f"altura: {altura}")

    # Todo
except:
    print("infelizmente o programa nao pode ser executado.")

